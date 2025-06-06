# turnBasedMatchmakerViewController(_:playerQuitFor:)

**Framework**: GameKit  
**Kind**: method

Handles when a player quits the match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitFor match: GKTurnBasedMatch)
```

#### Discussion

When GameKit invokes this method, the player forfeits the match without taking their turn. Implement this method to dismiss the view controller, set an outcome for the player, and then call the match’s [`participantQuitInTurn(with:nextParticipants:turnTimeout:match:completionHandler:)`](gkturnbasedmatch/participantquitinturn(with:nextparticipants:turntimeout:match:completionhandler:).md) method.

## Parameters

- `viewController`: The view controller with which the player interacts.
- `match`: The match that the player quits.

## See Also

- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, didFind: GKTurnBasedMatch)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfind:).md)
  Handles when the view controller finds participants for a turn-based match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:playerquitfor:))*