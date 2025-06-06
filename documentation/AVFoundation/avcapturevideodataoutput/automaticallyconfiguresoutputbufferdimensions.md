# automaticallyConfiguresOutputBufferDimensions

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the output automatically configures the size of output buffers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var automaticallyConfiguresOutputBufferDimensions: Bool { get set }
```

#### Discussion

In most configurations, [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) delivers full-resolution buffers that match the video dimensions of the capture device’s [`activeFormat`](avcapturedevice/activeformat.md) property. When this property is [`true`](https://developer.apple.com/documentation/swift/true), the output is free to scale the buffers delivered to [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) to a size suitable for preview (approximately the size of the screen).

You can query this property to find out whether the automatic configuration of output buffer dimensions is downscaling buffers to a preview size. You can also query the output’s [`videoSettings`](avcapturevideodataoutput/videosettings.md) dictionary to find the buffer’s exact dimensions.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

> ❗ **Important**:  You must set this property to [`false`](https://developer.apple.com/documentation/swift/false) before you can manually set [`deliversPreviewSizedOutputBuffers`](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md) to [`true`](https://developer.apple.com/documentation/swift/true).

 You must set this property to [`false`](https://developer.apple.com/documentation/swift/false) before you can manually set [`deliversPreviewSizedOutputBuffers`](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md) to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var videoSettings: [String : Any]!](avcapturevideodataoutput/videosettings.md)
  A dictionary that contains the compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [var alwaysDiscardsLateVideoFrames: Bool](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md)
  Indicates whether to drop video frames if they arrive late.
- [var deliversPreviewSizedOutputBuffers: Bool](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md)
  A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions)*