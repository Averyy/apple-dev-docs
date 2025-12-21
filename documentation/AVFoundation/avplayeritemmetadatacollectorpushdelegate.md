# AVPlayerItemMetadataCollectorPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol you implement to receive metadata callbacks from a player item metadata collector.

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
protocol AVPlayerItemMetadataCollectorPushDelegate : NSObjectProtocol, Sendable
```

## Topics

### Accessing HLS date range metadata
- [func metadataCollector(AVPlayerItemMetadataCollector, didCollect: sending [AVDateRangeMetadataGroup], indexesOfNewGroups: IndexSet, indexesOfModifiedGroups: IndexSet)](avplayeritemmetadatacollectorpushdelegate/metadatacollector(_:didcollect:indexesofnewgroups:indexesofmodifiedgroups:).md)
  Tells the delegate the collected metadata group information has changed and needs to be updated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setDelegate((any AVPlayerItemMetadataCollectorPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadatacollector/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate will be called.
- [var delegate: (any AVPlayerItemMetadataCollectorPushDelegate)?](avplayeritemmetadatacollector/delegate.md)
  Accesses the metadata collector’s delegate object.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadatacollector/delegatequeue.md)
  The dispatch queue on which the delegate’s methods are called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate)*