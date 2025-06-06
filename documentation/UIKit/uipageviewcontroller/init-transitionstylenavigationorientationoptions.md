# init(transitionStyle:navigationOrientation:options:)

**Framework**: UIKit  
**Kind**: init

Initializes a newly created page view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(transitionStyle style: UIPageViewController.TransitionStyle, navigationOrientation: UIPageViewController.NavigationOrientation, options: [UIPageViewController.OptionsKey : Any]? = nil)
```

#### Return Value

The initialized page view controller.

#### Discussion

After initialization, use the [`setViewControllers(_:direction:animated:completion:)`](uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:).md) method to set the initial view controllers.

## Parameters

- `style`: The style for transitions between pages.
- `navigationOrientation`: The orientation of the page-by-page navigation.
- `options`: A dictionary of options. For keys, see  .

## See Also

- [init?(coder: NSCoder)](uipageviewcontroller/init(coder:).md)
  Creates a page view controller from data in an unarchiver.
- [UIPageViewController.OptionsKey](uipageviewcontroller/optionskey.md)
  Keys for creating the page view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/init(transitionstyle:navigationorientation:options:))*