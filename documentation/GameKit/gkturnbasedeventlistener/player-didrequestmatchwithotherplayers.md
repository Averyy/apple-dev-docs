# player(_:didRequestMatchWithOtherPlayers:)

**Framework**: GameKit  
**Kind**: method

Handles when the player uses Game Center to start a match with other players.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithOtherPlayers playersToInvite: [GKPlayer])
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to present a turn-based matchmaker interface configured with the players to invite:

1. Create a [`GKMatchRequest`](gkmatchrequest.md) object.
2. Set the match request’s [`recipients`](gkmatchrequest/recipients.md) property to `playersToInvite`.
3. Create a [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) with the match request object.
4. Present the turn-based matchmaker view controller.

## Parameters

- `player`: The player who receives this turn-based event.
- `playersToInvite`: The players to invite in the view controller interface.

## See Also

- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:matchended:).md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:wantstoquitmatch:).md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:))*