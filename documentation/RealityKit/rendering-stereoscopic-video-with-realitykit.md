# Rendering stereoscopic video with RealityKit

**Framework**: RealityKit

Render stereoscopic video in visionOS with RealityKit.

**Availability**:
- visionOS 26.0+
- Xcode 26.0+

#### Overview

visionOS offers a range of options for programmatic video playback, including:

- [`AVKit`](https://developer.apple.com/documentation/AVKit) provides a superior video playback experience in visionOS. With AVKit, you can present an interface that’s consistent with other apps on the system, with minimal adoption effort. For more information on using AVKit in visionOS, see [`Adopting the system player interface in visionOS`](https://developer.apple.com/documentation/AVKit/adopting-the-system-player-interface-in-visionos).
- [`RealityKit`](RealityKit.md) offer a greater degree of customization, using either [`VideoMaterial`](videomaterial.md) or [`VideoPlayerComponent`](videoplayercomponent.md).

`VideoMaterial` and `VideoPlayerComponent` offer two distinct options for controlling playback.

- [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) is a versatile system component, appropriate for controlling both playback and timing of a media asset.
- [`AVSampleBufferVideoRenderer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferVideoRenderer) enables greater customization — it requires that you programmatically enqueue individual video-sample buffers for rendering. You can also use an `AVSampleBufferAudioRenderer` instance with a [`AVSampleBufferRenderSynchronizer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferRenderSynchronizer), which affords I/O control, supports preprocessing of media data, and accommodates DRM models not supported by `AVPlayer`. An `AVSampleBufferRenderSynchronizer` can optionally synchronize audio with an [`AVSampleBufferAudioRenderer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferAudioRenderer).

This sample app uses an `AVSampleBufferVideoRenderer` and a `VideoPlayerComponent` to render stereoscopic video in the . Its content is a  video, which places the left- and right-eye images next to each other as part of a single video frame. Because the duration of the video is brief, a looping mechanism supports continuous playback.

![A screenshot of a visionOS window displaying a video of a hummingbird flying in front of flowers.](https://docs-assets.developer.apple.com/published/ba6819ffde514eccc6e9ddb3470a547b/render-stereoscopic-video-with-realitykit-1%402x.png)

> **Note**: By default, 3D video in visionOS uses the Multiview High Efficiency Video Encoding (MV-HEVC) format, supported by MPEG4 and QuickTime. For information about converting a file like the one in this sample to MV-HEVC, see [`Converting side-by-side 3D video to multiview HEVC and spatial video`](https://developer.apple.com/documentation/AVFoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video).

#### Structure the App

The structure of the app is simple. `PlayerModel` is an [`Observable`](https://developer.apple.com/documentation/Observation/Observable) custom type that’s injected into the SwiftUI [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment) for visibility to the root `ContentView`. This model includes a property of type `PlayerState`, which is a Swift enumeration that reflects the current player state. It also includes an instance of type `LoopingVideoPlayer`, which exposes the underlying `AVSampleBufferVideoRenderer`.

```swift
/// The main app structure.
@main
struct RealityKitPlaybackApp: App {
    /// An object that controls the video playback behavior.
    @State private var player = PlayerModel()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(player)
                .frame(width: 1600, height: 900)
        }
        // Expressly constrain window size to that of its content.
        .windowResizability(.contentSize)
        // Disable background glass.
        .windowStyle(.plain)
    }
}
```

For simplicity, the following modifiers are applied to create a window with fixed size, 16x9 aspect ratio, and absent background glass:

- [`frame(width:height:alignment:)`](https://developer.apple.com/documentation/SwiftUI/View/frame(width:height:alignment:))
- [`windowResizability(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowResizability(_:))
- [`windowStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/windowStyle(_:))

#### Create an Entity to Render Video Content

Use the `PlayerModel` as a property exposed from `ContentView`:

```swift
/// A reference to the player.
@Environment(PlayerModel.self) private var player
```

`ContentView` also defines an [`Entity`](entity.md) to house the [`RealityView`](realityview.md) at the root of this scene:

```swift
/// The root entity of the scene.
private let entity = Entity()
```

In the `RealityView` `make` closure, the app instantiates a `VideoPlayerComponent`, passing the player’s video renderer. It then adds the video player to the root entity. The sample uses `scaleFactor`, a type property set to `0.5`, to scale the root entity to half its default size.

```swift
RealityView { content in
    // Initialize the video player with the supplied renderer.
    let videoPlayerComponent = VideoPlayerComponent(videoRenderer: player.videoRenderer)
    entity.components.set(videoPlayerComponent)

    // Scale the root entity and add it to the view.
    entity.scale = SIMD3<Float>(repeating: Self.scaleFactor)
    content.add(entity)
}
// Set the frame to 0 so that the RealityView's origin exists on the same plane as the window.
.frame(depth: 0)
```

Finally, the sample applies these modifiers to initialize the player, and to begin and end playback:

- [`onChange(of:initial:_:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:initial:_:)-8wgw9)
- [`task(priority:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(priority:_:))

```swift
// Begin playback when ready.
.onChange(of: player.isReadyToPlay) { _, ready in
    if ready {
        player.play()
    }
}
// Monitor the scene phase and stop playback when entering the background.
.onChange(of: scenePhase) { _, scenePhase in
    if scenePhase == .background {
        player.stop()
    }
}
// Start loading the player.
.task {
    await player.load()
}
```

#### Prepare for Continuous Playback

`LoopingVideoPlayer` is a custom type that coordinates continuous playback of the sample video. To achieve this, it manages multiple instances of another custom type, `SerialProcessor`.

The player has two key properties: a video renderer and a synchronizer to control the rendering timeline:

```swift
/// The synchronizer that controls the underlying video renderer.
private let synchronizer = AVSampleBufferRenderSynchronizer()

/// The video renderer that enqueues individual frames for playback.
let videoRenderer = AVSampleBufferVideoRenderer()
```

When the system creates the player, it adds the renderer to the synchronizer, and initializes an [`AVURLAsset`](https://developer.apple.com/documentation/AVFoundation/AVURLAsset) with a URL to the underlying video:

```swift
/// Initializes a player with the specified asset URL.
/// - Parameter assetURL: A URL for the asset that the app plays.
init(assetURL: URL) {
    synchronizer.addRenderer(videoRenderer)
    asset = AVURLAsset(url: assetURL)
}
```

To prepare for playback, the processor loads the asset duration asynchronously with [`AVAsynchronousKeyValueLoading`](https://developer.apple.com/documentation/AVFoundation/AVAsynchronousKeyValueLoading). The sample uses duration to trigger looping at the end of each playback cycle with [`addBoundaryTimeObserver(forTimes:queue:using:)`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferRenderSynchronizer/addBoundaryTimeObserver(forTimes:queue:using:)). The sample initializes the first serial processor with the video renderer and asset:

```swift
/// Begin loading the player.
func load() async throws {
    // Determine the duration of the underlying video asset.
    let duration = try await asset.load(.duration)

    // Use the asset duration as the boundary period with which to loop.
    synchronizer.addBoundaryTimeObserver(forTimes: [NSValue(time: duration)], queue: nil) {
        Task { @MainActor [weak self] in
            guard let self else { return }
            self.loop(rate: self.synchronizer.rate)
        }
    }

    // Prepare the processor that the app uses for the initial playback loop.
    enqueueProcessor()
}
```

#### Loop Playback

The app begins playback by calling `loop(rate:)` for the first time. The initial rate of the render synchronizer is `0.0`, meaning that playback has stopped. Passing `1.0` starts playback at the natural rate of the media.

```swift
/// Begin playback by starting the loop.
func play() {
    isLooping = true
    loop(rate: 1)
}
```

The app starts the loop by dequeueing a serial processor instance. It specifies the time and rate of the render synchronizer with [`setRate(_:time:)`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferRenderSynchronizer/setRate(_:time:)). It then enqueues the next serial processor instance and increments the loop count:

```swift
/// Executes a logical playback loop.
/// - Parameter rate: The rate with which to playback content.
private func loop(rate: Float) {
    guard isLooping, let nextProcessor else {
        return
    }

    let currentProcessor = nextProcessor
    process(with: currentProcessor)
    synchronizer.setRate(rate, time: .zero)

    enqueueProcessor()
    loopCount += 1
}
```

The boundary time observer initiates subsequent loops. Playback continues until someone closes the scene. At that time, the sample calls `stop()` to dispose of the player’s resources:

```swift
/// End playback by stopping the loop and resetting relevant state.
func stop() {
    nextProcessor = nil
    isLooping = false
    loopCount = 0
    synchronizer.rate = 0
    videoRenderer.stopRequestingMediaData()
}
```

#### Load the Side By Side Video

Each `SerialProcessor` traverses the video track from start to finish, extracting each individual video frame for processing. Processing converts these input frames from the single-layer, side-by-side input format to a multi-layer, output format.

With side-by-side input, the sample places left- and right-eye images next to each other as part of a single frame. The sample splits the frame into separate images, copies them to distinct left- and right-eye layers, and writes them as a multi-layer frame.

The processor begins when the sample calls [`loadTracks(withMediaCharacteristic:completionHandler:)`](https://developer.apple.com/documentation/AVFoundation/AVAsset/loadTracks(withMediaCharacteristic:completionHandler:)) to load video tracks, and then selects the first available track as the side-by-side input.

```swift
// Load the asset.
guard let videoTrack = try await asset.loadTracks(withMediaCharacteristic: .visual).first else {
    fatalError("Error loading side-by-side video input")
}
```

The processor also loads the natural size of the side-by-side video for later use:

```swift
// Determine the size of the video track, which reflects frame packing.
let videoFrameSize = try await videoTrack.load(.naturalSize)
```

The processor specifies [`IOSurface`](https://developer.apple.com/documentation/IOSurface) settings in its `readerSettings` dictionary. Because the sample manages its own pixel buffer allocations, it uses an empty array as the value corresponding to the [`kCVPixelBufferIOSurfacePropertiesKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferIOSurfacePropertiesKey) key. These settings create an [`AVAssetReaderTrackOutput`](https://developer.apple.com/documentation/AVFoundation/AVAssetReaderTrackOutput). To finish loading the video, the sample obtains an output provider from the [`AVAssetReader`](https://developer.apple.com/documentation/AVFoundation/AVAssetReader), and starts reading.

```swift
// Setup the asset reader.
let readerSettings: [String: Any] = [
    kCVPixelBufferIOSurfacePropertiesKey as String: [String: String]()
]
let videoTrackOutput = AVAssetReaderTrackOutput(track: videoTrack, outputSettings: readerSettings)
let assetReader = try AVAssetReader(asset: asset)
let videoTrackOutputProvider = assetReader.outputProvider(for: videoTrackOutput)
try assetReader.start()
```

#### Create the Video Frame Transfer Session and Output Pixel Buffer Pool

To prepare for processing the video input, the sample creates a [`VTPixelTransferSession`](https://developer.apple.com/documentation/VideoToolbox/VTPixelTransferSession) to read raw [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) input and write processed `CVPixelBuffers` as output.

```swift
// Setup the pixel transfer session.
var transferSession: VTPixelTransferSession?
let sessionResult = VTPixelTransferSessionCreate(
    allocator: kCFAllocatorDefault,
    pixelTransferSessionOut: &transferSession
)
guard sessionResult == kCVReturnSuccess, let transferSession else {
    fatalError("Failed to create pixel transfer session: \(sessionResult)")
}
VTSessionSetProperty(transferSession, key: kVTPixelTransferPropertyKey_ScalingMode, value: kVTScalingMode_CropSourceToCleanAperture)
```

For efficiency, the sample creates a [`CVMutablePixelBuffer.Pool`](https://developer.apple.com/documentation/CoreVideo/CVMutablePixelBuffer/Pool) to allocate pixel buffers for the processed multi-layer output. It creates a pool with attributes that include the pixel format type and size of the eye frame. The sample derives the eye frame size from the natural video size, previously loaded. It then merges these specified attributes with [`recommendedPixelBufferAttributes`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferVideoRenderer/recommendedPixelBufferAttributes-6zrqb).

```swift
// Setup the pixel buffer pool.
let eyeFrameSize = CVImageSize(
    width: Int(videoFrameSize.width / stereoMetadata.horizontalScale),
    height: Int(videoFrameSize.height / stereoMetadata.verticalScale)
)
let defaultAttributes = CVPixelBufferCreationAttributes(
    pixelFormatType: CVPixelFormatType(rawValue: kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange),
    size: eyeFrameSize
)
let recommendedAttributes = videoRenderer.recommendedPixelBufferAttributes
guard let mergedAttributes = CVPixelBufferAttributes(merging: [CVPixelBufferAttributes(defaultAttributes), recommendedAttributes]),
      let creationAttributes = CVPixelBufferCreationAttributes(mergedAttributes),
      let pixelBufferPool = try? CVMutablePixelBuffer.Pool(pixelBufferAttributes: creationAttributes)
else {
    fatalError("Failed to create pixel buffer pool")
}
```

#### Process Input As It Becomes Available

To begin processing, the processor waits for the video renderer to indicate that it is ready to begin rendering. The private `untilReadyForMoreMediaData()` function achieves this with a call to [`requestMediaDataWhenReady(on:using:)`](https://developer.apple.com/documentation/AVFoundation/AVQueuedSampleBufferRendering/requestMediaDataWhenReady(on:using:)). As the sample reads the asset, the `videoTrackOutputProvider` supplies a stream of sample buffers for processing. As the sample receives these sample buffers, the processor calls `transform(from:with:in:)` to convert the side-by-side frame input into stereo-encoded output. The sample then enqueues the stereo-encoded frames to the video renderer. Processing concludes once the stream of sample buffers is exhausted.

```swift
Task {
    // Prepare the renderer for processing.
    await untilReadyForMoreMediaData()
    isProcessing = true

    // Process all read frames from the input video track.
    while videoRenderer.isReadyForMoreMediaData && isProcessing {
        while let sampleBuffer = try await videoTrackOutputProvider.next() {
            if let transformedBuffer = try transform(from: sampleBuffer, with: pixelBufferPool, in: transferSession) {
                videoRenderer.enqueue(transformedBuffer)
            }
        }

        // Indicate that processing is substantially complete.
        isProcessing = false
    }

    // Conclude processing.
    assetReader.cancelReading()
    VTPixelTransferSessionInvalidate(transferSession)
}
```

#### Transform Side By Side Input to Multi Layer Output

The processor creates individual left- and right-eye images in the transformation function. It specifies layer ID `0` for the left eye, and `1` for the right eye.

```None
let layerIDs = [0, 1]
let eyeComponents: [CMStereoViewComponents] = [.leftEye, .rightEye]
var taggedBuffers = [CMTaggedDynamicBuffer]()
for (layerID, eye) in zip(layerIDs, eyeComponents) {
    // ...
```

The function uses the `VTPixelTransferSession` to copy pixels from the side-by-side source pixel buffer, crop to the frame for the current eye, and place them into the destination pixel buffer.

```swift
// Crop the transfer region to the current eye.
let bufferSize = pixelBufferPool.pixelBufferAttributes.size
let apertureOffset = stereoMetadata.apertureOffset(for: bufferSize, layerID: layerID)
let cropRectDict = [
    kCVImageBufferCleanApertureHorizontalOffsetKey: apertureOffset.horizontal,
    kCVImageBufferCleanApertureVerticalOffsetKey: apertureOffset.vertical,
    kCVImageBufferCleanApertureWidthKey: bufferSize.width,
    kCVImageBufferCleanApertureHeightKey: bufferSize.height
]
CVBufferSetAttachment(sourceImageBuffer, kCVImageBufferCleanApertureKey, cropRectDict as CFDictionary, .shouldPropagate)
VTSessionSetProperty(transferSession, key: kVTPixelTransferPropertyKey_ScalingMode, value: kVTScalingMode_CropSourceToCleanAperture)

// Transfer the image to the pixel buffer.
pixelBuffer.withUnsafeBuffer { cvPixelBuffer in
    let transferResult = VTPixelTransferSessionTransferImage(transferSession, from: sourceImageBuffer, to: cvPixelBuffer)
    guard transferResult == kCVReturnSuccess else {
        fatalError("Error during pixel transfer session for layer \(layerID): \(transferResult)")
    }
}
```

The sample creates the individual left and right pixel buffers, adorns them with [`CMTag`](https://developer.apple.com/documentation/CoreMedia/CMTag-swift.class) metadata, and stores them as [`CMTaggedDynamicBuffer`](https://developer.apple.com/documentation/CoreMedia/CMTaggedDynamicBuffer) pairs.

```swift
// Create and append a tagged buffer for this eye.
let tags: [CMTag] = [.videoLayerID(Int64(layerID)), .stereoView(eye), .mediaType(.video)]
taggedBuffers.append(CMTaggedDynamicBuffer(tags: tags, content: .pixelBuffer(CVReadOnlyPixelBuffer(pixelBuffer))))
```

Finally, the sample combines the tagged buffers with the presentation timestamp and duration of the input sample buffer and creates the final output sample buffer.

```swift
let buffer = CMReadySampleBuffer(
    taggedBuffers: taggedBuffers,
    formatDescription: CMTaggedBufferGroupFormatDescription(taggedBuffers: taggedBuffers),
    presentationTimeStamp: cmSampleBuffer.presentationTimeStamp,
    duration: cmSampleBuffer.duration
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/rendering-stereoscopic-video-with-realitykit)*