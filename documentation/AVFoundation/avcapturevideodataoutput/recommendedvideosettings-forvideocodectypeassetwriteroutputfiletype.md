# recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:)

**Framework**: AVFoundation  
**Kind**: method

Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func recommendedVideoSettings(forVideoCodecType videoCodecType: AVVideoCodecType, assetWriterOutputFileType outputFileType: AVFileType) -> [String : Any]?
```

#### Return Value

A fully populated dictionary of keys and values that are compatible with [`AVAssetWriter`](avassetwriter.md).

#### Discussion

This dictionary contains keys and values described in [`Video settings`](video-settings.md) and is suitable for use when creating an [`AVAssetWriterInput`](avassetwriterinput.md) with the [`init(mediaType:outputSettings:)`](avassetwriterinput/init(mediatype:outputsettings:).md) initializer.

For QuickTime movie and ISO file types, the recommended video settings produce output comparable to that of [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md).

Note that the dictionary of settings is dependent on the current configuration of the output’s [`AVCaptureSession`](avcapturesession.md) and its inputs. The settings dictionary may change if the session’s configuration changes. As such, configure your session first, then query the recommended video settings.

## Parameters

- `videoCodecType`: The video codec type to write.
- `outputFileType`: The Uniform Type Identifier of the file type to write. See   for supported types.

## See Also

- [var videoSettings: [String : Any]!](avcapturevideodataoutput/videosettings.md)
  A dictionary that contains the compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [var alwaysDiscardsLateVideoFrames: Bool](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md)
  Indicates whether to drop video frames if they arrive late.
- [var automaticallyConfiguresOutputBufferDimensions: Bool](avcapturevideodataoutput/automaticallyconfiguresoutputbufferdimensions.md)
  A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [var deliversPreviewSizedOutputBuffers: Bool](avcapturevideodataoutput/deliverspreviewsizedoutputbuffers.md)
  A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:))*