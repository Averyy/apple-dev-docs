# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var delegate: (any AVCaptureBroadcastVideoOutputDelegate)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<AVCaptureBroadcastVideoOutputDelegate> delegate;
```

## Discussion

The value of this property is an object conforming to the [`AVCaptureBroadcastVideoOutputDelegate`](../avcapturebroadcastvideooutputdelegate.md) protocol that will be able to monitor the broadcast output operations.

## See Also

### Related Documentation
- [protocol AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
### Managing the Output
- [var delegateCallbackQueue: dispatch_queue_t?](./delegatecallbackqueue.md)
  The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](../avcapturebroadcastvideooutputdelegate.md) methods will be called.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegate)*