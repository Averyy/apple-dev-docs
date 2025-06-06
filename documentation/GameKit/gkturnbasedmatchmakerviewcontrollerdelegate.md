# GKTurnBasedMatchmakerViewControllerDelegate

**Framework**: GameKit  
**Kind**: protocol

A protocol that handles when the status of turn-based matchmaking changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKTurnBasedMatchmakerViewControllerDelegate : NSObjectProtocol
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Overview

To receive notifications when a player cancels turn-based matchmaking or an error occurs, implement this protocol in the [`GKTurnBasedMatchmakerViewController`](gkturnbasedmatchmakerviewcontroller.md) object’s delegate.

## Topics

### Handling Cancellation and Errors
- [func turnBasedMatchmakerViewControllerWasCancelled(GKTurnBasedMatchmakerViewController)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontrollerwascancelled(_:).md)
  Handles when the player dismisses the view controller without inviting players.
- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, didFailWithError: any Error)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfailwitherror:).md)
  Handles when an error occurs while the local player invites other players.
### Deprecated Methods
- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, didFind: GKTurnBasedMatch)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfind:).md)
  Handles when the view controller finds participants for a turn-based match.
- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, playerQuitFor: GKTurnBasedMatch)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:playerquitfor:).md)
  Handles when a player quits the match.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var turnBasedMatchmakerDelegate: (any GKTurnBasedMatchmakerViewControllerDelegate)?](gkturnbasedmatchmakerviewcontroller/turnbasedmatchmakerdelegate.md)
  The object that handles turn-based matchmaker view controller changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)*