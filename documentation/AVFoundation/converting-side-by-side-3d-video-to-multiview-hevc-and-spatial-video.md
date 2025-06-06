# Converting side-by-side 3D video to multiview HEVC and spatial video

**Framework**: AVFoundation

Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.

**Availability**:
- macOS 15.0+
- Xcode 16.0+

#### Overview

In visionOS, 3D video uses the  (MV-HEVC) format, supported by MPEG4 and QuickTime. Unlike other 3D media, MV-HEVC stores a single track containing multiple layers for the video, where the track and layers share a frame size. This track frame size is different from other 3D video types, such as . Side-by-side videos use a single track, and place the left- and right-eye images next to each other as part of a single video frame.

To convert side-by-side video to MV-HEVC, you load the source video, extract each frame, and then split the frame horizontally. Then copy the left and right sides of the split frame into the left- and right-eye layers, writing a frame containing both layers to the output.

This sample app demonstrates the process for converting side-by-side video files to MV-HEVC, encoding the output as a QuickTime file. The output is placed in the same directory as the input file, with `_MVHEVC` appended to the original filename.

For videos you capture with a consistent camera configuration, you can optionally add spatial metadata to the output file.  describes properties of the left- and right-eye cameras that captured the stereo scene.

Adding spatial metadata to a stereo MV-HEVC video prompts Apple platforms to consider the video as  instead of just stereo, and opts the video into visual treatments on Apple Vision Pro that can minimize common causes of stereo viewing discomfort.

To learn more about when to provide spatial metadata for a stereo MV-HEVC video and the metadata values to provide, see [`Creating spatial photos and videos with spatial metadata`](https://developer.apple.com/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata).

You can verify this sample’s MV-HEVC output by opening it with the sample project from [`Reading multiview 3D video files`](reading-multiview-3d-video-files.md).

For the full details of the MV-HEVC format, see [`Apple HEVC Stereo Video - Interoperability Profile (PDF)`](https://developer.apple.comhttps://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) and [`ISO Base Media File Format and Apple HEVC Stereo Video (PDF)`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf).

##### Configure the Sample Code Project

The app takes a path to a side-by-side stereo input video file as a single command-line argument. To run the app in Xcode, select Product > Scheme > Edit Scheme (Command-<), and add the path to your file to Arguments Passed On Launch.

To also add spatial metadata to the file, add four additional arguments to Arguments Passed On Launch:

- `--spatial` (or `-s`) to indicate that you want to include spatial metadata
- `--baseline` (or `-b`) to provide a baseline in millimeters (for example, `--baseline 64.0` for a 64mm baseline)
- `--fov` (or `-f`) to provide a horizontal field of view in degrees (for example, `--fov 80.0` for an 80-degree field of view)
- `--disparityAdjustment` (or `-d`) to provide a disparity adjustment (for example, `--disparityAdjustment 0.02` for a 2% positive disparity shift)

By default, the project’s scheme loads a side-by-side video from the Xcode project folder named `Hummingbird.mov`. This video is a sequence of renders of a 3D scene, showing an animated hummingbird model. By default, the app converts this example video to a stereo MV-HEVC file, without spatial metadata.

To add spatial metadata to the hummingbird video during conversion, choose Product > Scheme > Edit Scheme (Command-<), and select the checkbox to the left of the second row of arguments in the Arguments Passed On Launch field. This enables the following additional arguments: `--spatial --baseline 64.0 --fov 80.0 --disparityAdjustment 0.02`.

The `--spatial` argument tells the app to write spatial metadata to the output video. The virtual cameras used to create these renders were positioned 64mm apart with a horizontal field of view of 80 degrees, and so the value for the `--baseline` argument is `64.0`, and the value of the `--fov` argument is `80.0`.

For this video, a disparity adjustment of +2% of the image width produces a comfortable depth effect when the spatial video is presented in a window on Apple Vision Pro. This 2% disparity adjustment value positions the nearest object in the spatial video — the hummingbird — just behind the front of the window, while still keeping an effective illusion of depth between the hummingbird and the background. The scheme’s arguments express the +2% disparity adjustment with a `--disparityAdjustment` value of `0.02`.

##### Load the Side By Side Video

The app starts by loading the side-by-side video, creating an [`AVAssetReader`](avassetreader.md). The app calls [`loadTracks(withMediaCharacteristic:completionHandler:)`](avasset/loadtracks(withmediacharacteristic:completionhandler:).md) to load video tracks, and then selects the first track available as the side-by-side input.

```swift
let asset = AVURLAsset(url: url)
reader = try AVAssetReader(asset: asset)

// Get the side-by-side video track.
guard let videoTrack = try await asset.loadTracks(withMediaCharacteristic: .visual).first else {
    fatalError("Error loading side-by-side video input")
}
```

The app also stores the frame size for the side-by-side video, and calculates the size of the output frames.

```swift
sideBySideFrameSize = try await videoTrack.load(.naturalSize)
eyeFrameSize = CGSize(width: sideBySideFrameSize.width / 2, height: sideBySideFrameSize.height)
```

To finish loading the video, the app creates an [`AVAssetReaderTrackOutput`](avassetreadertrackoutput.md) and then adds this output stream to the `AVAssetReader`.

```swift
let readerSettings: [String: Any] = [
    kCVPixelBufferIOSurfacePropertiesKey as String: [String: String]()
]
sideBySideTrack = AVAssetReaderTrackOutput(track: videoTrack, outputSettings: readerSettings)

if reader.canAdd(sideBySideTrack) {
    reader.add(sideBySideTrack)
}

if !reader.startReading() {
    fatalError(reader.error?.localizedDescription ?? "Unknown error during track read start")
}
```

When creating the reader track output, the app specifies the file’s pixel format and [`IOSurface`](https://developer.apple.com/documentation/IOSurface) settings in the `readerSettings` dictionary. The app indicates that output goes to a 32-bit ARGB pixel buffer, using [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) with a value of [`kCVPixelFormatType_32ARGB`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32ARGB). The sample app also manages its own pixel buffer allocations, passing an empty array as the value for [`kCVPixelBufferIOSurfacePropertiesKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferIOSurfacePropertiesKey).

##### Configure the Output Mv Hevc File

With the reader initialized, the app calls the `async` method `transcodeToMVHEVC(output:spatialMetadata:)` to generate the output file. First, the app creates a new [`AVAssetWriter`](avassetwriter.md) pointing to the video output location, and then configures the necessary information on the output to indicate that the file contains MV-HEVC video.

```swift
var multiviewCompressionProperties: [CFString: Any] = [
    kVTCompressionPropertyKey_MVHEVCVideoLayerIDs: MVHEVCVideoLayerIDs,
    kVTCompressionPropertyKey_MVHEVCViewIDs: MVHEVCViewIDs,
    kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs: MVHEVCLeftAndRightViewIDs,
    kVTCompressionPropertyKey_HasLeftStereoEyeView: true,
    kVTCompressionPropertyKey_HasRightStereoEyeView: true
]
```

[`kVTCompressionPropertyKey_HasLeftStereoEyeView`](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_HasLeftStereoEyeView) and [`kVTCompressionPropertyKey_HasRightStereoEyeView`](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_HasRightStereoEyeView) are `true`, because the output contains a layer for each eye. [`kVTCompressionPropertyKey_MVHEVCVideoLayerIDs`](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_MVHEVCVideoLayerIDs), [`kVTCompressionPropertyKey_MVHEVCViewIDs`](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_MVHEVCViewIDs), and [`kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs`](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs) define the layer and view IDs to use for multiview HEVC encoding. In the sample app, these are all the same.

The sample app uses `0` for the left eye layer/view ID and `1` for the right eye layer/view ID.

```swift
let MVHEVCVideoLayerIDs = [0, 1]

// For simplicity, choose view IDs that match the layer IDs.
let MVHEVCViewIDs = [0, 1]

// The first element in this array is the view ID of the left eye.
let MVHEVCLeftAndRightViewIDs = [0, 1]
```

##### Include Spatial Metadata

If the person calling this command-line app requested to add spatial metadata to the output file, and provided the necessary spatial metadata, the app converts that metadata to expected units and scales, and adds an additional compression property key for each metadata value. The app also specifies that the input uses a rectilinear projection, to indicate that it has the expected projection for spatial video.

```swift
if let spatialMetadata {

    let baselineInMicrometers = UInt32(1000.0 * spatialMetadata.baselineInMillimeters)
    let encodedHorizontalFOV = UInt32(1000.0 * spatialMetadata.horizontalFOV)
    let encodedDisparityAdjustment = Int32(10_000.0 * spatialMetadata.disparityAdjustment)

    multiviewCompressionProperties[kVTCompressionPropertyKey_ProjectionKind] = kCMFormatDescriptionProjectionKind_Rectilinear
    multiviewCompressionProperties[kVTCompressionPropertyKey_StereoCameraBaseline] = baselineInMicrometers
    multiviewCompressionProperties[kVTCompressionPropertyKey_HorizontalFieldOfView] = encodedHorizontalFOV
    multiviewCompressionProperties[kVTCompressionPropertyKey_HorizontalDisparityAdjustment] = encodedDisparityAdjustment

}
```

##### Configure the Mv Hevc Input Source

The app transcodes video by directly copying pixels from the source frame. Writing track data to a video file requires an [`AVAssetWriterInput`](avassetwriterinput.md). The sample app uses an [`AVAssetWriterInputTaggedPixelBufferGroupAdaptor`](avassetwriterinputtaggedpixelbuffergroupadaptor.md) to provide pixel data from the source, writing to the output.

```swift
let multiviewSettings: [String: Any] = [
    AVVideoCodecKey: AVVideoCodecType.hevc,
    AVVideoWidthKey: self.eyeFrameSize.width,
    AVVideoHeightKey: self.eyeFrameSize.height,
    AVVideoCompressionPropertiesKey: multiviewCompressionProperties
]

guard multiviewWriter.canApply(outputSettings: multiviewSettings, forMediaType: AVMediaType.video) else {
    fatalError("Error applying output settings")
}

let frameInput = AVAssetWriterInput(mediaType: .video, outputSettings: multiviewSettings)

let sourcePixelAttributes: [String: Any] = [
    kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB,
    kCVPixelBufferWidthKey as String: self.sideBySideFrameSize.width,
    kCVPixelBufferHeightKey as String: self.sideBySideFrameSize.height
]

let bufferInputAdapter = AVAssetWriterInputTaggedPixelBufferGroupAdaptor(assetWriterInput: frameInput, sourcePixelBufferAttributes: sourcePixelAttributes)
```

The `AVAssetWriterInput` source uses the same `outputSettings` as `videoWriter`, and the created pixel buffer adapter has the same frame size as the source. The app follows the best practice of calling [`canAdd(_:)`](avassetwriter/canadd(_:)-6al7j.md) to check the input adapter compatibility before calling [`add(_:)`](avassetwriter/add(_:)-4c4d0.md) to use it as a source.

```swift
guard multiviewWriter.canAdd(frameInput) else {
    fatalError("Error adding side-by-side video frames as input")
}
multiviewWriter.add(frameInput)
```

##### Process Input As It Becomes Available

The app calls [`startWriting()`](avassetwriter/startwriting().md) and [`startSession(atSourceTime:)`](avassetwriter/startsession(atsourcetime:).md) in sequence to start the video writing process, and then iterates over available frame inputs with [`requestMediaDataWhenReady(on:using:)`](avassetwriterinput/requestmediadatawhenready(on:using:).md).

```swift
guard multiviewWriter.startWriting() else {
    fatalError("Failed to start writing multiview output file")
}
multiviewWriter.startSession(atSourceTime: CMTime.zero)

// The dispatch queue executes the closure when media reads from the input file are available.
frameInput.requestMediaDataWhenReady(on: DispatchQueue(label: "Multiview HEVC Writer")) {
```

The closure argument of `requestMediaDataWhenReady(on:using:)` runs on the provided [`DispatchQueue`](https://developer.apple.com/documentation/Dispatch/DispatchQueue) when the first data read is available. The closure itself is responsible for managing resources that process the media data, and running a loop to process data efficiently.

##### Create the Video Frame Transfer Session and Output Pixel Buffer Pool

To perform the data transfer from the source track, the pixel input adapter requires a pixel buffer as a source. The app creates a [`VTPixelTransferSession`](https://developer.apple.com/documentation/VideoToolbox/VTPixelTransferSession) to allow for reading data from the video source, and uses the `AVAssetWriterInputTaggedPixelBufferGroupAdaptor`’s existing pixel buffer pool to allocate pixel buffers for the new multiview eye layers.

```swift
var session: VTPixelTransferSession? = nil
guard VTPixelTransferSessionCreate(allocator: kCFAllocatorDefault, pixelTransferSessionOut: &session) == noErr, let session else {
    fatalError("Failed to create pixel transfer")
}
guard let pixelBufferPool = bufferInputAdapter.pixelBufferPool else {
    fatalError("Failed to retrieve existing pixel buffer pool")
}
```

##### Copy Frame Images From Input to Output

After preparing resources, the app then begins a loop to process frames until there’s no more data, or the input read has stopped to buffer data. The [`isReadyForMoreMediaData`](avassetwriterinput/isreadyformoremediadata.md) property of an input source is `true` if another frame is immediately available to process. When a frame is ready, a [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/CVImageBuffer) instance is created from it.

The app is now ready to handle sampling. If there’s an available sample, the app processes it in the `convertFrame` method, then calls [`appendTaggedBuffers(_:withPresentationTime:)`](avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(_:withpresentationtime:).md), copying the side-by-side sample buffer’s [`outputPresentationTimeStamp`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer/outputPresentationTimeStamp) timestamp to the new multiview timestamp.

```swift
while frameInput.isReadyForMoreMediaData && bufferInputAdapter.assetWriterInput.isReadyForMoreMediaData {
    if let sampleBuffer = self.sideBySideTrack.copyNextSampleBuffer() {
        guard let imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else {
            fatalError("Failed to load source samples as an image buffer")
        }
        let taggedBuffers = self.convertFrame(fromSideBySide: imageBuffer, with: pixelBufferPool, in: session)
        let newPTS = sampleBuffer.outputPresentationTimeStamp
        if !bufferInputAdapter.appendTaggedBuffers(taggedBuffers, withPresentationTime: newPTS) {
            fatalError("Failed to append tagged buffers to multiview output")
        }
```

Input reading finishes when there are no more sample buffers to process from the input stream. The app calls [`markAsFinished()`](avassetwriterinput/markasfinished().md) to close the stream, and [`finishWriting(completionHandler:)`](avassetwriter/finishwriting(completionhandler:).md) to complete the multiview video write. The app also calls [`resume()`](https://developer.apple.com/documentation/Swift/CheckedContinuation/resume()) on its associated [`CheckedContinuation`](https://developer.apple.com/documentation/Swift/CheckedContinuation), to return to the `await` call, then breaks from the processing loop.

```swift
frameInput.markAsFinished()
multiviewWriter.finishWriting {
    continuation.resume()
}

break
```

##### Convert Side By Side Inputs Into Video Layer Outputs

In the `convertFrame` method, the app processes the left- and right-eye images for the frame by `layerID`, using `0` for the left eye and `1` for the right. First, the app creates a pixel buffer from the pool.

```swift
var pixelBuffer: CVPixelBuffer?
CVPixelBufferPoolCreatePixelBuffer(kCFAllocatorDefault, pixelBufferPool, &pixelBuffer)
guard let pixelBuffer else {
    fatalError("Failed to create pixel buffer for layer \(layerID)")
}
```

The method then uses its passed `VTPixelTransferSession` to copy the pixels from the side-by-side source, placing them into the created output sample buffer by cropping the frame to include only one eye’s image.

```swift
// Crop the transfer region to the current eye.
let apertureOffset = -(self.eyeFrameSize.width / 2) + CGFloat(layerID) * self.eyeFrameSize.width
let cropRectDict = [
    kCVImageBufferCleanApertureHorizontalOffsetKey: apertureOffset,
    kCVImageBufferCleanApertureVerticalOffsetKey: 0,
    kCVImageBufferCleanApertureWidthKey: self.eyeFrameSize.width,
    kCVImageBufferCleanApertureHeightKey: self.eyeFrameSize.height
]
CVBufferSetAttachment(imageBuffer, kCVImageBufferCleanApertureKey, cropRectDict as CFDictionary, CVAttachmentMode.shouldPropagate)
VTSessionSetProperty(session, key: kVTPixelTransferPropertyKey_ScalingMode, value: kVTScalingMode_CropSourceToCleanAperture)

// Transfer the image to the pixel buffer.
guard VTPixelTransferSessionTransferImage(session, from: imageBuffer, to: pixelBuffer) == noErr else {
    fatalError("Error during pixel transfer session for layer \(layerID)")
}
```

Setting aperture view properties on [`CVBufferSetAttachment(_:_:_:_:)`](https://developer.apple.com/documentation/CoreVideo/CVBufferSetAttachment(_:_:_:_:)) defines how to capture and crop input images. The aperture here is the size of an eye image, and the center of the capture frame offset with [`kCVImageBufferCleanApertureHorizontalOffsetKey`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferCleanApertureHorizontalOffsetKey) by `-0.5 * width` for the left eye and `+0.5 * width` for the right eye, to capture the correct half of the side-by-side frame.

The app then calls [`VTSessionSetProperty(_:key:value:)`](https://developer.apple.com/documentation/VideoToolbox/VTSessionSetProperty(_:key:value:)) to crop the image to the aperture frame with [`kVTScalingMode_CropSourceToCleanAperture`](https://developer.apple.com/documentation/VideoToolbox/kVTScalingMode_CropSourceToCleanAperture). Next, the app calls [`VTPixelTransferSessionTransferImage(_:from:to:)`](https://developer.apple.com/documentation/VideoToolbox/VTPixelTransferSessionTransferImage(_:from:to:)) to copy source pixels to the destination buffer.

The final step is to create a [`CMTaggedBuffer`](https://developer.apple.com/documentation/CoreMedia/CMTaggedBuffer) for the eye image to return to the calling output writer.

```swift
let tags: [CMTag] = [.videoLayerID(Int64(layerID)), .stereoView(eye)]
let buffer = CMTaggedBuffer(tags: tags, buffer: .pixelBuffer(pixelBuffer))
taggedBuffers.append(buffer)
```

## See Also

- [Writing Fragmented MPEG-4 Files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an App’s Video Color](evaluating-an-app-s-video-color.md)
  Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
- [class AVOutputSettingsAssistant](avoutputsettingsassistant.md)
  An object that builds audio and video output settings dictionaries.
- [class AVAssetWriter](avassetwriter.md)
  An object that writes media data to a container file.
- [class AVAssetWriterInput](avassetwriterinput.md)
  An object that appends media samples to a track in an asset writer’s output file.
- [class AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md)
  An object that appends video samples to an asset writer input.
- [class AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md)
  An object that appends tagged buffer groups to an asset writer input.
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video)*