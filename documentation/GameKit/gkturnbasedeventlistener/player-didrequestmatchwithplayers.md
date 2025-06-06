# player(_:didRequestMatchWithPlayers:)

**Framework**: GameKit  
**Kind**: method

Handles when the player uses Game Center to start a match with other players.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String])
```

#### Discussion

Implement this method to present a [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) configured with the players to invite specified by the `playerIDsToInvite` parameter.

## Parameters

- `player`: The player who receives this turn-based event. .
- `playerIDsToInvite`: The identifiers for the players to invite in the view controller interface.

## See Also

- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:).md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:matchended:).md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:wantstoquitmatch:).md)
  Handles when the current participant wants to quit a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:))*