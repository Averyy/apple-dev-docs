# completionDate

**Framework**: GameKit  
**Kind**: property

The date when all recipients of the exchange request reply.

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
var completionDate: Date? { get }
```

#### Discussion

The date the exchange [`status`](gkturnbasedexchange/status.md) property becomes [`GKTurnBasedExchangeStatus.complete`](gkturnbasedexchangestatus/complete.md).

## See Also

- [func reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md)
  Replies to an exchange request on behalf of a recipient.
- [var replies: [GKTurnBasedExchangeReply]?](gkturnbasedexchange/replies.md)
  The replies from recipients of the exchange request.
- [var status: GKTurnBasedExchangeStatus](gkturnbasedexchange/status.md)
  The status of the exchange request.
- [enum GKTurnBasedExchangeStatus](gkturnbasedexchangestatus.md)
  The status of an exchange or reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/completiondate)*