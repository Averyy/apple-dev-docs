# spineLocation

**Framework**: UIKit  
**Kind**: property

The location of the spine.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var spineLocation: UIPageViewController.SpineLocation { get }
```

#### Discussion

The value of this property is set with the [`spineLocation`](uipageviewcontroller/optionskey/spinelocation.md) key when the page view controller is initialized, and can be changed by returning the new value from the [`pageViewController(_:spineLocationFor:)`](uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:).md) method of the delegate.

## See Also

- [var navigationOrientation: UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.enum.md)
  Locations for the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](uipageviewcontroller/isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.property)*