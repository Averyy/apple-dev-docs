# setSampleBufferDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the sample buffer delegate and the queue for invoking callbacks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setSampleBufferDelegate(_ sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue sampleBufferCallbackQueue: dispatch_queue_t?)
```

#### Discussion

When a new video sample buffer is captured, it is sent to the sample buffer delegate using [`captureOutput(_:didOutput:from:)`](avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:).md). All delegate methods are invoked on the specified dispatch queue.

If the queue is blocked when new frames are captured, those frames will be automatically dropped at a time determined by the value of the [`alwaysDiscardsLateVideoFrames`](avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) property. This allows you to process existing frames on the same queue without having to manage the potential memory usage increases that would otherwise occur when that processing is unable to keep up with the rate of incoming frames.

If your frame processing is consistently unable to keep up with the rate of incoming frames, you should consider using the [`minFrameDuration`](avcapturevideodataoutput/minframeduration.md) property, which will generally yield better performance characteristics and more consistent frame rates than frame dropping alone.

If you need to minimize the chances of frames being dropped, you should specify a queue on which a sufficiently small amount of processing is being done outside of receiving sample buffers. However, if you migrate extra processing to another queue, you are responsible for ensuring that memory usage does not grow without bound from frames that have not been processed.

##### Special Considerations

This method uses [`dispatch_retain`](https://developer.apple.com/documentation/dispatch/1496306-dispatch_retain) and [`dispatch_release`](https://developer.apple.com/documentation/dispatch/1496328-dispatch_release) to manage the queue.

## Parameters

- `sampleBufferDelegate`: An object conforming to the   protocol that will receive sample buffers after they are captured.
- `sampleBufferCallbackQueue`: The sampleBufferCallbackQueue parameter may not be  , except when setting the   to  .

## See Also

- [var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?](avcapturevideodataoutput/samplebufferdelegate.md)
  The capture object’s delegate.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](avcapturevideodataoutput/samplebuffercallbackqueue.md)
  The queue on which the system invokes delegate callbacks.
- [protocol AVCaptureVideoDataOutputSampleBufferDelegate](avcapturevideodataoutputsamplebufferdelegate.md)
  Methods for receiving sample buffers from, and monitoring the status of, a video data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/setsamplebufferdelegate(_:queue:))*