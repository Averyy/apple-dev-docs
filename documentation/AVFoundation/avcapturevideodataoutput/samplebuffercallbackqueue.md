# sampleBufferCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The queue on which the system invokes delegate callbacks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBufferCallbackQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t sampleBufferCallbackQueue;
```

## Discussion

You set the queue using [`setSampleBufferDelegate(_:queue:)`](./setsamplebufferdelegate%28_,queue%29.md).

## See Also

### Receiving captured video data
- [func setSampleBufferDelegate((any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](./setsamplebufferdelegate%28_,queue%29.md)
  Sets the sample buffer delegate and the queue for invoking callbacks.
- [var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?](./samplebufferdelegate.md)
  The capture object’s delegate.
- [protocol AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md)
  Methods for receiving sample buffers from, and monitoring the status of, a video data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/samplebuffercallbackqueue)*