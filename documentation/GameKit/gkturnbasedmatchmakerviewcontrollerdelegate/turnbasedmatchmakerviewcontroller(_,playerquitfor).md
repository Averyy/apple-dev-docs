# turnBasedMatchmakerViewController(_:playerQuitFor:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Handles when a player quits the match.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0
- iPadOS 5.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.11
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`GKTurnBasedEventListener`](../gkturnbasedeventlistener.md) method [`player(_:wantsToQuitMatch:)`](../gkturnbasedeventlistener/player%28_,wantstoquitmatch%29.md) instead.

## Declaration

```swift
optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitFor match: GKTurnBasedMatch)
```

```objc
- (void) turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController *) viewController playerQuitForMatch:(GKTurnBasedMatch *) match;
```

#### Discussion

When GameKit invokes this method, the player forfeits the match without taking their turn. Implement this method to dismiss the view controller, set an outcome for the player, and then call the match’s [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](../gkturnbasedmatch/participantquitinturn%28with,nextparticipants,turntimeout,match,completionhandler%29.md) method.

## Parameters

- `viewController`: The view controller with which the player interacts.
- `match`: The match that the player quits.

## See Also

### Deprecated Methods
- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, didFind: GKTurnBasedMatch)](./turnbasedmatchmakerviewcontroller%28_,didfind%29.md)
  Handles when the view controller finds participants for a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:playerquitfor:))*