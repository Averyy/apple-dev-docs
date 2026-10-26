# recommendedMovieMetadata(forVideoCodecType:assetWriterOutputFileType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<AVMetadataItem *> *) recommendedMovieMetadataForVideoCodecType:(AVVideoCodecType) videoCodecType assetWriterOutputFileType:(AVFileType) outputFileType;
```

#### Return Value

A fully populated array of [`AVMetadataItem`](../avmetadataitem.md) objects compatible with [`AVAssetWriter`](../avassetwriter.md).

#### Discussion

The value of this property is an array of [`AVMetadataItem`](../avmetadataitem.md) objects representing the collection of top-level metadata to be written in each output file. This array is suitable to use as the [`metadata`](../avassetwriter/metadata.md) property before you have called [`startWriting()`](../avassetwriter/startwriting%28%29.md). For more details see [`startWriting()`](../avassetwriter/startwriting%28%29.md).

The `videoCodecType` string you provide must be present in [`availableVideoCodecTypesForAssetWriter(writingTo:)`](./availablevideocodectypesforassetwriter%28writingto%29.md) array, or an `NSInvalidArgumentException` is thrown.

For clients writing files using a ProRes Raw codec type, white balance must be locked (call [`setWhiteBalanceModeLocked(with:completionHandler:)`](../avcapturedevice/setwhitebalancemodelocked%28with,completionhandler%29.md)) before querying this property, or an `NSIvalidArgumentException` is thrown.

> **Note**: The array of metadata is dependent on the current configuration of the receiver’s [`AVCaptureSession`](../avcapturesession.md) and its inputs. The array may change when the session’s configuration changes. As such, you should configure and start your session first, then query this method.

## Parameters

- `videoCodecType`: The desired [`AVVideoCodecKey`](../avvideocodeckey.md) to be used for compression (see [Video settings](../video-settings.md)).
- `outputFileType`: Specifies the UTI of the file type to be written (see [`AVFileType`](../avfiletype.md)).

## See Also

### Configuring video capture
- [var videoSettings: [String : Any]!](./videosettings.md)
  A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.
- [var alwaysDiscardsLateVideoFrames: Bool](./alwaysdiscardslatevideoframes.md)
  Indicates whether to drop video frames if they arrive late.
- [var automaticallyConfiguresOutputBufferDimensions: Bool](./automaticallyconfiguresoutputbufferdimensions.md)
  A Boolean value that indicates whether the output automatically configures the size of output buffers.
- [var deliversPreviewSizedOutputBuffers: Bool](./deliverspreviewsizedoutputbuffers.md)
  A Boolean value that indicates whether the output is configured to deliver preview-sized buffers.
- [var preparesCellularRadioForNetworkConnection: Bool](./preparescellularradiofornetworkconnection.md)
  Indicates whether the receiver should prepare the cellular radio for imminent network activity.
- [var preservesDynamicHDRMetadata: Bool](./preservesdynamichdrmetadata.md)
  Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.
- [var recommendedMediaTimeScaleForAssetWriter: CMTimeScale](./recommendedmediatimescaleforassetwriter.md)
  Indicates the recommended media timescale for the video track.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype,outputfileurl%29.md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedvideosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an AVAssetWriterInput.
- [minFrameDuration](./minframeduration.md)
  The minimum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedmoviemetadata(forvideocodectype:assetwriteroutputfiletype:))*