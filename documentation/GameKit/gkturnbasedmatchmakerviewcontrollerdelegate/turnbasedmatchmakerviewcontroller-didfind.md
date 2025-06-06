# turnBasedMatchmakerViewController(_:didFind:)

**Framework**: GameKit  
**Kind**: method

Handles when the view controller finds participants for a turn-based match.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFind match: GKTurnBasedMatch)
```

#### Discussion

When the participants accept their invitations to join a turn-based match, GameKit invokes this method in the game instances for all participants in the match, including the local player who initiates the match. Implement this method to dismiss the view controller and start gameplay that allows the local player to take their turn. Use the match object to show information about the other participants in the match.

## Parameters

- `viewController`: The view controller that finds participants for the match.
- `match`: The match that the participants join.

## See Also

- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, playerQuitFor: GKTurnBasedMatch)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:playerquitfor:).md)
  Handles when a player quits the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfind:))*