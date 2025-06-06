# videoSettings

**Framework**: AVFoundation  
**Kind**: property

A dictionary that contains the compression settings for the output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var videoSettings: [String : Any]! { get set }
```

#### Discussion

To receive samples in their device-native format, set this value to an empty dictionary:

To receive samples in a default uncompressed format, set this value to `nil`. Then you can query this value to receive a dictionary of the settings the session uses.

In iOS versions prior to iOS 16, the only key supported is [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey). In iOS 16 and later, the supported keys include the following:

- For compressed video output, only use [`AVVideoPixelAspectRatioKey`](avvideopixelaspectratiokey.md), [`AVVideoCleanApertureKey`](avvideocleanaperturekey.md), [`AVVideoScalingModeKey`](avvideoscalingmodekey.md), [`AVVideoColorPropertiesKey`](avvideocolorpropertieskey.md), and [`AVVideoAllowWideColorKey`](avvideoallowwidecolorkey.md).
- For uncompressed video output, you can also use [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey), [`kCVPixelBufferWidthKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferWidthKey), and [`kCVPixelBufferHeightKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferHeightKey), in addition to the compressed video output keys.

You can use [`availableVideoPixelFormatTypes`](avcapturevideodataoutput/availablevideopixelformattypes.md) and [`availableVideoCodecTypes`](avcapturevideodataoutput/availablevideocodectypes.md) to get a list of the supported pixel formats and video codecs, respectively. The width and height need to match the [`videoOrientation`](avcaptureconnection/videoorientation.md) specified in the output’s [`AVCaptureConnection`](avcaptureconnection.md), otherwise the system throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception). The aspect ratio of the width and height also need to match the aspect ratio of the source’s [`activeFormat`](avcapturedevice/activeformat.md), corrected for the connection’s [`videoOrientation`](avcaptureconnection/videoorientation.md), otherwise the system throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception). If the width or height exceeds the source’s `activeFormat`‘s width or height, the system throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception). Don’t change the width and height if [`deliversPreviewSizedOutputBuffers`](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md) is [`true`](https://developer.apple.com/documentation/swift/true), otherwise the system throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception).

## See Also

- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [var alwaysDiscardsLateVideoFrames: Bool](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md)
  Indicates whether to drop video frames if they arrive late.
- [var automaticallyConfiguresOutputBufferDimensions: Bool](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md)
  A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [var deliversPreviewSizedOutputBuffers: Bool](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md)
  A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/videosettings)*