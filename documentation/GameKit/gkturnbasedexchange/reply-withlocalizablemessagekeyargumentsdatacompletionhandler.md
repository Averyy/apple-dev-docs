# reply(withLocalizableMessageKey:arguments:data:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Replies to an exchange request on behalf of a recipient.

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
func reply(withLocalizableMessageKey key: String, arguments: [String], data: Data) async throws
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

To accept or decline an exchange request, invoke this method from the [`player(_:receivedExchangeRequest:for:)`](gkturnbasedeventlistener/player(_:receivedexchangerequest:for:).md) protocol method. Include game-specific details about the exchange in the `data` parameter. When all recipients reply or time out, GameKit invokes the [`player(_:receivedExchangeReplies:forCompletedExchange:for:)`](gkturnbasedeventlistener/player(_:receivedexchangereplies:forcompletedexchange:for:).md) protocol method in the game instances of the sender and the current participant.

## Parameters

- `key`: The identifier for looking up the translated reply message in the default   file. If you use a formatted string with specifiers, provide the arguments.
- `arguments`: A list of arguments to substitute into the localized string if it’s formatted and contains specifiers.
- `data`: The game-specific data associated with the reply.
- `completionHandler`: The block receives the following parameter:

## See Also

- [var replies: [GKTurnBasedExchangeReply]?](gkturnbasedexchange/replies.md)
  The replies from recipients of the exchange request.
- [var status: GKTurnBasedExchangeStatus](gkturnbasedexchange/status.md)
  The status of the exchange request.
- [enum GKTurnBasedExchangeStatus](gkturnbasedexchangestatus.md)
  The status of an exchange or reply.
- [var completionDate: Date?](gkturnbasedexchange/completiondate.md)
  The date when all recipients of the exchange request reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/reply(withlocalizablemessagekey:arguments:data:completionhandler:))*