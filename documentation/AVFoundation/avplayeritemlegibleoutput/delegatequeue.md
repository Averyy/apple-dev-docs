# delegateQueue

**Framework**: AVFoundation  
**Kind**: property

The dispatch queue on which the delegate is called.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get }
```

#### Discussion

This property does not support key-value observing.

## See Also

- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemlegibleoutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [protocol AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md)
  Methods you can implement to provide alternative attributed-string output.
- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/delegatequeue)*