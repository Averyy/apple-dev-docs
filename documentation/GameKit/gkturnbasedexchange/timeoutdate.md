# timeoutDate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The date that the recipients must reply by before the exchange request times out.

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
var timeoutDate: Date? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSDate * timeoutDate;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSDate * timeoutDate;
```

## See Also

### Retrieving Exchange Details
- [var exchangeID: String](./exchangeid.md)
  The identifier for the exchange request.
- [var sender: GKTurnBasedParticipant](./sender.md)
  The participant who sends the exchange request to recipients.
- [var recipients: [GKTurnBasedParticipant]](./recipients.md)
  The participants who receives the exchange request.
- [var data: Data?](./data.md)
  The game-specific exchange data that GameKit sends to participants.
- [var message: String?](./message.md)
  A localized message from the sender to the recipients of an exchange request.
- [var sendDate: Date](./senddate.md)
  The date that the sender initiates the exchange request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/timeoutdate)*