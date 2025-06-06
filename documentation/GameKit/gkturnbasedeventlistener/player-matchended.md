# player(_:matchEnded:)

**Framework**: GameKit  
**Kind**: method

Handles when the match ends.

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
optional func player(_ player: GKPlayer, matchEnded match: GKTurnBasedMatch)
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to stop gameplay, notify the player that the match is over, and show the participant outcomes.

## Parameters

- `player`: The player who receives this turn-based event.
- `match`: The match that ends.

## See Also

- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:).md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:wantstoquitmatch:).md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:matchended:))*