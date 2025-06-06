# sampleBufferDelegate

**Framework**: AVFoundation  
**Kind**: property

The capture object’s delegate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)? { get }
```

#### Discussion

The delegate receives sample buffers after they are captured.

You set the delegate using [`setSampleBufferDelegate(_:queue:)`](avcapturevideodataoutput/setsamplebufferdelegate(_:queue:).md).

## See Also

- [func setSampleBufferDelegate((any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](avcapturevideodataoutput/setsamplebufferdelegate(_:queue:).md)
  Sets the sample buffer delegate and the queue for invoking callbacks.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcapturevideodataoutput/samplebuffercallbackqueue.md)
  The queue on which the system invokes delegate callbacks.
- [protocol AVCaptureVideoDataOutputSampleBufferDelegate](avcapturevideodataoutputsamplebufferdelegate.md)
  Methods for receiving sample buffers from, and monitoring the status of, a video data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/samplebufferdelegate)*