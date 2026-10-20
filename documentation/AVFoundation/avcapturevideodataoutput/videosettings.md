# videoSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, null_resettable) NSDictionary<NSString *,id> * videoSettings;
```

#### Discussion

To receive samples in their device-native format, set this value to an empty dictionary:

**Swift**:

```swift
let myVideoOutput = AVCaptureVideoDataOutput()
myVideoOutput.videoSettings = [:] // Receive samples in device format.
```

**Objective-C**:

```objc
AVCaptureVideoDataOutput* myVideoOutput;
myVideoOutput.videoSettings = @{ }; // Receive samples in device format.
```

To receive samples in a default uncompressed format, set this value to `nil`. Then you can query this value to receive a dictionary of the settings the session uses.

In iOS versions prior to iOS 16, the only key supported is [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md). In iOS 16 and later, the supported keys include the following:

- For compressed video output, only use [`AVVideoPixelAspectRatioKey`](../avvideopixelaspectratiokey.md), [`AVVideoCleanApertureKey`](../avvideocleanaperturekey.md), [`AVVideoScalingModeKey`](../avvideoscalingmodekey.md), [`AVVideoColorPropertiesKey`](../avvideocolorpropertieskey.md), and [`AVVideoAllowWideColorKey`](../avvideoallowwidecolorkey.md).
- For uncompressed video output, you can also use [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md), [`kCVPixelBufferWidthKey`](../../CoreVideo/kcvpixelbufferwidthkey.md), and [`kCVPixelBufferHeightKey`](../../CoreVideo/kcvpixelbufferheightkey.md), in addition to the compressed video output keys.

You can use [`availableVideoPixelFormatTypes`](./availablevideopixelformattypes.md) and [`availableVideoCodecTypes`](./availablevideocodectypes.md) to get a list of the supported pixel formats and video codecs, respectively. The width and height need to match the [`videoOrientation`](../avcaptureconnection/videoorientation.md) specified in the output’s [`AVCaptureConnection`](../avcaptureconnection.md), otherwise the system throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md). The aspect ratio of the width and height also need to match the aspect ratio of the source’s [`activeFormat`](../avcapturedevice/activeformat.md), corrected for the connection’s [`videoOrientation`](../avcaptureconnection/videoorientation.md), otherwise the system throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md). If the width or height exceeds the source’s `activeFormat`‘s width or height, the system throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md). Don’t change the width and height if [`deliversPreviewSizedOutputBuffers`](./deliverspreviewsizedoutputbuffers.md) is [`true`](../../Swift/true.md), otherwise the system throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md).

## See Also

### Configuring video capture
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
- [func recommendedMovieMetadata(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [AVMetadataItem]?](./recommendedmoviemetadata%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Recommends movie-level metadata for a particular video codec type and output file type, to be used with an asset writer input.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype%29.md)
  Returns a video settings dictionary appropriate for capturing video to a file with the specified codec and type.
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](./recommendedvideosettings%28forvideocodectype,assetwriteroutputfiletype,outputfileurl%29.md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](./recommendedvideosettingsforassetwriter%28writingto%29.md)
  Specifies the recommended settings for use with an AVAssetWriterInput.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/videosettings)*