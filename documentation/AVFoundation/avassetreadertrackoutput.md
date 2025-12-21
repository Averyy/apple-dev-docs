# AVAssetReaderTrackOutput

**Framework**: AVFoundation  
**Kind**: class

An object that reads media data from a single track of an asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReaderTrackOutput
```

#### Overview

Read the media data of an asset track by adding a track output to an asset reader. You can read the media samples in their stored format, or you can convert them to an alternative format.

A track output produces uncompressed output. For audio output settings, this means that [`AVFormatIDKey`](https://developer.apple.com/documentation/AVFAudio/AVFormatIDKey) must be [`kAudioFormatLinearPCM`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioFormatLinearPCM). For video output settings, this means that the dictionary must contain values for uncompressed video output, as defined in `Video Settings`. A track output doesn’t support the [`AVSampleRateConverterAudioQualityKey`](https://developer.apple.com/documentation/AVFAudio/AVSampleRateConverterAudioQualityKey) audio setting key or the following video settings keys: [`AVVideoCleanApertureKey`](avvideocleanaperturekey.md), [`AVVideoPixelAspectRatioKey`](avvideopixelaspectratiokey.md), and [`AVVideoScalingModeKey`](avvideoscalingmodekey.md).

When constructing video output settings, the choice of pixel format affects the performance and quality of the decompression. For optimal performance when decompressing video, the requested pixel format should be one that the decoder supports natively to avoid unnecessary conversions. Below are some recommendations:

- For H.264, use [`kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange) or [`kCVPixelFormatType_420YpCbCr8BiPlanarFullRange`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) when you know the video is full range.
- In iOS, use [`kCVPixelFormatType_420YpCbCr8BiPlanarFullRange`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) for JPEG output.
- In macOS, [`kCVPixelFormatType_422YpCbCr8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_422YpCbCr8) is the preferred pixel format for video and generally provides the best performance when decoding. If you need to work in the RGB domain, use [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) in iOS, and [`kCVPixelFormatType_32ARGB`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32ARGB) in macOS.
- ProRes-encoded media can contain up to 12 bits per channel. For ProRes-encoded sources that you wish to preserve more than 8 bits per channel during decompression, use one of the following pixel formats: [`kCVPixelFormatType_4444AYpCbCr16`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_4444AYpCbCr16), [`kCVPixelFormatType_422YpCbCr16`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_422YpCbCr16), [`kCVPixelFormatType_422YpCbCr10`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_422YpCbCr10), or [`kCVPixelFormatType_64ARGB`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_64ARGB). [`AVAssetReader`](avassetreader.md) doesn’t support scaling with any of these high-bit-depth pixel formats. If you use the above pixel formats, don’t specify [`kCVPixelBufferWidthKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferWidthKey) or [`kCVPixelBufferHeightKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferHeightKey) in the [`outputSettings`](avassetreadertrackoutput/outputsettings.md) dictionary. Only ProRes encoders support these pixel formats.
- ProRes 4444-encoded media can contain a mathematically lossless alpha channel. To preserve the alpha channel during decompression, use a pixel format with an alpha component such as [`kCVPixelFormatType_4444AYpCbCr16`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_4444AYpCbCr16) or [`kCVPixelFormatType_64ARGB`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_64ARGB). To test whether your source contains an alpha channel, check that the track’s format description has a [`kCMFormatDescriptionExtension_Depth`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_Depth) key with a value of `32`.

## Topics

### Creating a track output
- [init(track: AVAssetTrack, outputSettings: [String : Any]?)](avassetreadertrackoutput/init(track:outputsettings:).md)
  Creates an object that reads media data from an asset track.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
### Configuring audio settings
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avassetreadertrackoutput/audiotimepitchalgorithm.md)
  The processing algorithm to use for scaled audio edits.
### Inspecting an output
- [var outputSettings: [String : Any]?](avassetreadertrackoutput/outputsettings.md)
  The output settings for this track output.
- [var track: AVAssetTrack](avassetreadertrackoutput/track.md)
  The track from which the output reads sample buffers.

## Relationships

### Inherits From
- [AVAssetReaderOutput](avassetreaderoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReader](avassetreader.md)
  An object that reads media data from an asset.
- [class AVAssetReaderOutput](avassetreaderoutput.md)
  An abstract class that defines the interface to read media samples from an asset reader.
- [class AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput)*