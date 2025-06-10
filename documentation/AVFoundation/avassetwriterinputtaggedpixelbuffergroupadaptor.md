# AVAssetWriterInputTaggedPixelBufferGroupAdaptor

**Framework**: AVFoundation  
**Kind**: class

An object that appends tagged buffer groups to an asset writer input.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetWriterInputTaggedPixelBufferGroupAdaptor
```

#### Overview

This class provides a [`CVPixelBufferPool`](https://developer.apple.com/documentation/CoreVideo/CVPixelBufferPool-77o) to use for allocating the pixel buffers of tagged buffer groups to write to the output file. Using the provided pixel buffer pool for buffer allocation is typically more efficient than appending pixel buffers allocated using a separate pool.

## Topics

### Creating an adaptor
- [init(assetWriterInput: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]?)](avassetwriterinputtaggedpixelbuffergroupadaptor/init(assetwriterinput:sourcepixelbufferattributes:).md)
  Creates an object that appends tagged buffer groups to an asset writer input.
### Configuring the buffer pool
- [var sourcePixelBufferAttributes: [String : any Sendable]?](avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes.md)
  The attributes of buffers that the adaptor’s pixel buffer pool vends.
- [var pixelBufferPool: CVPixelBufferPool?](avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool.md)
  A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups.
### Appending pixel buffers
- [func appendTaggedBuffers([CMTaggedBuffer], withPresentationTime: CMTime) -> Bool](avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(_:withpresentationtime:).md)
  Appends a tagged buffer group to the adaptor.
- [func appendTaggedPixelBufferGroup(__CMTaggedBufferGroup, withPresentationTime: CMTime) -> Bool](avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedpixelbuffergroup(_:withpresentationtime:).md)
  Appends a tagged buffer group to the adaptor.
### Accessing the writer input
- [var assetWriterInput: AVAssetWriterInput](avassetwriterinputtaggedpixelbuffergroupadaptor/assetwriterinput.md)
  The asset writer input to which the adaptor appends tagged buffer groups.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md)
  Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
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
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor)*