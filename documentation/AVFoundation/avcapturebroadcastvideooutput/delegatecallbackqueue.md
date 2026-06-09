# delegateCallbackQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) methods will be called.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

#### Discussion

The value of this property is a dispatch queue on which all delegate method calls will be serialized. If you have not called the [`setDelegate(_:queue:)`](avcapturebroadcastvideooutput/setdelegate(_:queue:).md) method, the value of this property will be `nil`.

## See Also

- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](avcapturebroadcastvideooutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](avcapturebroadcastvideooutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegatecallbackqueue)*