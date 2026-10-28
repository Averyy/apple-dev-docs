# transitionStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style used to transition between view controllers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var transitionStyle: UIPageViewController.TransitionStyle { get }
```

```objc
@property (nonatomic, readonly) UIPageViewControllerTransitionStyle transitionStyle;
```

## Discussion

The value of this property is set when the page view controller is initialized, and cannot be changed.

## See Also

### Display Options
- [var navigationOrientation: UIPageViewController.NavigationOrientation](./navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](./navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [var spineLocation: UIPageViewController.SpineLocation](./spinelocation-swift.property.md)
  The location of the spine.
- [UIPageViewController.SpineLocation](./spinelocation-swift.enum.md)
  Locations for the spine.
- [UIPageViewController.TransitionStyle](./transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle-swift.property)*