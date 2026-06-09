# delegate

**Framework**: AVFoundation  
**Kind**: property

The receiver’s delegate.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var delegate: (any AVCaptureBroadcastVideoOutputDelegate)? { get }
```

#### Discussion

The value of this property is an object conforming to the [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) protocol that will be able to monitor the broadcast output operations.

## See Also

- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](avcapturebroadcastvideooutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturebroadcastvideooutput/delegatecallbackqueue.md)
  The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) methods will be called.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](avcapturebroadcastvideooutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegate)*