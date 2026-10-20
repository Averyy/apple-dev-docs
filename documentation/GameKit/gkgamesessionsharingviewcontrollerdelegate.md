# GKGameSessionSharingViewControllerDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

A protocol you implement to respond to changes to a sharing user interface.

**Availability**:
- tvOS 10.0+ - Deprecated in 12.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewControllerDelegate to receive notifications from the GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewControllerDelegate and GKLocalPlayerListener to receive notifications from the GKTurnBasedMatchmakerViewController.

## Declaration

```swift
protocol GKGameSessionSharingViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol GKGameSessionSharingViewControllerDelegate <NSObject>
```

## Topics

### Dismissing a Sharing View Controller
- [func sharingViewController(GKGameSessionSharingViewController, didFinishWithError: (any Error)?)](./gkgamesessionsharingviewcontrollerdelegate/sharingviewcontroller%28_,didfinishwitherror%29.md)
  Indicates the sharing view controller is ready to be dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing Share View Controller Properties
- [var delegate: (any GKGameSessionSharingViewControllerDelegate)?](./gkgamesessionsharingviewcontroller/delegate.md)
  The delegate for the sharing view controller.
- [var session: GKGameSession](./gkgamesessionsharingviewcontroller/session.md)
  The game session associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate)*