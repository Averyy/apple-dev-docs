# isDoubleSided

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether content appears on the back of pages.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isDoubleSided: Bool { get set }
```

#### Discussion

The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

If the back of pages has no content (the value is [`false`](https://developer.apple.com/documentation/swift/false)), then the content on the front of the page will partially show through to the back when turning pages.

If the spine is located in the middle, the value must be [`true`](https://developer.apple.com/documentation/swift/true). Setting it to [`false`](https://developer.apple.com/documentation/swift/false) with the spine located in the middle raises an exception.

## See Also

- [var navigationOrientation: UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [var spineLocation: UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.property.md)
  The location of the spine.
- [UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.enum.md)
  Locations for the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.enum.md)
  Styles for the page-turn transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/isdoublesided)*