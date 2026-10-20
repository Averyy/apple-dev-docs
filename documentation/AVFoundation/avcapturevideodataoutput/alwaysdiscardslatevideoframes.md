# alwaysDiscardsLateVideoFrames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether to drop video frames if they arrive late.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var alwaysDiscardsLateVideoFrames: Bool { get set }
```

```objc
@property (nonatomic) BOOL alwaysDiscardsLateVideoFrames;
```

#### Discussion

If this property is [`true`](../../Swift/true.md), the output immediately discard frames that captured while the dispatch queue handling existing frames blocks in the [`captureOutput(_:didOutput:from:)`](../avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_,didoutput,from%29.md) delegate method. When set to [`false`](../../Swift/false.md), the output gives delegates more time to process old frames before it discards new frames, but application memory usage may increase significantly as a result.

The default is [`true`](../../Swift/true.md).

## See Also

### Configuring video capture
- [var videoSettings: [String : Any]!](./videosettings.md)
  A dictionary that contains the compression settings for the output.
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.
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
- [func recommendedMovieMetadata(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [AVMetadataItem]?](./recommendedmoviemetadata%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype,outputfileurl%29.md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedvideosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/alwaysdiscardslatevideoframes)*