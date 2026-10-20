# spineLocation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The location of the spine.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var spineLocation: UIPageViewController.SpineLocation { get }
```

```objc
@property (nonatomic, readonly) UIPageViewControllerSpineLocation spineLocation;
```

#### Discussion

The value of this property is set with the [`spineLocation`](./optionskey/spinelocation.md) key when the page view controller is initialized, and can be changed by returning the new value from the [`pageViewController(_:spineLocationFor:)`](../uipageviewcontrollerdelegate/pageviewcontroller%28_,spinelocationfor%29.md) method of the delegate.

## See Also

### Display Options
- [var navigationOrientation: UIPageViewController.NavigationOrientation](./navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](./navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [UIPageViewController.SpineLocation](./spinelocation-swift.enum.md)
  Locations for the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](./transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](./transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.property)*