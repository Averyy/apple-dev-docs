# pageViewController(_:viewControllerBefore:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the view controller before the given view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController?
```

```objc
- (UIViewController *) pageViewController:(UIPageViewController *) pageViewController viewControllerBeforeViewController:(UIViewController *) viewController;
```

#### Return Value

The view controller before the given view controller, or `nil` to indicate that there is no previous view controller.

## Parameters

- `pageViewController`: The page view controller
- `viewController`: The view controller that the user navigated away from.

## See Also

### Providing View Controllers
- [func pageViewController(UIPageViewController, viewControllerAfter: UIViewController) -> UIViewController?](./pageviewcontroller%28_,viewcontrollerafter%29.md)
  Returns the view controller after the given view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/pageviewcontroller(_:viewcontrollerbefore:))*