# session

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The game session associated with the view controller.

**Availability**:
- tvOS 10.0+ - Deprecated in 12.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
var session: GKGameSession { get }
```

```objc
@property (nonatomic, strong, readonly) GKGameSession * session;
```

## See Also

### Accessing Share View Controller Properties
- [var delegate: (any GKGameSessionSharingViewControllerDelegate)?](./delegate.md)
  The delegate for the sharing view controller.
- [protocol GKGameSessionSharingViewControllerDelegate](../gkgamesessionsharingviewcontrollerdelegate.md)
  A protocol you implement to respond to changes to a sharing user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/session)*