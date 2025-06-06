# GKInviteRecipientResponse

**Framework**: GameKit  
**Kind**: enum

A player’s response to an invitation to join a match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKInviteRecipientResponse
```

## Topics

### Responses
- [GKInviteRecipientResponse.accepted](gkinviterecipientresponse/accepted.md)
  A response when the player accepts the invitation.
- [GKInviteRecipientResponse.declined](gkinviterecipientresponse/declined.md)
  A response when the player rejects the invitation.
- [GKInviteRecipientResponse.failed](gkinviterecipientresponse/failed.md)
  A response when the system fails to deliver the invitation to the player.
- [GKInviteRecipientResponse.incompatible](gkinviterecipientresponse/incompatible.md)
  A response when the player isn’t running a compatible version of the game.
- [GKInviteRecipientResponse.unableToConnect](gkinviterecipientresponse/unabletoconnect.md)
  A response when the system can’t contact the player.
- [GKInviteRecipientResponse.noAnswer](gkinviterecipientresponse/noanswer.md)
  A response when the invitation times out because the player doesn’t answer it.
### Deprecated Properties
- [static var inviteeResponseAccepted: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponseaccepted.md)
  The player accepted the invitation.
- [static var inviteeResponseDeclined: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponsedeclined.md)
  The player rejected the invitation.
- [static var inviteeResponseFailed: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponsefailed.md)
  The invitation was unable to be delivered.
- [static var inviteeResponseIncompatible: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponseincompatible.md)
  The invitee isn’t running a compatible version of your game.
- [static var inviteeResponseNoAnswer: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponsenoanswer.md)
  The invitation timed out without an answer.
- [static var inviteeResponseUnableToConnect: GKInviteRecipientResponse](gkinviterecipientresponse/inviteeresponseunabletoconnect.md)
  The invitee couldn’t be contacted.
### Initializers
- [init?(rawValue: Int)](gkinviterecipientresponse/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var inviteMessage: String?](gkmatchrequest/invitemessage.md)
  The message sent to other players when the local player invites them to join a match.
- [var recipients: [GKPlayer]?](gkmatchrequest/recipients.md)
  The players to invite to the match.
- [var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)?](gkmatchrequest/recipientresponsehandler.md)
  A method that handles when a player responds to an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)*