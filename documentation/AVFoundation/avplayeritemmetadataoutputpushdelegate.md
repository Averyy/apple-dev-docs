# AVPlayerItemMetadataOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to provide additional metadata.

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
protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

```objc
@protocol AVPlayerItemMetadataOutputPushDelegate <AVPlayerItemOutputPushDelegate>
```

## Overview

This protocol extends the [`AVPlayerItemOutputPushDelegate`](./avplayeritemoutputpushdelegate.md) protocol.

## Topics

### Combining timed metadata groups
- [func metadataOutput(AVPlayerItemMetadataOutput, didOutputTimedMetadataGroups: sending [AVTimedMetadataGroup], from: AVPlayerItemTrack?)](./avplayeritemmetadataoutputpushdelegate/metadataoutput%28_,didoutputtimedmetadatagroups,from%29.md)
  Tells the delegate a new collection of metadata items is available.

## Relationships

### Inherits From
- [AVPlayerItemOutputPushDelegate](./avplayeritemoutputpushdelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the delegate
- [var advanceIntervalForDelegateInvocation: TimeInterval](./avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [var delegate: (any AVPlayerItemMetadataOutputPushDelegate)?](./avplayeritemmetadataoutput/delegate.md)
  The delegate object.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemmetadataoutput/delegatequeue.md)
  The dispatch queue on which messages are sent to the delegate.
- [func setDelegate((any AVPlayerItemMetadataOutputPushDelegate)?, queue: dispatch_queue_t?)](./avplayeritemmetadataoutput/setdelegate%28_,queue%29.md)
  Sets the delegate and a dispatch queue on which the delegate is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate)*