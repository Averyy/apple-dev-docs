# delegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the sharing view controller.

**Availability**:
- tvOS 10.0+ - Deprecated in 12.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
weak var delegate: (any GKGameSessionSharingViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<GKGameSessionSharingViewControllerDelegate> delegate;
```

## See Also

### Accessing Share View Controller Properties
- [protocol GKGameSessionSharingViewControllerDelegate](../gkgamesessionsharingviewcontrollerdelegate.md)
  A protocol you implement to respond to changes to a sharing user interface.
- [var session: GKGameSession](./session.md)
  The game session associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/delegate)*