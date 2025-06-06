# status

**Framework**: GameKit  
**Kind**: property

The status of the exchange request.

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
var status: GKTurnBasedExchangeStatus { get }
```

## See Also

- [func reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: (((any Error)?) -> Void)?)](gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:).md)
  Replies to an exchange request on behalf of a recipient.
- [var replies: [GKTurnBasedExchangeReply]?](gkturnbasedexchange/replies.md)
  The replies from recipients of the exchange request.
- [enum GKTurnBasedExchangeStatus](gkturnbasedexchangestatus.md)
  The status of an exchange or reply.
- [var completionDate: Date?](gkturnbasedexchange/completiondate.md)
  The date when all recipients of the exchange request reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/status)*