# pageViewController(_:viewControllerAfter:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the view controller after the given view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pageViewController(_ pageViewController: UIPageViewController, viewControllerAfter viewController: UIViewController) -> UIViewController?
```

#### Return Value

The view controller after the given view controller, or `nil` to indicate that there is no next view controller.

## Parameters

- `pageViewController`: The page view controller
- `viewController`: The view controller that the user navigated away from.

## See Also

- [func pageViewController(UIPageViewController, viewControllerBefore: UIViewController) -> UIViewController?](uipageviewcontrollerdatasource/pageviewcontroller(_:viewcontrollerbefore:).md)
  Returns the view controller before the given view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/pageviewcontroller(_:viewcontrollerafter:))*