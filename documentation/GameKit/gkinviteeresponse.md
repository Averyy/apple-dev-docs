# GKInviteeResponse

**Framework**: GameKit  
**Kind**: typealias  
**Role**: Type Alias

Possible responses from an invitation to a remote player.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.8+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

## Declaration

```swift
typealias GKInviteeResponse = GKInviteRecipientResponse
```

```c
typedef GKInviteRecipientResponse GKInviteeResponse;
```

## Topics

### Responses
- [static var inviteeResponseAccepted: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponseaccepted.md)
  The player accepted the invitation.
- [static var inviteeResponseDeclined: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponsedeclined.md)
  The player rejected the invitation.
- [static var inviteeResponseFailed: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponsefailed.md)
  The invitation was unable to be delivered.
- [static var inviteeResponseIncompatible: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponseincompatible.md)
  The invitee isn’t running a compatible version of your game.
- [static var inviteeResponseUnableToConnect: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponseunabletoconnect.md)
  The invitee couldn’t be contacted.
- [static var inviteeResponseNoAnswer: GKInviteRecipientResponse](./gkinviterecipientresponse/inviteeresponsenoanswer.md)
  The invitation timed out without an answer.

## See Also

### Deprecated methods and properties
- [var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?](./gkmatchrequest/inviteeresponsehandler.md)
  Handles when a player responds to an invitation.
- [var playersToInvite: [String]?](./gkmatchrequest/playerstoinvite.md)
  A list of player identifiers for players to invite to the match.
- [var restrictToAutomatch: Bool](./gkmatchrequest/restricttoautomatch.md)
  A Boolean value that determines whether a game uses automatch to find players or the local player invites players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeresponse)*