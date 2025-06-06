# deliversPreviewSizedOutputBuffers

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var deliversPreviewSizedOutputBuffers: Bool { get set }
```

#### Discussion

[`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) produces preview-sized buffers, which are approximately the size of the screen, when its [`automaticallyConfiguresOutputBufferDimensions`](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md) property is [`true`](https://developer.apple.com/documentation/swift/true). If you wish to manually set this property, you must first set [`automaticallyConfiguresOutputBufferDimensions`](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md) to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var videoSettings: [String : Any]!](avcapturevideodataoutput/videosettings.md)
  A dictionary that contains the compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [var alwaysDiscardsLateVideoFrames: Bool](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md)
  Indicates whether to drop video frames if they arrive late.
- [var automaticallyConfiguresOutputBufferDimensions: Bool](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md)
  A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/deliverspreviewsizedoutputbuffers)*