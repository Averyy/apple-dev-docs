# handleInvite(fromGameCenter:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sent to the delegate when the local player receives an invitation to join a new turn-based match.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
func handleInvite(fromGameCenter playersToInvite: [String])
```

```objc
- (void) handleInviteFromGameCenter:(NSArray<NSString *> *) playersToInvite;
```

## Discussion

When your delegate receives this message, your game should create a new [`GKMatchRequest`](../gkmatchrequest.md) object and assign the `playersToInvite` parameter to the match request’s [`playersToInvite`](../gkmatchrequest/playerstoinvite.md) property. Then, your game can either call the [`GKTurnBasedMatch`](../gkturnbasedmatch.md) class method [`find(for:withCompletionHandler:)`](../gkturnbasedmatch/find%28for,withcompletionhandler%29.md) to find a match programmatically or it can use the request to instantiate a new [`GKTurnBasedMatchmakerViewController`](../gkturnbasedmatchmakerviewcontroller.md) object to show a user interface to the player.

## Parameters

- `playersToInvite`: An array of `NSString` objects containing the player identifiers for the players to initially invite to the game.

## See Also

### Receiving Turn-based Events
- [func handleTurnEvent(for: GKTurnBasedMatch)](./handleturnevent%28for%29.md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](./handleturnevent%28for,didbecomeactive%29.md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](./handlematchended%28_%29.md)
  Sent to the delegate when a match the local player is participating in has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:))*