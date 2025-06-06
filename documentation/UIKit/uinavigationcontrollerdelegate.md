# UINavigationControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for an object that serves as a navigation controller’s delegate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UINavigationControllerDelegate : NSObjectProtocol
```

#### Overview

Use a navigation controller delegate (a custom object that implements this protocol) to modify behavior when a view controller is pushed or popped from the navigation stack of a [`UINavigationController`](uinavigationcontroller.md) object.

## Topics

### Responding to a view controller being shown
- [func navigationController(UINavigationController, willShow: UIViewController, animated: Bool)](uinavigationcontrollerdelegate/navigationcontroller(_:willshow:animated:).md)
  Notifies the delegate before the navigation controller displays a view controller’s view and navigation item properties.
- [func navigationController(UINavigationController, didShow: UIViewController, animated: Bool)](uinavigationcontrollerdelegate/navigationcontroller(_:didshow:animated:).md)
  Notifies the delegate after the navigation controller displays a view controller’s view and navigation item properties.
### Supporting custom transition animations
- [func navigationController(UINavigationController, animationControllerFor: UINavigationController.Operation, from: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:).md)
  Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [func navigationController(UINavigationController, interactionControllerFor: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:).md)
  Allows the delegate to return an interactive animator object for use during view controller transitions.
- [func navigationControllerPreferredInterfaceOrientationForPresentation(UINavigationController) -> UIInterfaceOrientation](uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [func navigationControllerSupportedInterfaceOrientations(UINavigationController) -> UIInterfaceOrientationMask](uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.
### Constants
- [UINavigationController.Operation](uinavigationcontroller/operation.md)
  Constants that define the type of navigation controller transitions that can occur.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UINavigationControllerDelegate)?](uinavigationcontroller/delegate.md)
  The delegate of the navigation controller object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate)*