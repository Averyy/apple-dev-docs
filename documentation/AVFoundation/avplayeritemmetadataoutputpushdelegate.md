# AVPlayerItemMetadataOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods you can implement to provide additional metadata.

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
protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

#### Overview

This protocol extends the [`AVPlayerItemOutputPushDelegate`](avplayeritemoutputpushdelegate.md) protocol.

## Topics

### Combining Timed Metadata Groups
- [func metadataOutput(AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups: [AVTimedMetadataGroup], from: AVPlayerItemTrack?)](avplayeritemmetadataoutputpushdelegate/metadataoutput(_:didoutputtimedmetadatagroups:from:).md)
  Tells the delegate a new collection of metadata items is available.

## Relationships

### Inherits From
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [var delegate: (any AVPlayerItemMetadataOutputPushDelegate)?](avplayeritemmetadataoutput/delegate.md)
  The delegate object.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadataoutput/delegatequeue.md)
  The dispatch queue on which messages are sent to the delegate.
- [func setDelegate((any AVPlayerItemMetadataOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadataoutput/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate)*