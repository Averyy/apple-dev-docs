# turnBasedMatchmakerViewControllerWasCancelled(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Handles when the player dismisses the view controller without inviting players.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController)
```

#### Discussion

This method needs to dismiss the view controller.

## Parameters

- `viewController`: The view controller that the player dismisses.

## See Also

- [func turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController, didFailWithError: any Error)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfailwitherror:).md)
  Handles when an error occurs while the local player invites other players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontrollerwascancelled(_:))*