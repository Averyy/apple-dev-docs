# AVPlayerItemLegibleOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to provide alternative attributed-string output.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

```objc
@protocol AVPlayerItemLegibleOutputPushDelegate <AVPlayerItemOutputPushDelegate>
```

#### Overview

This protocol extends the [`AVPlayerItemOutputPushDelegate`](./avplayeritemoutputpushdelegate.md) protocol.

## Topics

### Providing alternative attributed-string output
- [func legibleOutput(AVPlayerItemLegibleOutput, didOutputAttributedStrings: [NSAttributedString], nativeSampleBuffers: [Any], forItemTime: CMTime)](./avplayeritemlegibleoutputpushdelegate/legibleoutput%28_,didoutputattributedstrings,nativesamplebuffers,foritemtime%29.md)
  Asks the delegate to process the delivery of new textual samples.

## Relationships

### Inherits From
- [AVPlayerItemOutputPushDelegate](./avplayeritemoutputpushdelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the delegate
- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](./avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./avplayeritemlegibleoutput/setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [var advanceIntervalForDelegateInvocation: TimeInterval](./avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemlegibleoutput/delegatequeue.md)
  The dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate)*