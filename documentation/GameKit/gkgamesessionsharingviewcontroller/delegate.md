# delegate

**Framework**: GameKit  
**Kind**: property

The delegate for the sharing view controller.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
weak var delegate: (any GKGameSessionSharingViewControllerDelegate)? { get set }
```

## See Also

- [protocol GKGameSessionSharingViewControllerDelegate](gkgamesessionsharingviewcontrollerdelegate.md)
  A protocol you implement to respond to changes to a sharing user interface.
- [var session: GKGameSession](gkgamesessionsharingviewcontroller/session.md)
  The game session associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/delegate)*