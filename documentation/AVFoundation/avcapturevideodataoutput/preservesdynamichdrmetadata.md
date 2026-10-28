# preservesDynamicHDRMetadata

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying pixel buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var preservesDynamicHDRMetadata: Bool { get set }
```

```objc
@property BOOL preservesDynamicHDRMetadata;
```

## Discussion

Set this property to `true` if you wish to use [`AVCaptureVideoDataOutput`](../avcapturevideodataoutput.md) with [`AVAssetWriter`](../avassetwriter.md) to record HDR movies. You must also set `kVTCompressionPropertyKey_PreserveDynamicHDRMetadata` to `true` in the compression settings you pass to your [`AVAssetWriterInput`](../avassetwriterinput.md). These compression settings are represented under the [`AVVideoCompressionPropertiesKey`](../avvideocompressionpropertieskey.md) sub-dictionary of your top-level AVVideoSettings (see [Video settings](../video-settings.md)). When you set this key to `true`, performance improves, as the encoder is able to skip HDR metadata calculation for every frame. The default value is `false`.

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
- [var recommendedMediaTimeScaleForAssetWriter: CMTimeScale](./recommendedmediatimescaleforassetwriter.md)
  Indicates the recommended media timescale for the video track.
- [func recommendedMovieMetadata(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [AVMetadataItem]?](./recommendedmoviemetadata%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype,outputfileurl%29.md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedvideosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an AVAssetWriterInput.
- [minFrameDuration](./minframeduration.md)
  The minimum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/preservesdynamichdrmetadata)*