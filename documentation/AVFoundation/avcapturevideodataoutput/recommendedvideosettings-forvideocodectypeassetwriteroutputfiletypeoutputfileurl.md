# recommendedVideoSettings(forVideoCodecType:assetWriterOutputFileType:outputFileURL:)

**Framework**: AVFoundation  
**Kind**: method

Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func recommendedVideoSettings(forVideoCodecType videoCodecType: AVVideoCodecType, assetWriterOutputFileType outputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?
```

#### Return Value

A fully populated output settings dictionary suitable for configuring an asset writer input.

## Parameters

- `videoCodecType`: The type of video codec to use.
- `outputFileType`: The type of output file to write.
- `outputFileURL`: The URL of the output file to write.

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
- [var preparesCellularRadioForNetworkConnection: Bool](avcapturevideodataoutput/preparescellularradiofornetworkconnection.md)
  Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [var preservesDynamicHDRMetadata: Bool](avcapturevideodataoutput/preservesdynamichdrmetadata.md)
  Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [var recommendedMediaTimeScaleForAssetWriter: CMTimeScale](avcapturevideodataoutput/recommendedmediatimescaleforassetwriter.md)
  Indicates the recommended media timescale for the video track.
- [func recommendedMovieMetadata(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [AVMetadataItem]?](avcapturevideodataoutput/recommendedmoviemetadata(forvideocodectype:assetwriteroutputfiletype:).md)
  Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:))*