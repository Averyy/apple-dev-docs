# spineLocation

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Location of the spine.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
static let spineLocation: UIPageViewController.OptionsKey
```

```c
extern UIPageViewControllerOptionsKey const UIPageViewControllerOptionSpineLocationKey;
```

#### Discussion

For possible values, see [`UIPageViewController.SpineLocation`](../spinelocation-swift.enum.md). A spine location is only valid if the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](../transitionstyle-swift.enum/pagecurl.md).

If the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](../transitionstyle-swift.enum/pagecurl.md), the default value for this property is [`UIPageViewController.SpineLocation.min`](../spinelocation-swift.enum/min.md); otherwise, the default is [`UIPageViewController.SpineLocation.none`](../spinelocation-swift.enum/none.md).

## See Also

### Page options
- [static let interPageSpacing: UIPageViewController.OptionsKey](./interpagespacing.md)
  Space between pages, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/spinelocation)*