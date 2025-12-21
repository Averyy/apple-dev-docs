# sourceItem

**Framework**: UIKit  
**Kind**: property

The item on which to anchor the popover.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceItem: (any UIPopoverPresentationControllerSourceItem)? { get set }
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

Assign a value to this property to anchor the popover to the specified [`UIBarButtonItem`](uibarbuttonitem.md) or [`NSToolbarItem`](https://developer.apple.com/documentation/AppKit/NSToolbarItem). In iOS 18 and earlier, the popover’s arrow points to the specified item. In iOS 26 and later, the popover animates from and replaces the specified item until someone selects an action item or dismisses the popover.

Alternatively, you may specify the anchor location for the popover using the [`sourceView`](uipopoverpresentationcontroller/sourceview.md) and [`sourceRect`](uipopoverpresentationcontroller/sourcerect.md) properties.

The default value of this property is `nil`.

## See Also

- [protocol UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](uipopoverpresentationcontroller/sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var sourceRect: CGRect](uipopoverpresentationcontroller/sourcerect.md)
  The area in the source view in which you anchor the popover.
- [var barButtonItem: UIBarButtonItem?](uipopoverpresentationcontroller/barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceitem)*