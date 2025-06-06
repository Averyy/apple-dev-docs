# matchmakerViewControllerWasCancelled(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Handles when a player cancels a request to find players for a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

This method needs to dismiss the view controller.

## Parameters

- `viewController`: The view controller that the player cancels.

## See Also

- [func matchmakerViewController(GKMatchmakerViewController, didFailWithError: any Error)](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfailwitherror:).md)
  Handles when a view controller encounters an error while finding players for a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontrollerwascancelled(_:))*