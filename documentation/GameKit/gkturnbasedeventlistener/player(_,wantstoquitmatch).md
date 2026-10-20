# player(_:wantsToQuitMatch:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) player:(GKPlayer *) player wantsToQuitMatch:(GKTurnBasedMatch *) match;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to forfeit the match by passing the turn to the next participant using the  [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](../gkturnbasedmatch/participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md) method.

## Parameters

- `player`: The player who receives this turn-based event.
- `match`: The match that the current participant wants to quit.

## See Also

### Handling Match-Related Events
- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](./player%28_,receivedturneventfor,didbecomeactive%29.md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](./player%28_,didrequestmatchwithotherplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](./player%28_,matchended%29.md)
  Handles when the match ends.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](./player%28_,didrequestmatchwithplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:wantstoquitmatch:))*