# sampleBufferDelegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) id<AVCaptureVideoDataOutputSampleBufferDelegate> sampleBufferDelegate;
```

#### Discussion

The delegate receives sample buffers after they are captured.

You set the delegate using [`setSampleBufferDelegate(_:queue:)`](./setsamplebufferdelegate%28_,queue%29.md).

## See Also

### Receiving captured video data
- [func setSampleBufferDelegate((any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](./setsamplebufferdelegate%28_,queue%29.md)
  Sets the sample buffer delegate and the queue for invoking callbacks.
- [var sampleBufferCallbackQueue: dispatch_queue_t?](./samplebuffercallbackqueue.md)
  The queue on which the system invokes delegate callbacks.
- [protocol AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md)
  Methods for receiving sample buffers from, and monitoring the status of, a video data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/samplebufferdelegate)*