# sampleBufferCallbackQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The queue on which delegate callbacks are invoked

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var sampleBufferCallbackQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t sampleBufferCallbackQueue;
```

## See Also

### Receiving captured audio data
- [func setSampleBufferDelegate((any AVCaptureAudioDataOutputSampleBufferDelegate)?, queue: dispatch_queue_t?)](./setsamplebufferdelegate%28_,queue%29.md)
  Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [var sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)?](./samplebufferdelegate.md)
  The capture object’s delegate.
- [protocol AVCaptureAudioDataOutputSampleBufferDelegate](../avcaptureaudiodataoutputsamplebufferdelegate.md)
  Methods for receiving audio sample data from an audio capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/samplebuffercallbackqueue)*