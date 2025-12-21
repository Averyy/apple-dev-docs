# AVPlayerItemLegibleOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods you can implement to provide alternative attributed-string output.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

#### Overview

This protocol extends the [`AVPlayerItemOutputPushDelegate`](avplayeritemoutputpushdelegate.md) protocol.

## Topics

### Providing alternative attributed-string output
- [func legibleOutput(AVPlayerItemLegibleOutput, didOutputAttributedStrings: [NSAttributedString], nativeSampleBuffers: [Any], forItemTime: CMTime)](avplayeritemlegibleoutputpushdelegate/legibleoutput(_:didoutputattributedstrings:nativesamplebuffers:foritemtime:).md)
  Asks the delegate to process the delivery of new textual samples.

## Relationships

### Inherits From
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemlegibleoutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [var delegateQueue: dispatch_queue_t?](avplayeritemlegibleoutput/delegatequeue.md)
  The dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)*