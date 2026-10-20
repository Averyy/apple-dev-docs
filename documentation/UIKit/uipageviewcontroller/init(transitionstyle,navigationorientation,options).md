# init(transitionStyle:navigationOrientation:options:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly created page view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(transitionStyle style: UIPageViewController.TransitionStyle, navigationOrientation: UIPageViewController.NavigationOrientation, options: [UIPageViewController.OptionsKey : Any]? = nil)
```

```objc
- (instancetype) initWithTransitionStyle:(UIPageViewControllerTransitionStyle) style navigationOrientation:(UIPageViewControllerNavigationOrientation) navigationOrientation options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

The initialized page view controller.

#### Discussion

After initialization, use the [`setViewControllers(_:direction:animated:completion:)`](./setviewcontrollers%28_,direction,animated,completion%29.md) method to set the initial view controllers.

## Parameters

- `style`: The style for transitions between pages.
- `navigationOrientation`: The orientation of the page-by-page navigation.
- `options`: A dictionary of options. For keys, see [`UIPageViewController.OptionsKey`](./optionskey.md).

## See Also

### Creating a page view controller
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a page view controller from data in an unarchiver.
- [UIPageViewController.OptionsKey](./optionskey.md)
  Keys for creating the page view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/init(transitionstyle:navigationorientation:options:))*