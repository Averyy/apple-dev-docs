# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the receiver’s delegate and a dispatch queue on which the delegate is called.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVPlayerItemLegibleOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

#### Discussion

Because the delegate is held using a zeroing-weak reference, it is safe to deallocate the delegate while the receiver still has a reference to it.

## Parameters

- `delegate`: An object conforming to the   protocol.
- `delegateQueue`: A dispatch queue on which all delegate methods will be called.

## See Also

- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [protocol AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md)
  Methods you can implement to provide alternative attributed-string output.
- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [var delegateQueue: dispatch_queue_t?](avplayeritemlegibleoutput/delegatequeue.md)
  The dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/setdelegate(_:queue:))*