# player(_:didAccept:)

**Framework**: GameKit  
**Kind**: method

Handles the event when the local player accepts an invitation from another player.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didAccept invite: GKInvite)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

This method presents the matchmaker view controller in the invitation state so that the local player can see other players in the match accept their invitations.

## Parameters

- `player`: The local player who accepts the invitation.
- `invite`: The invitation that the local player accepts.

## See Also

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [func player(GKPlayer, didRequestMatchWithRecipients: [GKPlayer])](gkinviteeventlistener/player(_:didrequestmatchwithrecipients:).md)
  Handles the event when the local player sends other players an invitation to join a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkinviteeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles the event when the local player sends other players an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/player(_:didaccept:))*