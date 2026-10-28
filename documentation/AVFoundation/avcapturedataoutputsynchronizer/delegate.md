# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A delegate object that receives synchronized capture data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var delegate: (any AVCaptureDataOutputSynchronizerDelegate)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<AVCaptureDataOutputSynchronizerDelegate> delegate;
```

## Discussion

This property is read-only. You set the delegate object and the dispatch queue for delegate methods together using the [`setDelegate(_:queue:)`](./setdelegate%28_,queue%29.md) method.

## See Also

### Receiving synchronized capture data
- [func setDelegate((any AVCaptureDataOutputSynchronizerDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.
- [var delegateCallbackQueue: dispatch_queue_t?](./delegatecallbackqueue.md)
  A dispatch queue for delivering synchronized capture data.
- [protocol AVCaptureDataOutputSynchronizerDelegate](../avcapturedataoutputsynchronizerdelegate.md)
  Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/delegate)*