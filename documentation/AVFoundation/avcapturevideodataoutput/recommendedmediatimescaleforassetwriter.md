# recommendedMediaTimeScaleForAssetWriter

**Framework**: AVFoundation  
**Kind**: property

Indicates the recommended media timescale for the video track.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var recommendedMediaTimeScaleForAssetWriter: CMTimeScale { get }
```

#### Return Value

The recommended media timescale based on the active capture session’s inputs. It is never less than 600. It may or may not be a multiple of 600.

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
- [func recommendedMovieMetadata(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [AVMetadataItem]?](avcapturevideodataoutput/recommendedmoviemetadata(forvideocodectype:assetwriteroutputfiletype:).md)
  Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedmediatimescaleforassetwriter)*