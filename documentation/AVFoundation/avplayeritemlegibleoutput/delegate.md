# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate of the output class.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVPlayerItemLegibleOutputPushDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<AVPlayerItemLegibleOutputPushDelegate> delegate;
```

## Discussion

Because the delegate is held using a zeroing-weak reference, this property has a value of `nil` after a delegate that was previously set has been deallocated.

This property does not support key-value observing.

## See Also

### Configuring the delegate
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [protocol AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md)
  Methods you can implement to provide alternative attributed-string output.
- [var advanceIntervalForDelegateInvocation: TimeInterval](./advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/delegate)*