# AVCaptureVideoDataOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output that records video and provides access to video frames for processing.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVCaptureVideoDataOutput
```

## Mentions

- [Setting up a capture session](setting-up-a-capture-session.md)

#### Overview

Use this output to process compressed or uncompressed frames from the captured video. You can access the frames with the [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) delegate method.

This object supports compressed video data output for macOS only. It can output pixel buffers in several pixel formats. Consider the usability and performance characteristics of these formats and choose the best format for your app.

> ❗ **Important**:  Avoid defaulting to a BGRA format, because BGRA formats aren’t native and require conversion. Additionally, BGRA formats requires significantly more memory than many of the native formats. For more information, see [`TN3121: Selecting a pixel format for an AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/Technotes/tn3121-selecting-a-pixel-format-for-an-avcapturevideodataoutput).

## Topics

### Configuring video capture
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
- [func recommendedVideoSettings(forVideoCodecType: AVVideoCodecType, assetWriterOutputFileType: AVFileType, outputFileURL: URL?) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettings(forvideocodectype:assetwriteroutputfiletype:outputfileurl:).md)
  Returns a dictionary of recommended output settings for writing the specified code, file type, and output URL.
- [func recommendedVideoSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcapturevideodataoutput/recommendedvideosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an AVAssetWriterInput.
### Retrieving supported video types
- [var availableVideoPixelFormatTypes: [OSType]](avcapturevideodataoutput/availablevideopixelformattypes.md)
  The video pixel formats the output supports.
- [var availableVideoCodecTypes: [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypes.md)
  The video codecs that the output supports.
- [func availableVideoCodecTypesForAssetWriter(writingTo: AVFileType) -> [AVVideoCodecType]](avcapturevideodataoutput/availablevideocodectypesforassetwriter(writingto:).md)
  The video codecs that the output supports for writing video to the output file.
- [struct AVVideoCodecType](avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.
### Receiving captured video data
- [func setSampleBufferDelegate((any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](avcapturevideodataoutput/setsamplebufferdelegate(_:queue:).md)
  Sets the sample buffer delegate and the queue for invoking callbacks.
- [var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?](avcapturevideodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcapturevideodataoutput/samplebuffercallbackqueue.md)
  The queue on which the system invokes delegate callbacks.
- [protocol AVCaptureVideoDataOutputSampleBufferDelegate](avcapturevideodataoutputsamplebufferdelegate.md)
  Methods for receiving sample buffers from, and monitoring the status of, a video data output.
### Creating video capture output
- [init()](avcapturevideodataoutput/init.md)
  Creates a new video file output.

## Relationships

### Inherits From
- [AVCaptureOutput](avcaptureoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md)
  Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [class AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md)
  A capture output that records audio and provides access to audio sample buffers as they are recorded.
- [class AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md)
  An interface for generating a spatial audio timed metadata sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput)*