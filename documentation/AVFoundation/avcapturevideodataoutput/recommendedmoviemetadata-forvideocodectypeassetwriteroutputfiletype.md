# recommendedMovieMetadata(forVideoCodecType:assetWriterOutputFileType:)

**Framework**: AVFoundation  
**Kind**: method

Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func recommendedMovieMetadata(forVideoCodecType videoCodecType: AVVideoCodecType, assetWriterOutputFileType outputFileType: AVFileType) -> [AVMetadataItem]?
```

#### Return Value

A fully populated array of [`AVMetadataItem`](avmetadataitem.md) objects compatible with [`AVAssetWriter`](avassetwriter.md).

#### Discussion

The value of this property is an array of [`AVMetadataItem`](avmetadataitem.md) objects representing the collection of top-level metadata to be written in each output file. This array is suitable to use as the [`metadata`](avassetwriter/metadata.md) property before you have called [`startWriting()`](avassetwriter/startwriting().md). For more details see [`startWriting()`](AVAssetWriter/startWriting().md).

The `videoCodecType` string you provide must be present in [`availableVideoCodecTypesForAssetWriter(writingTo:)`](avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:).md) array, or an `NSInvalidArgumentException` is thrown.

For clients writing files using a ProRes Raw codec type, white balance must be locked (call [`setWhiteBalanceModeLocked(with:completionHandler:)`](avcapturedevice/setwhitebalancemodelocked(with:completionhandler:).md)) before querying this property, or an `NSIvalidArgumentException` is thrown.

> **Note**: The array of metadata is dependent on the current configuration of the receiver’s [`AVCaptureSession`](avcapturesession.md) and its inputs. The array may change when the session’s configuration changes. As such, you should configure and start your session first, then query this method.

## Parameters

- `videoCodecType`: The desired   to be used for compression (see  ).
- `outputFileType`: Specifies the UTI of the file type to be written (see  ).

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
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:).md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedmoviemetadata(forvideocodectype:assetwriteroutputfiletype:))*