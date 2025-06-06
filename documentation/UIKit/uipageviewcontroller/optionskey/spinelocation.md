# spineLocation

**Framework**: UIKit  
**Kind**: property

Location of the spine.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static let spineLocation: UIPageViewController.OptionsKey
```

#### Discussion

For possible values, see [`UIPageViewController.SpineLocation`](uipageviewcontroller/spinelocation-swift.enum.md). A spine location is only valid if the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md).

If the transition style is [`UIPageViewController.TransitionStyle.pageCurl`](uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md), the default value for this property is [`UIPageViewController.SpineLocation.min`](uipageviewcontroller/spinelocation-swift.enum/min.md); otherwise, the default is [`UIPageViewController.SpineLocation.none`](uipageviewcontroller/spinelocation-swift.enum/none.md).

## See Also

- [static let interPageSpacing: UIPageViewController.OptionsKey](uipageviewcontroller/optionskey/interpagespacing.md)
  Space between pages, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/spinelocation)*