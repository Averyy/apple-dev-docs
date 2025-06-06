# advanceIntervalForDelegateInvocation

**Framework**: AVFoundation  
**Kind**: property

The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var advanceIntervalForDelegateInvocation: TimeInterval { get set }
```

#### Discussion

If possible, an `AVPlayerItemLegibleOutput` instance messages its delegate `advanceIntervalForDelegateInvocation` seconds earlier than it otherwise would.

If the value provided is large, the delegate methods are invoked as soon as possible.

## See Also

- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemlegibleoutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [protocol AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md)
  Methods you can implement to provide alternative attributed-string output.
- [var delegateQueue: dispatch_queue_t?](avplayeritemlegibleoutput/delegatequeue.md)
  The dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/advanceintervalfordelegateinvocation)*