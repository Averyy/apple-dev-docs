# Counting human body action repetitions in a live video feed

**Framework**: Create ML Components

Use Create ML Components to analyze a series of video frames and count a person’s repetitive or periodic body movements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Xcode 14.0+

#### Overview

> **Note**: This sample code project is associated with WWDC22 session [`110332: What’s new in Create ML`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110332/).

This sample code project is associated with WWDC22 session [`110332: What’s new in Create ML`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110332/).

This sample app counts a person’s repetitive or periodic body movements () by analyzing a series of video frames and making a prediction with a human body action repetition counter. The counter in this sample can count arbitrary body moves that occur at moderate speed, such as jumping jacks, dance spins, and waving arms.

![A flow diagram that illustrates two people performing jumping jacks in front of a device’s camera. A video reader extracts video frames from the camera, and then the pose extractor consumes the frames to generate poses of body location data. The Create ML Components framework consumes the pose data and predicts the count for the jumping jacks.](https://docs-assets.developer.apple.com/published/9eff398948/renderedDark2x-1658773614.png)

The app continually presents the current action repetition count on top of a live, full-screen video feed from the camera in portrait orientation. When the app detects one or more people in the frame, it overlays a wireframe body pose on each person. At the same time, the app predicts the action repetition count about the most prominent person across multiple frames, typically whoever is closest to the camera.

The app begins by configuring a camera to generate video frames, then directs the frames through a series of transformers it chains together with Create ML Components. These methods work together to:

1. Read camera frames in real time using [`VideoReader`](videoreader.md).
2. Analyze each frame to locate any human body poses using [`HumanBodyPoseExtractor`](humanbodyposeextractor.md), and redirect the pose stream with an [`AsyncChannel`](https://developer.apple.comhttps://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncAlgorithms.docc/Guides/Channel.md) to allow multiple consumers.
3. Optionally, downsample the stream using a [`Downsampler`](downsampler.md) to process the observed actions in different speeds. To improve performance, you can move the downsampler to an earlier stage in the pipeline if you don’t need to render poses on every frame.
4. Isolate the prominent pose using [`PoseSelector`](poseselector.md).
5. Optionally, use [`JointsSelector`](jointsselector.md) to select only joints of interest for counting.
6. Aggregate the prominent pose’s position data over time using [`SlidingWindowTransformer`](slidingwindowtransformer.md).
7. Predict action repetitions by sending aggregate data to the [`HumanBodyActionCounter`](humanbodyactioncounter.md).

##### 4065198

This sample code project requires a device with iOS 16 or later, or iPadOS 16 or later.

To build this project:

1. Double-click the `CountMyActions.xcodeproj` project to open it in Xcode.
2. In Xcode, from the Project navigator, select the `CountMyActions` project and click the Signing & Capabilities tab.
3. Select your development team from the Add Account pop-up menu.
4. Select your target device from the scheme menu, and choose Product > Run.

##### 4065199

The app uses [`VideoReader`](videoreader.md) to configure the device’s camera and generate an asynchronous video frame sequence. The [`VideoReader.CameraConfiguration`](videoreader/cameraconfiguration.md) specifies the front- or rear-facing camera, and configures its pixel format and resolution. This app supports portrait orientation only. Low lighting and other factors can vary the frame rate, which may affect the counting performance, so ensure the person’s full body is visible in bright environments.

```swift
/// The camera configuration to define the basic camera position, pixel format, and resolution to use.
private var configuration = VideoReader.CameraConfiguration()
```

When the app first launches — or when the user toggles the camera — the video reader configures a camera device, starts the video-processing pipeline, and produces a frame sequence output with [`readCamera(configuration:)`](videoreader/readcamera(configuration:).md).

```swift
/// Start the video-processing pipeline by displaying the poses in the camera frames and
/// starting the action repetition count prediction stream.
func startVideoProcessingPipeline() {

    if let displayCameraTask = displayCameraTask {
        displayCameraTask.cancel()
    }

    displayCameraTask = Task {
        // Display poses on top of each camera frame.
        try await self.displayPoseInCamera()
    }

    if predictionTask == nil {
        predictionTask = Task {
            // Predict the action repetition count.
            try await self.predictCount()
        }
    }
}
```

##### 4065200

The [`HumanBodyPoseExtractor`](humanbodyposeextractor.md) is a transformer that can locate any human body poses from an image or a video frame.

```swift
/// A Create ML Components transformer to extract human body poses from a single image or a video frame.
/// - Tag: poseExtractor
private let poseExtractor = HumanBodyPoseExtractor()
```

When the transformation completes, the method creates and returns a [`Pose`](pose.md) array that contains one pose for every detected person in the same frame.

```swift
// Extract poses in every frame.
let poses = try await poseExtractor.applied(to: frame.feature)
```

The `Pose` structure serves the following purposes:

- Calculates the pose’s area within a frame (See the “Isolate a body pose” section below.).
- Draws each detected pose as a wireframe of points and lines (See the “Present the poses to the user” section below.).

For more information about the underlying human body pose model, see [`Detecting Human Body Poses in Images`](https://developer.apple.com/documentation/vision/detecting-human-body-poses-in-images).

##### 4065201

[`AsyncChannel`](https://developer.apple.comhttps://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncAlgorithms.docc/Guides/Channel.md) sends the extracted poses to a separate asynchronous stream. This allows additional consumers to obtain poses from the upstream asynchronous sequence. [`AsyncChannel`](https://developer.apple.comhttps://github.com/apple/swift-async-algorithms/blob/main/Sources/AsyncAlgorithms/AsyncAlgorithms.docc/Guides/Channel.md) requires the inclusion of the [`AsyncAlgorithms`](https://developer.apple.comhttps://github.com/apple/swift-async-algorithms) Swift package.

```swift
/// An asynchronous channel to divert the pose stream for another consumer.
private let poseStream = AsyncChannel<TemporalFeature<[Pose]>>()
```

##### 4065202

The `ActionCounter` structure consists of a pipeline of Create ML Components transformers to achieve continuous action repetition counting. It takes a pose stream as input and returns an asynchronous sequence of cumulative counts.

```swift
/// The counter to count action repetitions from a pose stream.
private let actionCounter = ActionCounter()
```

##### 4065203

The first optional transformer in the pipeline, [`Downsampler`](downsampler.md), downsamples the incoming pose sequence by an integer factor. This allows the pipeline to process and count much slower actions. For example, without downsampling, the original counter model can handle moderate speed actions, about one repetition per second, such as jumping jacks. A downsampling factor of three can effectively speed up slower actions, such as pushups or a complex dance sequence with about one repetition per 3 seconds, and still allow the model to count the actions.

```swift
// Use an optional Downsampler transformer to downsample the
// incoming frames (that is, effectively speed up the observed actions).
let pipeline = Downsampler(factor: 1)
```

##### 4065204

The next transformer in the pipeline, [`PoseSelector`](poseselector.md), selects a single pose from the array of poses by using the default strategy, namely, selecting the most prominent person by their maximum bounding box area.

```swift
// Use a PoseSelector transformer to select one pose to count if
// the system detects multiple poses.
    .appending(PoseSelector(strategy: .maximumBoundingBoxArea))
```

The goal of this strategy is to consistently select the same person’s pose from a crowd over time.

![A flow diagram that illustrates two detected poses in the same frame passing into a pose selector, where the default strategy selects the most-prominent pose, and the output is a single pose. ](https://docs-assets.developer.apple.com/published/e848533bc0/renderedDark2x-1658258329.png)

> ❗ **Important**: Get the most accurate predictions by using whatever strategy best tracks a person from frame to frame.

Get the most accurate predictions by using whatever strategy best tracks a person from frame to frame.

##### 4065205

The next optional transformer in the pipeline, [`JointsSelector`](jointsselector.md), selects or ignores a specified subset of body joints from the pose.

![A flow diagram that illustrates a full body pose passing into a joints selector, which reduces it to a subset of joints that consists of an upper-body-only pose. ](https://docs-assets.developer.apple.com/published/adeb7bee6f/renderedDark2x-1658258330.png)

For example, to count only upper-body movements, the transformer can ignore lower-body joints in the pose, such as knees and ankles, which can eliminate noise by ignoring any leg movements.

```swift
// Use an optional JointsSelector transformer to specifically ignore
// or select a set of joints in a pose to include in counting.
    .appending(JointsSelector(ignoredJoints: [.nose, .leftEye, .leftEar, .rightEye, .rightEar]))
```

##### 4065206

The next transformer in the pipeline is a [`SlidingWindowTransformer`](slidingwindowtransformer.md) that receives a pose sequence from its upstream and gathers the frames into an array by providing the following parameters:

- A `stride` that determines the number of frames to count before updating the pose window
- A `length` that determines the window size, namely, how many frames to group together

```swift
// Use a SlidingWindowTransformer to group frames into windows, and
// prepare them for prediction.
    .appending(SlidingWindowTransformer<Pose>(stride: 5, length: 90))
```

![A flow diagram that illustrates a pose sequence passing into a sliding window transformer, which defines the stride and length for its window. ](https://docs-assets.developer.apple.com/published/c29f8c7dd9/rendered2x-1658258332.png)

The action repetition counter assumes a fixed length of 90, where the sliding window transformer groups 90 frames together to generate a single prediction count. The stride is adjustable. An example is a stride of 10 frames, indicating the count updates every 10 frames, which is about 0.3 seconds if the frame rate is 30 frames per second. When the stride is smaller than the length, the windows overlap.

##### 4065207

The next transformer in the pipeline, [`HumanBodyActionCounter`](humanbodyactioncounter.md), takes a stream of grouped pose windows as input and produces a [`HumanBodyActionCounter.CumulativeSumSequence`](humanbodyactioncounter/cumulativesumsequence.md) where each result is a cumulative count of the actions in the sequence. Live counting occurs by iterating each item in the resulted sequence.

```swift
// Use a HumanBodyActionCounter transformer to count actions from
// each window and produce cumulative counts for the input stream.
    .appending(HumanBodyActionCounter())
```

##### 4065208

The final count appears as a [`SwiftUI`](https://developer.apple.com/documentation/swiftui) label on the screen using the `OverlayView` structure on the main thread.

##### 4065209

The app visualizes the result of each detected human body pose by drawing the poses on top of the frame that [`HumanBodyPoseExtractor`](humanbodyposeextractor.md) finds them in. Each time the `poseExtractor` creates an array of [`Pose`](pose.md) instances, the `PosesView` iterates each detected pose and draws it by calling its `drawWireframe(to:applying:)` method, which draws the pose as a wireframe of connection lines and joint circles.

```swift
// Draw all the poses Vision finds in the frame.
for pose in poses {
    // Draw each pose as a wireframe at the scale of the image.
    pose.drawWireframe(to: context, applying: pointTransform)
}
```

The `ViewModel` presents the image and poses onscreen by calling `display(image:, poses:)` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/counting_human_body_action_repetitions_in_a_live_video_feed)*