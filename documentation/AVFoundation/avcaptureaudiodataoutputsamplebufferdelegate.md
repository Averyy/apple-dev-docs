# AVCaptureAudioDataOutputSampleBufferDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for receiving audio sample data from an audio capture.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
protocol AVCaptureAudioDataOutputSampleBufferDelegate : NSObjectProtocol
```

#### Overview

This protocol defines an interface for delegates of an [`AVCaptureAudioDataOutput`](avcaptureaudiodataoutput.md) object to receive captured audio sample buffers.

The delegate of an [`AVCaptureAudioDataOutput`](avcaptureaudiodataoutput.md) object must adopt this protocol. The method in this protocol is optional.

## Topics

### Managing sample buffer behavior
- [func captureOutput(AVCaptureOutput, didOutput: CMSampleBuffer, from: AVCaptureConnection)](avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md)
  Notifies the delegate that a sample buffer was written.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setSampleBufferDelegate((any AVCaptureAudioDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](avcaptureaudiodataoutput/setsamplebufferdelegate(_:queue:).md)
  Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [var sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)?](avcaptureaudiodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcaptureaudiodataoutput/samplebuffercallbackqueue.md)
  The queue on which delegate callbacks are invoked


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate)*