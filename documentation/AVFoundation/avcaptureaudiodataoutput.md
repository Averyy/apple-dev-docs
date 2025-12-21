# AVCaptureAudioDataOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output that records audio and provides access to audio sample buffers as they are recorded.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureAudioDataOutput
```

## Topics

### Creating an audio capture output
- [init()](avcaptureaudiodataoutput/init.md)
  Creates an instance of audio data output.
### Configuring audio capture
- [var audioSettings: [String : Any]!](avcaptureaudiodataoutput/audiosettings.md)
  The settings used to decode or re-encode audio before it’s output.
- [func recommendedAudioSettingsForAssetWriter(writingTo: AVFileType) -> [String : Any]?](avcaptureaudiodataoutput/recommendedaudiosettingsforassetwriter(writingto:).md)
  Specifies the recommended settings for use with an `AVAssetWriterInput`.
- [var spatialAudioChannelLayoutTag: AudioChannelLayoutTag](avcaptureaudiodataoutput/spatialaudiochannellayouttag.md)
  The audio channel layout tag of the audio sample buffers produced by the audio data output.
### Receiving captured audio data
- [func setSampleBufferDelegate((any AVCaptureAudioDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](avcaptureaudiodataoutput/setsamplebufferdelegate(_:queue:).md)
  Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [var sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)?](avcaptureaudiodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcaptureaudiodataoutput/samplebuffercallbackqueue.md)
  The queue on which delegate callbacks are invoked
- [protocol AVCaptureAudioDataOutputSampleBufferDelegate](avcaptureaudiodataoutputsamplebufferdelegate.md)
  Methods for receiving audio sample data from an audio capture.

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
- [class AVCaptureVideoDataOutput](avcapturevideodataoutput.md)
  A capture output that records video and provides access to video frames for processing.
- [class AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md)
  An interface for generating a spatial audio timed metadata sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput)*