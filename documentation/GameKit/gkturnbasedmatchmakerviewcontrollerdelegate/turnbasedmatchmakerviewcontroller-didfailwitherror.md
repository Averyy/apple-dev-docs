# turnBasedMatchmakerViewController(_:didFailWithError:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Handles when an error occurs while the local player invites other players.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: any Error)
```

#### Discussion

This method needs to dismiss the view controller.

## Parameters

- `viewController`: The view controller that encounters an error.
- `error`: The error that occurs.

## See Also

- [func turnBasedMatchmakerViewControllerWasCancelled(GKTurnBasedMatchmakerViewController)](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontrollerwascancelled(_:).md)
  Handles when the player dismisses the view controller without inviting players.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfailwitherror:))*