# player(_:didRequestMatchWithOtherPlayers:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) player:(GKPlayer *) player didRequestMatchWithOtherPlayers:(NSArray<GKPlayer *> *) playersToInvite;
```

## Mentions

- [Starting turn-based matches and passing turns between players](../starting-turn-based-matches-and-passing-turns-between-players.md)

#### Discussion

Implement this method to present a turn-based matchmaker interface configured with the players to invite:

1. Create a [`GKMatchRequest`](../gkmatchrequest.md) object.
2. Set the match request’s [`recipients`](../gkmatchrequest/recipients.md) property to `playersToInvite`.
3. Create a [`GKTurnBasedMatchmakerViewController`](../gkturnbasedmatchmakerviewcontroller.md) with the match request object.
4. Present the turn-based matchmaker view controller.

## Parameters

- `player`: The player who receives this turn-based event.
- `playersToInvite`: The players to invite in the view controller interface.

## See Also

### Handling Match-Related Events
- [func player(GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](./player%28_,receivedturneventfor,didbecomeactive%29.md)
  Handles turn-based match events, such as accepting invitations, passing turns, and saving match data.
- [func player(GKPlayer, matchEnded: GKTurnBasedMatch)](./player%28_,matchended%29.md)
  Handles when the match ends.
- [func player(GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](./player%28_,wantstoquitmatch%29.md)
  Handles when the current participant wants to quit a match.
- [func player(GKPlayer, didRequestMatchWithPlayers: [String])](./player%28_,didrequestmatchwithplayers%29.md)
  Handles when the player uses Game Center to start a match with other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/player(_:didrequestmatchwithotherplayers:))*