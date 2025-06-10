# AVAssetWriterInputPixelBufferAdaptor

**Framework**: AVFoundation  
**Kind**: class

An object that appends video samples to an asset writer input.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetWriterInputPixelBufferAdaptor
```

#### Overview

A pixel buffer adaptor provides a pixel buffer pool that you use to allocate pixel buffers to the output file. Using the provided pool for buffer allocation is typically more efficient than managing your own pool.

## Topics

### Creating an Adaptor
- [init(assetWriterInput: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]?)](avassetwriterinputpixelbufferadaptor/init(assetwriterinput:sourcepixelbufferattributes:).md)
  Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file.
### Appending Pixel Buffers
- [func append(CVPixelBuffer, withPresentationTime: CMTime) -> Bool](avassetwriterinputpixelbufferadaptor/append(_:withpresentationtime:).md)
  Appends a pixel buffer to the adaptor.
### Accessing the Pool
- [var pixelBufferPool: CVPixelBufferPool?](avassetwriterinputpixelbufferadaptor/pixelbufferpool.md)
  A pool of pixel buffers to append to the adaptor’s input.
- [var sourcePixelBufferAttributes: [String : any Sendable]?](avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes.md)
  The attributes of the pixel buffers that the pool contains.
### Inspecting a Pixel Buffer Adaptor
- [var assetWriterInput: AVAssetWriterInput](avassetwriterinputpixelbufferadaptor/assetwriterinput.md)
  The asset writer input to which the adaptor appends pixel buffers.

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
- [class AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md)
  An object that appends tagged buffer groups to an asset writer input.
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor)*