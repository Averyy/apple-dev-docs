# UIPageViewController.SpineLocation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Locations for the spine.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum SpineLocation
```

```c
enum UIPageViewControllerSpineLocation : NSInteger;
```

## Overview

To set the spine location, wrap one of these constants in an [`NSNumber`](../../Foundation/nsnumber.md) object and set it as the value for the [`spineLocation`](./optionskey/spinelocation.md) key in the options dictionary passed to the [`init(transitionStyle:navigationOrientation:options:)`](./init%28transitionstyle,navigationorientation,options%29.md) method.

## Topics

### Constants
- [UIPageViewController.SpineLocation.none](./spinelocation-swift.enum/none.md)
  No spine.
- [UIPageViewController.SpineLocation.min](./spinelocation-swift.enum/min.md)
  Spine at the left or top edge of the screen.
- [UIPageViewController.SpineLocation.mid](./spinelocation-swift.enum/mid.md)
  Spine in the middle or the screen.
- [UIPageViewController.SpineLocation.max](./spinelocation-swift.enum/max.md)
  Spine at the right or bottom edge of the screen.
### Initializers
- [init?(rawValue: Int)](./spinelocation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Display Options
- [var navigationOrientation: UIPageViewController.NavigationOrientation](./navigationorientation-swift.property.md)
  The direction along which navigation occurs.
- [UIPageViewController.NavigationOrientation](./navigationorientation-swift.enum.md)
  Orientations for page-turn transitions.
- [var spineLocation: UIPageViewController.SpineLocation](./spinelocation-swift.property.md)
  The location of the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](./transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](./transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.enum)*