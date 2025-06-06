# transitionStyle

**Framework**: UIKit  
**Kind**: property

The style used to transition between view controllers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var transitionStyle: UIPageViewController.TransitionStyle { get }
```

#### Discussion

The value of this property is set when the page view controller is initialized, and cannot be changed.

## See Also

- [var navigationOrientation: UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [var spineLocation: UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.property.md)
  The location of the spine.
- [UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.enum.md)
  Locations for the spine.
- [UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](uipageviewcontroller/isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle-swift.property)*