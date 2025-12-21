# matchmakerDelegate

**Framework**: GameKit  
**Kind**: property

The object that handles matchmaker view controller changes.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var matchmakerDelegate: (any GKMatchmakerViewControllerDelegate)? { get set }
```

## Mentions

- [Finding players for custom server-based games](finding-players-for-custom-server-based-games.md)

#### Discussion

You must set the delegate for GameKit to notify you when players accept their invitations and you can start the game.

## See Also

- [protocol GKMatchmakerViewControllerDelegate](gkmatchmakerviewcontrollerdelegate.md)
  An object that handles when the status of matchmaking changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/matchmakerdelegate)*