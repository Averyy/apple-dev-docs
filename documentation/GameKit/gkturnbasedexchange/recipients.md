# recipients

**Framework**: GameKit  
**Kind**: property

The participants who receives the exchange request.

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
var recipients: [GKTurnBasedParticipant] { get }
```

## See Also

- [var exchangeID: String](gkturnbasedexchange/exchangeid.md)
  The identifier for the exchange request.
- [var sender: GKTurnBasedParticipant](gkturnbasedexchange/sender.md)
  The participant who sends the exchange request to recipients.
- [var data: Data?](gkturnbasedexchange/data.md)
  The game-specific exchange data that GameKit sends to participants.
- [var message: String?](gkturnbasedexchange/message.md)
  A localized message from the sender to the recipients of an exchange request.
- [var sendDate: Date](gkturnbasedexchange/senddate.md)
  The date that the sender initiates the exchange request.
- [var timeoutDate: Date?](gkturnbasedexchange/timeoutdate.md)
  The date that the recipients must reply by before the exchange request times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/recipients)*