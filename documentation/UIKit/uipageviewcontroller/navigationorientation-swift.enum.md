# UIPageViewController.NavigationOrientation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Orientations for page-turn transitions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum NavigationOrientation
```

```c
enum UIPageViewControllerNavigationOrientation : NSInteger;
```

## Topics

### Constants
- [UIPageViewController.NavigationOrientation.horizontal](./navigationorientation-swift.enum/horizontal.md)
  Horizontal orientation, with pages turning left and right.
- [UIPageViewController.NavigationOrientation.vertical](./navigationorientation-swift.enum/vertical.md)
  Vertical orientation, with pages turning up and down.
### Initializers
- [init?(rawValue: Int)](./navigationorientation-swift.enum/init%28rawvalue%29.md)

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
- [var spineLocation: UIPageViewController.SpineLocation](./spinelocation-swift.property.md)
  The location of the spine.
- [UIPageViewController.SpineLocation](./spinelocation-swift.enum.md)
  Locations for the spine.
- [var transitionStyle: UIPageViewController.TransitionStyle](./transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](./transitionstyle-swift.enum.md)
  Styles for the page-turn transition.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that indicates whether content appears on the back of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationorientation-swift.enum)*