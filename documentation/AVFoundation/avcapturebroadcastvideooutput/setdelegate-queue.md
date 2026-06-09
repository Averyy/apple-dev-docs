# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
func setDelegate(_ delegate: (any AVCaptureBroadcastVideoOutputDelegate)?, queue delegateCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `delegate`: An object conforming to the [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) protocol that will receive broadcast video output notifications.
- `delegateCallbackQueue`: A dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) methods will be called.

## See Also

- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturebroadcastvideooutput/delegatecallbackqueue.md)
  The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) methods will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/setdelegate(_:queue:))*