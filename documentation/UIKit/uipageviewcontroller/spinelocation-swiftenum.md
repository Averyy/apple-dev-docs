# UIPageViewController.SpineLocation

**Framework**: UIKit  
**Kind**: enum

Locations for the spine.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum SpineLocation
```

#### Overview

To set the spine location, wrap one of these constants in an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object and set it as the value for the [`spineLocation`](uipageviewcontroller/optionskey/spinelocation.md) key in the options dictionary passed to the [`init(transitionStyle:navigationOrientation:options:)`](uipageviewcontroller/init(transitionstyle:navigationorientation:options:).md) method.

## Topics

### Constants
- [UIPageViewController.SpineLocation.none](uipageviewcontroller/spinelocation-swift.enum/none.md)
  No spine.
- [UIPageViewController.SpineLocation.min](uipageviewcontroller/spinelocation-swift.enum/min.md)
  Spine at the left or top edge of the screen.
- [UIPageViewController.SpineLocation.mid](uipageviewcontroller/spinelocation-swift.enum/mid.md)
  Spine in the middle or the screen.
- [UIPageViewController.SpineLocation.max](uipageviewcontroller/spinelocation-swift.enum/max.md)
  Spine at the right or bottom edge of the screen.
### Initializers
- [init?(rawValue: Int)](uipageviewcontroller/spinelocation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var navigationOrientation: UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](uipageviewcontroller/navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [var spineLocation: UIPageViewController.SpineLocation](uipageviewcontroller/spinelocation-swift.property.md)
  The location of the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](uipageviewcontroller/transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](uipageviewcontroller/isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.enum)*