# NSMetadataQuery.DidStartGatheringMessage

**Framework**: Foundation  
**Kind**: struct

A message a metadata query sends when it starts the initial result-gathering phase of the query.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DidStartGatheringMessage
```

#### Overview

Observe this message with the identifier [`didStartGathering`](notificationcenter/messageidentifier/didstartgathering.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSMetadataQuery`](nsmetadataquery.md).

This message interoperates with the notification [`NSMetadataQueryDidStartGathering`](nsnotification/name-swift.struct/nsmetadataquerydidstartgathering.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](nsmetadataquery/didstartgatheringmessage/init.md)
  Creates a message for a metadata query that is starting its initial result gathering.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NSMetadataQuery.DidFinishGatheringMessage](nsmetadataquery/didfinishgatheringmessage.md)
  A message a metadata query sends when it finishes the initial result-gathering phase of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/didstartgatheringmessage)*