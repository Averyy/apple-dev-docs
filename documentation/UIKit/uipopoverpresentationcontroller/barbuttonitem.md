# barButtonItem

**Framework**: UIKit  
**Kind**: property

The bar button item on which to anchor the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barButtonItem: UIBarButtonItem? { get set }
```

#### Discussion

Assign a value to this property to anchor the popover to the specified bar button item. When presented, the popover’s arrow points to the specified item. Alternatively, you may specify the anchor location for the popover using the [`sourceView`](uipopoverpresentationcontroller/sourceview.md) and [`sourceRect`](uipopoverpresentationcontroller/sourcerect.md) properties.

Prior to presentation, the presentation controller adds all sibling bar button items of the specified item (but not the item itself) to the popover’s list of passthrough views. UIKit automatically intercepts taps in the specified item and uses them to dismiss the popover. If you want taps in the other bar button items to dismiss the popover, you must add code to the action handlers of those items.

The default value of this property is `nil`.

## See Also

- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](uipopoverpresentationcontroller/sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](uipopoverpresentationcontroller/sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var sourceRect: CGRect](uipopoverpresentationcontroller/sourcerect.md)
  The area in the source view in which you anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/barbuttonitem)*