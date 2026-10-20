# player(_:matchEnded:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) player:(GKPlayer *) player matchEnded:(GKTurnBasedMatch *) match;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to stop gameplay, notify the player that the match is over, and show the participant outcomes.

## Parameters

- `player`: The player who receives this turn-based event.
- `match`: The match that ends.

## See Also

### Handling Match-Related Events
- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](./player%28_,receivedturneventfor,didbecomeactive%29.md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](./player%28_,didrequestmatchwithotherplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](./player%28_,wantstoquitmatch%29.md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](./player%28_,didrequestmatchwithplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:matchended:))*