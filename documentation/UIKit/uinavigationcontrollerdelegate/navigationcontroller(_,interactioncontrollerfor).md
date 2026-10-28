# navigationController(_:interactionControllerFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to return an interactive animator object for use during view controller transitions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func navigationController(_ navigationController: UINavigationController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

```objc
- (id<UIViewControllerInteractiveTransitioning>) navigationController:(UINavigationController *) navigationController interactionControllerForAnimationController:(id<UIViewControllerAnimatedTransitioning>) animationController;
```

## Return Value

The animator object responsible for managing the transition animations, or `nil` if you want to use the standard navigation controller transitions. The object you return must conform to the [`UIViewControllerInteractiveTransitioning`](../uiviewcontrollerinteractivetransitioning.md) protocol.

## Discussion

Implement this delegate method when you want to provide a custom, interactive transition between view controllers as they are added to or removed from the navigation stack. The object you return should configure the interactivity aspects of the transition and should work with the object in the `animationController` parameter to start the animations.

## Parameters

- `navigationController`: The navigation controller whose navigation stack is changing.
- `animationController`: The noninteractive animator object provided by the delegate’s [`navigationController(_:animationControllerFor:from:to:)`](./navigationcontroller%28_,animationcontrollerfor,from,to%29.md) method.

## See Also

### Supporting custom transition animations
- [func navigationController(UINavigationController, animationControllerFor: UINavigationController.Operation, from: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](./navigationcontroller%28_,animationcontrollerfor,from,to%29.md)
  Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [func navigationControllerPreferredInterfaceOrientationForPresentation(UINavigationController) -> UIInterfaceOrientation](./navigationcontrollerpreferredinterfaceorientationforpresentation%28_%29.md)
  Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [func navigationControllerSupportedInterfaceOrientations(UINavigationController) -> UIInterfaceOrientationMask](./navigationcontrollersupportedinterfaceorientations%28_%29.md)
  Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate/navigationcontroller(_:interactioncontrollerfor:))*