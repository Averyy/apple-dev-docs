# interPageSpacing

**Framework**: UIKit  
**Kind**: property

Space between pages, in points.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let interPageSpacing: UIPageViewController.OptionsKey
```

#### Discussion

The value should be a [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) wrapped in an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). The default value is zero. An inter-page spacing is only valid if the transition style is [`UIPageViewController.TransitionStyle.scroll`](uipageviewcontroller/transitionstyle-swift.enum/scroll.md).

## See Also

- [static let spineLocation: UIPageViewController.OptionsKey](uipageviewcontroller/optionskey/spinelocation.md)
  Location of the spine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/interpagespacing)*