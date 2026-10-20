# interPageSpacing

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Space between pages, in points.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let interPageSpacing: UIPageViewController.OptionsKey
```

```c
extern UIPageViewControllerOptionsKey const UIPageViewControllerOptionInterPageSpacingKey;
```

#### Discussion

The value should be a [`CGFloat`](../../../CoreFoundation/cgfloat-swift.struct.md) wrapped in an instance of [`NSNumber`](../../../Foundation/nsnumber.md). The default value is zero. An inter-page spacing is only valid if the transition style is [`UIPageViewController.TransitionStyle.scroll`](../transitionstyle-swift.enum/scroll.md).

## See Also

### Page options
- [static let spineLocation: UIPageViewController.OptionsKey](./spinelocation.md)
  Location of the spine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/interpagespacing)*