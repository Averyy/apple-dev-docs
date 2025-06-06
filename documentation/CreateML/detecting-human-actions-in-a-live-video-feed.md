# Detecting Human Actions in a Live Video Feed

**Framework**: Createml

Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Xcode 12.3+

#### Overview

This sample app recognizes a person’s body moves, called , by analyzing a series of video frames with [`Vision`](https://developer.apple.com/documentation/vision) and predicting the name of the movement by applying an action classifier. The action classifier in this sample recognizes three exercises:

- Jumping jacks
- Lunges
- Burpees

![Flow diagram that illustrates the purpose of an action classifier starting with a human performing jumping jacks in front of the device’s camera and ending with a prediction label. Starting at the top of the flow diagram, a camera generates video frames. The Vision framework consumes the frames to generate a data window of body location data. The action classifier consumes the data window and predicts the label: Jumping Jacks.](https://docs-assets.developer.apple.com/published/6969ad3794/rendered2x-1612563032.png)

> **Note**: See `Creating an Action Classifier Model` for information about creating your own action classifier.

The app continually presents its current action prediction on top of a live, full-screen video feed from the device’s camera. When the app recognizes one or more people in the frame, it overlays a wireframe body pose on each person. At the same time, the app predicts the  person’s current action; typically this is the person closest to the camera.

![A diagram that represents the sample app’s main view. The image prominently shows a human figure performing jumping jacks. The app draws a body wireframe of circles connected by lines at key locations, overlaid on the arms, legs, and torso. Two text labels at the bottom of the view read Jumping Jacks and 98.7%. ](https://docs-assets.developer.apple.com/published/799c02125a/rendered2x-1612816327.png)

At launch, the app configures the device’s camera to generate video frames and then directs the frames through a series of methods it chains together with [`Combine`](https://developer.apple.com/documentation/combine). These methods work together to analyze the frames and make action predictions by performing the following sequence of steps:

1. Locate all human body poses in each frame.
2. Isolate the prominent pose.
3. Aggregate the prominent pose’s position data over time.
4. Make action predictions by sending the aggregate data to the action classifier.

![A flow diagram that illustrates the path of video frames through the sample app, beginning with the device camera, and continuing through a video capture, video-processing chain, and the main view controller, ending at a mockup of the app’s interface. The interface shows a human figure augmented with a wireframe overlaid on the arms, legs, and torso, performing jumping jacks above two labels that read: “Jumping Jacks” and “98.7%.”](https://docs-assets.developer.apple.com/published/d6120914d4/rendered2x-1612816330.png)

##### 3744220

This sample app uses a camera, so you can’t run it in Simulator — you need to run it on an iOS or iPadOS device.

##### 3744221

The app’s `VideoCapture` class configures the device’s camera to generate video frames by creating an [`AVCaptureSession`](https://developer.apple.com/documentation/avfoundation/avcapturesession).

When the app first launches, or when the user rotates the device or switches between cameras, video capture configures a camera input, a frame output, and the connection between them in its `configureCaptureSession()` method.

```swift
// Set the video camera to run at the action classifier's frame rate.
let modelFrameRate = ExerciseClassifier.frameRate

let input = AVCaptureDeviceInput.createCameraInput(position: cameraPosition,
                                                   frameRate: modelFrameRate)

let output = AVCaptureVideoDataOutput.withPixelFormatType(kCVPixelFormatType_32BGRA)

let success = configureCaptureConnection(input, output)
return success ? output : nil
```

The `createCameraInput(position:frameRate:)` method selects the front- or rear-facing camera and configures its frame rate so it matches that of the action classifier.

> ❗ **Important**: If you replace the `ExerciseClassifier.mlmodel` file with your own action classifier model, set the `frameRate` property to match the Frame Rate training parameter you used in the Create ML developer tool.

The `AVCaptureVideoDataOutput.withPixelFormatType(_:)` method creates an [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) that produces frames with a specific pixel format.

The `configureCaptureConnection(_:_:)` method configures the relationship between the capture session’s camera input and video output by:

- Selecting a video orientation
- Deciding whether to horizontally flip the video
- Enabling image stabilization when applicable

```swift
if connection.isVideoOrientationSupported {
    // Set the video capture's orientation to match that of the device.
    connection.videoOrientation = orientation
}

if connection.isVideoMirroringSupported {
    connection.isVideoMirrored = horizontalFlip
}

if connection.isVideoStabilizationSupported {
    if videoStabilizationEnabled {
        connection.preferredVideoStabilizationMode = .standard
    } else {
        connection.preferredVideoStabilizationMode = .off
    }
}
```

The method keeps the app operating in real time — and avoids building up a frame backlog — by setting the video output’s [`alwaysDiscardsLateVideoFrames`](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/alwaysdiscardslatevideoframes) property to `true`.

```swift
// Discard newer frames if the app is busy with an earlier frame.
output.alwaysDiscardsLateVideoFrames = true
```

See [`Setting Up a Capture Session`](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session) for more information on how to configure capture sessions and connect their inputs and outputs.

##### 3744222

The video capture publishes frames from its capture session by creating a [`PassthroughSubject`](https://developer.apple.com/documentation/combine/passthroughsubject) in its `createVideoFramePublisher()` method.

```swift
// Create a new passthrough subject that publishes frames to subscribers.
let passthroughSubject = PassthroughSubject<Frame, Never>()

// Keep a reference to the publisher.
framePublisher = passthroughSubject
```

A passthrough subject is a concrete implementation of [`Subject`](https://developer.apple.com/documentation/combine/subject) that adapts imperative code to work with [`Combine`](https://developer.apple.com/documentation/combine). It immediately publishes the instance you pass to its [`send(_:)`](https://developer.apple.com/documentation/combine/subject/send(_:)) method, if it has a subscriber at that time.

Next, the video capture registers itself as the video output’s delegate so it receives the video frames from the capture session by calling the output’s [`setSampleBufferDelegate(_:queue:)`](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/setsamplebufferdelegate(_:queue:)) method.

```swift
// Set the video capture as the video output's delegate.
videoDataOutput.setSampleBufferDelegate(self, queue: videoCaptureQueue)
```

The video capture forwards each frame it receives to its `framePublisher` by passing the frame to its [`send(_:)`](https://developer.apple.com/documentation/combine/subject/send(_:)) method.

```swift
extension VideoCapture: AVCaptureVideoDataOutputSampleBufferDelegate {
    func captureOutput(_ output: AVCaptureOutput,
                       didOutput frame: Frame,
                       from connection: AVCaptureConnection) {

        // Forward the frame through the publisher.
        framePublisher?.send(frame)
    }
}
```

##### 3744223

The sample processes each video frame, and its derivative data, with a series of methods that it connects together into a chain of [`Combine`](https://developer.apple.com/documentation/combine) publishers in the `VideoProcessingChain` class.

Each time the video capture creates a new frame publisher it notifies the main view controller, which then assigns the publisher to the video-processing chain’s `upstreamFramePublisher` property:

```swift
func videoCapture(_ videoCapture: VideoCapture,
                  didCreate framePublisher: FramePublisher) {
    updateUILabelsWithPrediction(.startingPrediction)
    
    // Build a new video-processing chain by assigning the new frame publisher.
    videoProcessingChain.upstreamFramePublisher = framePublisher
}
```

Each time the property’s value changes, the video-processing chain creates a new daisy chain of publishers by calling its `buildProcessingChain()` method.

![Flow diagram of the video-processing chain that consumes video frames and produces information to the main view controller. The first two items in the chain are Convert to CGImage and Find poses. The final item in the chain is Send Prediction, which the diagram separates from the Find Poses item with a vertical ellipsis that indicates an indeterminate number of chain items in between. An arrow, labeled CGImage plus poses, goes from the chain item Find Poses to the main view controller. Another arrow, labeled action prediction goes from the chain item Send Prediction to the main view controller. ](https://docs-assets.developer.apple.com/published/e599394187/rendered2x-1612563035.png)

The method creates each new publisher by calling one of the following [`Publisher`](https://developer.apple.com/documentation/combine/publisher) methods:

- [`map(_:)`](https://developer.apple.com/documentation/combine/publisher/map(_:)-99evh),
- [`compactMap(_:)`](https://developer.apple.com/documentation/combine/publisher/compactmap(_:)),
- [`scan(_:_:)`](https://developer.apple.com/documentation/combine/publisher/scan(_:_:)).
- [`filter(_:)`](https://developer.apple.com/documentation/combine/publisher/filter(_:))

For example, the publisher that subscribes to the initial frame publisher is a [`Publishers.CompactMap`](https://developer.apple.com/documentation/combine/publishers/compactmap) that converts each `Frame` (a type alias of `CMSampleBuffer`) it receives into a [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage) by calling the video-processing chain’s `imageFromFrame(_:)` method.

```swift
// Create the chain of publisher-subscribers that transform the raw video
// frames from upstreamFramePublisher.
frameProcessingChain = upstreamFramePublisher
    // ---- Frame (aka CMSampleBuffer) -- Frame ----

    // Convert each frame to a CGImage, skipping any that don't convert.
    .compactMap(imageFromFrame)

    // ---- CGImage -- CGImage ----

    // Detect any human body poses (or lack of them) in the frame.
    .map(findPosesInFrame)

    // ---- [Pose]? -- [Pose]? ----
```

The next sections explain the remaining publishers in the chain and the methods they use to transform their inputs.

##### 3744224

The next publisher in the chain is a [`Publishers.Map`](https://developer.apple.com/documentation/combine/publishers/map) that receives each [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage) from the previous publisher (the compact map) by subscribing to it. The map publisher locates any human body poses in the frame by using the video-processing chain’s `findPosesInFrame(_:)` method. The method invokes a [`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest) by creating a [`VNImageRequestHandler`](https://developer.apple.com/documentation/vision/vnimagerequesthandler) with the image and submitting the video-processing chain’s `humanBodyPoseRequest` property to the handler’s [`perform(_:)`](https://developer.apple.com/documentation/vision/vnimagerequesthandler/perform(_:)) method.

> ❗ **Important**: Improve your app’s efficiency by creating and reusing a single [`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest) instance.

```swift
// Create a request handler for the image.
let visionRequestHandler = VNImageRequestHandler(cgImage: frame)

// Use Vision to find human body poses in the frame.
do { try visionRequestHandler.perform([humanBodyPoseRequest]) } catch {
    assertionFailure("Human Pose Request failed: \(error)")
}
```

When the request completes, the method creates and returns a `Pose` array that contains one pose for every [`VNHumanBodyPoseObservation`](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation) instance in the request’s [`results`](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/results) property.

```swift
let poses = Pose.fromObservations(humanBodyPoseRequest.results)
```

The `Pose` structure in this sample serves three main purposes:

- Calculating the observation’s area within a frame (see “Isolate A Body Pose”)
- Storing the the observation’s multiarray (see “Retrieve the Multiarray”)
- Drawing an observation as a wireframe of points and lines (see “Present the Poses to the User”)

For more information about using a [`VNDetectHumanBodyPoseRequest`](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest), see [`Detecting Human Body Poses in Images`](https://developer.apple.com/documentation/vision/detecting-human-body-poses-in-images).

##### 3744225

The next publisher in the chain is a map that chooses a single pose from the array of poses by using the video-processing chain’s `isolateLargestPose(_:)` method. This method selects the the most prominent pose by passing a closure to the pose array’s [`max(by:)`](https://developer.apple.com/documentation/swift/array/max(by:)) method.

```swift
private func isolateLargestPose(_ poses: [Pose]?) -> Pose? {
    return poses?.max(by:) { pose1, pose2 in pose1.area < pose2.area }
}
```

The closure compares the poses’ area estimates, with the goal of consistently selecting the same person’s pose over time, when multiple people are in frame.

> ❗ **Important**: Get the most accurate predictions from an action classifier by using whatever technique you think best tracks a person from frame to frame, and use the multiarray from that person’s [`VNHumanBodyPoseObservation`](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation) result.

##### 3744226

The next publisher in the chain is a map that publishes the [`MLMultiArray`](https://developer.apple.com/documentation/coreml/mlmultiarray) from the pose’s `multiArray` property by using the video processing chain’s `multiArrayFromPose(_:)` method.

```swift
private func multiArrayFromPose(_ item: Pose?) -> MLMultiArray? {
    return item?.multiArray
}
```

The `Pose` initializer copies the multiarray from its [`VNHumanBodyPoseObservation`](https://developer.apple.com/documentation/vision/vnhumanbodyposeobservation) parameter by calling the observation’s [`keypointsMultiArray()`](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/keypointsmultiarray()) method.

```swift
// Save the multiarray from the observation.
multiArray = try? observation.keypointsMultiArray()
```

##### 3744227

The next publisher in the chain is a [`Publishers.Scan`](https://developer.apple.com/documentation/combine/publishers/scan) that receives each multiarray from its upstream publisher and gathers them into an array by providing two arguments:

- An empty multiarray-optional array (`[`[`MLMultiArray`](https://developer.apple.com/documentation/coreml/mlmultiarray)`?]`) as the scan publisher’s initial value
- The video-processing chain’s `gatherWindow(previousWindow:multiArray:)` method as the scan publisher’s transform.

```swift
// ---- MLMultiArray? -- MLMultiArray? ----

// Gather a window of multiarrays, starting with an empty window.
.scan([MLMultiArray?](), gatherWindow)

// ---- [MLMultiArray?] -- [MLMultiArray?] ----
```

A scan publisher behaves similarly to a map, but it also maintains a state. The following scan publisher’s state is an array of multiarray optionals that’s initially empty. As the scan publisher receives multiarray optionals from its upstream publisher, the scan publisher passes its previous state and the incoming multiarray optional as arguments to its transform.

```swift
private func gatherWindow(previousWindow: [MLMultiArray?],
                          multiArray: MLMultiArray?) -> [MLMultiArray?] {
    var currentWindow = previousWindow

    // If the previous window size is the target size, it
    // means sendWindowWhenReady() just published an array window.
    if previousWindow.count == predictionWindowSize {
        // Advance the sliding array window by stride elements.
        currentWindow.removeFirst(windowStride)
    }

    // Add the newest multiarray to the window.
    currentWindow.append(multiArray)

    // Publish the array window to the next subscriber.
    // The currentWindow becomes this method's next previousWindow when
    // it receives the next multiarray from the upstream publisher.
    return currentWindow
}
```

The method:

1. Copies the `previousWindow` parameter to `currentWindow`
2. Removes `windowStride` elements from the front of `currentWindow`, if it’s full
3. Appends the `multiArray` parameter to the end of `currentWindow`

The video-processing chain considers a window to be full if it contains `predictionWindowSize` elements. When the window is full, this method removes (in step 2) the oldest elements to make room for newer elements, effectively sliding the window forward in time.

The Exercise Classifier’s `calculatePredictionWindowSize()` method determines the value of the prediction window size at runtime by inspecting the model’s [`modelDescription`](https://developer.apple.com/documentation/coreml/mlmodel/modeldescription) property.

##### 3744228

The next publisher in the chain is a [`Publishers.Filter`](https://developer.apple.com/documentation/combine/publishers/filter), which only publishes an array window when the `gateWindow(_:)` method returns `true`.

```swift
// Only publish a window when it grows to the correct size.
.filter(gateWindow)

// ---- [MLMultiArray?] -- [MLMultiArray?] ----
```

The method returns `true` if the window array contains exactly the number of elements defined in `predictionWindowSize`. Otherwise, the method returns `false`, which instructs the filter publisher to discard the current window and not publish it.

```swift
private func gateWindow(_ currentWindow: [MLMultiArray?]) -> Bool {
    return currentWindow.count == predictionWindowSize
}
```

This filter publisher, in combination with its upstream scan publisher, publishes an array of multiarray optionals (`[`[`MLMultiArray`](https://developer.apple.com/documentation/coreml/mlmultiarray)`?]`) once per each number of frames defined in `windowStride`.

##### 3744229

The next publisher in the chain makes an `ActionPrediction` from the multiarray window by using the `predictActionWithWindow(_:)` method as its transform.

```swift
// Make an activity prediction from the window.
.map(predictActionWithWindow)

// ---- ActionPrediction -- ActionPrediction ----
```

The method’s input array contains multiarray optionals where each `nil` element represents a frame in which [`Vision`](https://developer.apple.com/documentation/vision) wasn’t able to find any human body poses. An action classifier requires a valid, non-`nil` multiarray for every frame. To remove the `nil` elements in the array, the method creates a new multiarray, `filledWindow`, by:

- Copying each each valid element in `currentWindow`
- Replacing each `nil` element in `currentWindow` with an `emptyPoseMultiArray`

```swift
var poseCount = 0

// Fill the nil elements with an empty pose array.
let filledWindow: [MLMultiArray] = currentWindow.map { multiArray in
    if let multiArray = multiArray {
        poseCount += 1
        return multiArray
    } else {
        return Pose.emptyPoseMultiArray
    }
}
```

The empty pose multiarray has:

- Every element set to zero
- The same value for its [`shape`](https://developer.apple.com/documentation/coreml/mlmultiarray/shape) property as a multiarray from a human body-pose observation

As the method iterates through each element in `currentWindow`, it tallies the number of non-`nil` elements with `poseCount`.

If the value of `poseCount` is too low, the method directly creates a `noPersonPrediction` action prediction.

```swift
// Only use windows with at least 60% real data to make a prediction
// with the action classifier.
let minimum = predictionWindowSize * 60 / 100
guard poseCount >= minimum else {
    return ActionPrediction.noPersonPrediction
}
```

Otherwise, the method merges the array of multiarrays into a single, combined multiarray by calling the [`init(byConcatenatingMultiArrays:alongAxis:dataType:)`](https://developer.apple.com/documentation/coreml/mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:)) initializer.

```swift
// Merge the array window of multiarrays into one multiarray.
let mergedWindow = MLMultiArray(concatenating: filledWindow,
                                axis: 0,
                                dataType: .float)
```

The method generates an action prediction by passing the combined multiarray to the action classifier’s `predictActionFromWindow(_:)` helper method.

```swift
// Make a genuine prediction with the action classifier.
let prediction = actionClassifier.predictActionFromWindow(mergedWindow)

// Return the model's prediction if the confidence is high enough.
// Otherwise, return a "Low Confidence" prediction.
return checkConfidence(prediction)
```

The method checks the prediction’s confidence by passing the prediction to the `checkConfidence(_:)` helper method, which returns the same prediction if its confidence is high enough; otherwise `lowConfidencePrediction`.

##### 3744230

The final component in the chain is a subscriber that notifies the video-processing chain’s delegate with the prediction using the `sendPrediction(_:)` method.

```swift
// Send the action prediction to the delegate.
.sink(receiveValue: sendPrediction)
```

The method sends the action prediction and the number of frames the prediction represents (`windowStride`) to the video-processing chain’s `delegate`, the main view controller.

```swift
// Send the prediction to the delegate on the main queue.
DispatchQueue.main.async {
    self.delegate?.videoProcessingChain(self,
                                        didPredict: actionPrediction,
                                        for: windowStride)
}
```

Each time the main view controller receives an action prediction, it updates the app’s UI with the prediction and confidence in a helper method.

```swift
func videoProcessingChain(_ chain: VideoProcessingChain,
                          didPredict actionPrediction: ActionPrediction,
                          for frameCount: Int) {

    if actionPrediction.isModelLabel {
        // Update the total number of frames for this action.
        addFrameCount(frameCount, to: actionPrediction.label)
    }

    // Present the prediction in the UI.
    updateUILabelsWithPrediction(actionPrediction)
}
```

The main view controller also updates its `actionFrameCounts` property for action labels that come from the model, which it later sends to the Summary View Controller when the user taps the `Summary` button.

##### 3744231

The app visualizes the result of each human body-pose request by drawing the poses on top of the frame in which [`Vision`](https://developer.apple.com/documentation/vision) found them. Each time the video-processing chain’s `findPosesInFrame(_:)` creates an array of `Pose` instances, it sends the poses to its delegate, the main view controller.

```swift
// Send the frame and poses, if any, to the delegate on the main queue.
DispatchQueue.main.async {
    self.delegate?.videoProcessingChain(self, didDetect: poses, in: frame)
}
```

The main view controller’s `drawPoses(_:onto:)` method uses the frame as the background by first drawing the frame.

```swift
// Draw the camera image first as the background.
let imageRectangle = CGRect(origin: .zero, size: frameSize)
cgContext.draw(frame, in: imageRectangle)
```

Next, the method draws the poses by calling their `drawWireframeToContext(_:applying:)` method, which draws the pose as a wireframe of lines and circles.

```swift
// Draw all the poses Vision found in the frame.
for pose in poses {
    // Draw each pose as a wireframe at the scale of the image.
    pose.drawWireframeToContext(cgContext, applying: pointTransform)
}
```

The main view controller presents the finished image to the user by assigning it to its full-screen image view.

```swift
// Update the UI's full-screen image view on the main thread.
DispatchQueue.main.async { self.imageView.image = frameWithPosesRendering }
```

## See Also

- [Creating an Action Classifier Model](creating-an-action-classifier-model.md)
  Train a machine learning model to recognize a person’s body movements.
- [struct MLActionClassifier](mlactionclassifier.md)
  A model you train with videos to classify a person’s body movements.
- [struct MLHandActionClassifier](mlhandactionclassifier.md)
  A task that creates a hand action classification model by training with videos of people’s hand movements that you provide.
- [struct MLStyleTransfer](mlstyletransfer.md)
  A model you train to apply an image’s style to other images or videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/detecting_human_actions_in_a_live_video_feed)*