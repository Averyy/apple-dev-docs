# navigationController(_:interactionControllerFor:)

**Framework**: UIKit  
**Kind**: method

Allows the delegate to return an interactive animator object for use during view controller transitions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationController(_ navigationController: UINavigationController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

#### Return Value

The animator object responsible for managing the transition animations, or `nil` if you want to use the standard navigation controller transitions. The object you return must conform to the [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) protocol.

#### Discussion

Implement this delegate method when you want to provide a custom, interactive transition between view controllers as they are added to or removed from the navigation stack. The object you return should configure the interactivity aspects of the transition and should work with the object in the `animationController` parameter to start the animations.

## Parameters

- `navigationController`: The navigation controller whose navigation stack is changing.
- `animationController`: The noninteractive animator object provided by the delegate’s   method.

## See Also

- [func navigationController(UINavigationController, animationControllerFor: UINavigationController.Operation, from: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uinavigationcontrollerdelegate/navigationcontroller(_:animationcontrollerfor:from:to:).md)
  Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [func navigationControllerPreferredInterfaceOrientationForPresentation(UINavigationController) -> UIInterfaceOrientation](uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [func navigationControllerSupportedInterfaceOrientations(UINavigationController) -> UIInterfaceOrientationMask](uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(_:).md)
  Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:))*