# sourceView

**Framework**: UIKit  
**Kind**: property

The view containing the anchor rectangle for the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceView: UIView? { get set }
```

#### Discussion

Use this property in conjunction with the [`sourceRect`](uipopoverpresentationcontroller/sourcerect.md) property to specify the anchor location for the popover. Alternatively, you may specify the anchor location for the popover using the [`barButtonItem`](uipopoverpresentationcontroller/barbuttonitem.md) property.

## See Also

- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](uipopoverpresentationcontroller/sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceRect: CGRect](uipopoverpresentationcontroller/sourcerect.md)
  The area in the source view in which you anchor the popover.
- [var barButtonItem: UIBarButtonItem?](uipopoverpresentationcontroller/barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceview)*