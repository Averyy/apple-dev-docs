# navigationController(_:animationControllerFor:from:to:)

**Framework**: UIKit  
**Kind**: method

Allows the delegate to return a noninteractive animator object for use during view controller transitions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationController(_ navigationController: UINavigationController, animationControllerFor operation: UINavigationController.Operation, from fromVC: UIViewController, to toVC: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

#### Return Value

The animator object responsible for managing the transition animations, or `nil` if you want to use the standard navigation controller transitions. The object you return must conform to the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol.

#### Discussion

Implement this delegate method when you want to provide a custom animated transition between view controllers as they are added to or removed from the navigation stack. The object you return should be capable of configuring and performing noninteractive animations for the specified view controllers for the specified type of operation over a fixed period of time.

If you want to allow the user to perform interactive transitions, you must  implement the [`navigationController(_:interactionControllerFor:)`](uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:).md) method.

## Parameters

- `navigationController`: The navigation controller whose navigation stack is changing.
- `operation`: The type of transition operation that is occurring. For a list of possible values, see the   constants.
- `fromVC`: The currently visible view controller.
- `toVC`: The view controller that should be visible at the end of the transition.

## See Also

- [func navigationController(UINavigationController, interactionControllerFor: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:).md)
  Allows the delegate to return an interactive animator object for use during view controller transitions.
- [func navigationControllerPreferredInterfaceOrientationForPresentation(UINavigationController) -> UIInterfaceOrientation](uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [func navigationControllerSupportedInterfaceOrientations(UINavigationController) -> UIInterfaceOrientationMask](uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:))*