# setSampleBufferDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
func setSampleBufferDelegate(_ sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)?, queue sampleBufferCallbackQueue: dispatch_queue_t?)
```

#### Discussion

When a new audio sample buffer is captured it is vended to the sample buffer delegate using the [`captureOutput(_:didOutput:from:)`](avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md) delegate method. All delegate methods are called on the specified dispatch queue.

If the queue is blocked when new samples are captured, those samples will be automatically dropped when they become sufficiently late. This allows you to process existing samples on the same queue without having to manage the potential memory usage increases that would otherwise occur when that processing is unable to keep up with the rate of incoming samples.

If you need to minimize the chances of samples being dropped, you should specify a queue on which a sufficiently small amount of processing is being done outside of receiving sample buffers. When migrating extra processing to another queue, you are responsible for ensuring that memory usage does not grow without bound from samples that have not been processed.

##### Special Considerations

This method uses [`dispatch_retain`](https://developer.apple.com/documentation/Dispatch/dispatch_retain) and [`dispatch_release`](https://developer.apple.com/documentation/Dispatch/dispatch_release) to manage the queue.

## Parameters

- `sampleBufferDelegate`: An object conforming to the   protocol that will receive sample buffers after they are captured.
- `sampleBufferCallbackQueue`: The value may not be  , except when setting the   to  .

## See Also

- [var sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)?](avcaptureaudiodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcaptureaudiodataoutput/samplebuffercallbackqueue.md)
  The queue on which delegate callbacks are invoked
- [protocol AVCaptureAudioDataOutputSampleBufferDelegate](avcaptureaudiodataoutputsamplebufferdelegate.md)
  Methods for receiving audio sample data from an audio capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/setsamplebufferdelegate(_:queue:))*