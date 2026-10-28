# isDoubleSided

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether content appears on the back of pages.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isDoubleSided: Bool { get set }
```

```objc
@property (nonatomic, getter=isDoubleSided) BOOL doubleSided;
```

## Discussion

The default value for this property is [`false`](../../Swift/false.md).

If the back of pages has no content (the value is [`false`](../../Swift/false.md)), then the content on the front of the page will partially show through to the back when turning pages.

If the spine is located in the middle, the value must be [`true`](../../Swift/true.md). Setting it to [`false`](../../Swift/false.md) with the spine located in the middle raises an exception.

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
- [var transitionStyle: UIPageViewController.TransitionStyle](./transitionstyle-swift.property.md)
  The style used to transition between view controllers.
- [UIPageViewController.TransitionStyle](./transitionstyle-swift.enum.md)
  Styles for the page-turn transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/isdoublesided)*