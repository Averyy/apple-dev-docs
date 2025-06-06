# player(_:wantsToQuitMatch:)

**Framework**: GameKit  
**Kind**: method

Handles when the current participant wants to quit a match.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func player(_ player: GKPlayer, wantsToQuitMatch match: GKTurnBasedMatch)
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to forfeit the match by passing the turn to the next participant using the  [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `match`: The match that the current participant wants to quit.

## See Also

- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:).md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](gkturnbasedeventlistener/player(_:matchended:).md)
  Handles when the match ends.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:).md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:wantstoquitmatch:))*