# GKTurnBasedExchangeStatus

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The status of an exchange or reply.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKTurnBasedExchangeStatus
```

```c
enum GKTurnBasedExchangeStatus : int8_t;
```

## Topics

### Statuses
- [GKTurnBasedExchangeStatus.unknown](./gkturnbasedexchangestatus/unknown.md)
  The state of the exchange request is unknown.
- [GKTurnBasedExchangeStatus.active](./gkturnbasedexchangestatus/active.md)
  GameKit sent the exchange request to recipients but not all recipients replied.
- [GKTurnBasedExchangeStatus.complete](./gkturnbasedexchangestatus/complete.md)
  All recipients of the exchange request replied.
- [GKTurnBasedExchangeStatus.resolved](./gkturnbasedexchangestatus/resolved.md)
  The current participant saved the exchange request.
- [GKTurnBasedExchangeStatus.canceled](./gkturnbasedexchangestatus/canceled.md)
  The sender canceled the exchange request.
### Initializers
- [init?(rawValue: Int8)](./gkturnbasedexchangestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Replying to Exchange Requests
- [func reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: (((any Error)?) -> Void)?)](./gkturnbasedexchange/reply%28withlocalizablemessagekey,arguments,data,completionhandler%29.md)
  Replies to an exchange request on behalf of a recipient.
- [var replies: [GKTurnBasedExchangeReply]?](./gkturnbasedexchange/replies.md)
  The replies from recipients of the exchange request.
- [var status: GKTurnBasedExchangeStatus](./gkturnbasedexchange/status.md)
  The status of the exchange request.
- [var completionDate: Date?](./gkturnbasedexchange/completiondate.md)
  The date when all recipients of the exchange request reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)*