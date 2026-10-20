# replies

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The replies from recipients of the exchange request.

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
var replies: [GKTurnBasedExchangeReply]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSArray<GKTurnBasedExchangeReply *> * replies;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSArray<GKTurnBasedExchangeReply *> * replies;
```

## See Also

### Replying to Exchange Requests
- [func reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: (((any Error)?) -> Void)?)](./reply%28withlocalizablemessagekey,arguments,data,completionhandler%29.md)
  Replies to an exchange request on behalf of a recipient.
- [var status: GKTurnBasedExchangeStatus](./status.md)
  The status of the exchange request.
- [enum GKTurnBasedExchangeStatus](../gkturnbasedexchangestatus.md)
  The status of an exchange or reply.
- [var completionDate: Date?](./completiondate.md)
  The date when all recipients of the exchange request reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/replies)*