# player(_:receivedTurnEventFor:didBecomeActive:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.

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
optional func player(_ player: GKPlayer, receivedTurnEventFor match: GKTurnBasedMatch, didBecomeActive: Bool)
```

```objc
- (void) player:(GKPlayer *) player receivedTurnEventForMatch:(GKTurnBasedMatch *) match didBecomeActive:(BOOL) didBecomeActive;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)
- [Sending messages to players in turn-based games](../sending-messages-to-players-in-turn-based-games.md)
- [Exchanging data between players in turn-based games](../exchanging-data-between-players-in-turn-based-games.md)

## Discussion

GameKit invokes this method when these turn-based events occur:

- GameKit passes the turn to the player.
- The player accepts an invitation from another participant.
- The timeout for the player to take their turn is about to expire.
- A participant saves match data to Game Center.
- Another participant sends a reminder to the player.
- The player opens an existing or completed match.
- The player forfeits a match.

## Parameters

- `player`: The player who receives this turn-based event.
- `match`: The match related to this turn-based event.
- `didBecomeActive`: [`true`](../../Swift/true.md) if the system launches the game to deliver the turn-based event; otherwise, [`false`](../../Swift/false.md).

## See Also

### Handling Match-Related Events
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](./player%28_,didrequestmatchwithotherplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](./player%28_,matchended%29.md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](./player%28_,wantstoquitmatch%29.md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](./player%28_,didrequestmatchwithplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:))*