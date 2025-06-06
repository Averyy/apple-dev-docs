# GKGameSessionSharingViewControllerDelegate

**Framework**: GameKit  
**Kind**: protocol

A protocol you implement to respond to changes to a sharing user interface.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
protocol GKGameSessionSharingViewControllerDelegate : NSObjectProtocol
```

## Topics

### Dismissing a Sharing View Controller
- [func sharingViewController(GKGameSessionSharingViewController, didFinishWithError: (any Error)?)](gkgamesessionsharingviewcontrollerdelegate/sharingviewcontroller(_:didfinishwitherror:).md)
  Indicates the sharing view controller is ready to be dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any GKGameSessionSharingViewControllerDelegate)?](gkgamesessionsharingviewcontroller/delegate.md)
  The delegate for the sharing view controller.
- [var session: GKGameSession](gkgamesessionsharingviewcontroller/session.md)
  The game session associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate)*