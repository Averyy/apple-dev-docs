# player(_:didRequestMatchWithPlayers:)

**Framework**: GameKit  
**Kind**: method

Handles the event when the local player sends other players an invitation to join a match.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String])
```

#### Discussion

When you call this method, GameKit launches the game and starts the matchmaking process.

## Parameters

- `player`: The local player who sends the invitation.
- `playerIDsToInvite`: The identifiers for the players who receive invitations to join the match.

## See Also

- [func player(GKPlayer, didAccept: GKInvite)](gkinviteeventlistener/player(_:didaccept:).md)
  Handles the event when the local player accepts an invitation from another player.
- [func player(GKPlayer, didRequestMatchWithRecipients: [GKPlayer])](gkinviteeventlistener/player(_:didrequestmatchwithrecipients:).md)
  Handles the event when the local player sends other players an invitation to join a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/player(_:didrequestmatchwithplayers:))*