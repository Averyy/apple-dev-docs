# matchmakerViewController(_:didFailWithError:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Handles when a view controller encounters an error while finding players for a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: any Error)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)

#### Discussion

This method needs to dismiss the view controller.

## Parameters

- `viewController`: The view controller that encounters an error.
- `error`: The error that occurs.

## See Also

- [func matchmakerViewControllerWasCancelled(GKMatchmakerViewController)](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontrollerwascancelled(_:).md)
  Handles when a player cancels a request to find players for a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfailwitherror:))*