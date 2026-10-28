# player(_:didRequestMatchWithPlayers:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when the player uses Game Center to start a match with other players.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use the [`player(_:didRequestMatchWithOtherPlayers:)`](./player%28_,didrequestmatchwithotherplayers%29.md) method instead.

## Declaration

```swift
optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String])
```

```objc
- (void) player:(GKPlayer *) player didRequestMatchWithPlayers:(NSArray<NSString *> *) playerIDsToInvite;
```

## Discussion

Implement this method to present a [`GKTurnBasedMatchmakerViewController`](../gkturnbasedmatchmakerviewcontroller.md) configured with the players to invite specified by the `playerIDsToInvite` parameter.

## Parameters

- `player`: The player who receives this turn-based event. .
- `playerIDsToInvite`: The identifiers for the players to invite in the view controller interface.

## See Also

### Handling Match-Related Events
- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](./player%28_,receivedturneventfor,didbecomeactive%29.md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](./player%28_,didrequestmatchwithotherplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](./player%28_,matchended%29.md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](./player%28_,wantstoquitmatch%29.md)
  Handles when the current participant wants to quit a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:didrequestmatchwithplayers:))*