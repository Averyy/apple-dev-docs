# inviteMessage

**Framework**: GameKit  
**Kind**: property

The message sent to other players when the local player invites them to join a match.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var inviteMessage: String? { get set }
```

## See Also

- [var recipients: [GKPlayer]?](gkmatchrequest/recipients.md)
  The players to invite to the match.
- [var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)?](gkmatchrequest/recipientresponsehandler.md)
  A method that handles when a player responds to an invitation to join a match.
- [enum GKInviteRecipientResponse](gkinviterecipientresponse.md)
  A player’s response to an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchrequest/invitemessage)*