# AVCaptureVideoDataOutputSampleBufferDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for receiving sample buffers from, and monitoring the status of, a video data output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVCaptureVideoDataOutputSampleBufferDelegate : NSObjectProtocol
```

#### Overview

This protocol defines an interface for delegates of an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) object to receive captured video sample buffers and be notified of late sample buffers that were dropped.

The delegate of an [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) object must adopt the `AVCaptureVideoDataOutputSampleBufferDelegate` protocol. The methods in this protocol are optional.

## Topics

### Managing sample buffer behavior
- [func captureOutput(AVCaptureOutput, didOutput: CMSampleBuffer, from: AVCaptureConnection)](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md)
  Notifies the delegate that a new video frame was written.
- [func captureOutput(AVCaptureOutput, didDrop: CMSampleBuffer, from: AVCaptureConnection)](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:diddrop:from:).md)
  Notifies the delegate that a video frame was discarded.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setSampleBufferDelegate((any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](avcapturevideodataoutput/setsamplebufferdelegate(_:queue:).md)
  Sets the sample buffer delegate and the queue for invoking callbacks.
- [var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?](avcapturevideodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcapturevideodataoutput/samplebuffercallbackqueue.md)
  The queue on which the system invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate)*