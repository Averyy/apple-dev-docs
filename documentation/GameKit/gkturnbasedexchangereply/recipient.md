# recipient

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The participant who replies to the exchange request.

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
var recipient: GKTurnBasedParticipant { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) GKTurnBasedParticipant * recipient;
```

*macOS*

```objc
@property (atomic, readonly, nullable) GKTurnBasedParticipant * recipient;
```

## See Also

### Retrieving Reply Details
- [var data: Data?](./data.md)
  The game-specific data that the recipent provides in the exchange request reply.
- [var message: String?](./message.md)
  A message from the recipient to the sender of the exchange request.
- [var replyDate: Date](./replydate.md)
  The date the recipient replies to the exchange request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/recipient)*