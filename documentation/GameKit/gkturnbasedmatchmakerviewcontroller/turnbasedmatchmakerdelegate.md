# turnBasedMatchmakerDelegate

**Framework**: GameKit  
**Kind**: property

The object that handles turn-based matchmaker view controller changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
weak var turnBasedMatchmakerDelegate: (any GKTurnBasedMatchmakerViewControllerDelegate)? { get set }
```

#### Discussion

You must set the delegate for GameKit to notify you when players cancel matchmaking or an error occurs.

## See Also

- [protocol GKTurnBasedMatchmakerViewControllerDelegate](gkturnbasedmatchmakerviewcontrollerdelegate.md)
  A protocol that handles when the status of turn-based matchmaking changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/turnbasedmatchmakerdelegate)*