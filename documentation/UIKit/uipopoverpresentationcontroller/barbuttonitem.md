# barButtonItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bar button item on which to anchor the popover.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use the [`sourceItem`](./sourceitem.md) property to anchor the popover to a [`UIBarButtonItem`](../uibarbuttonitem.md) instead.

## Declaration

```swift
var barButtonItem: UIBarButtonItem? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIBarButtonItem * barButtonItem;
```

#### Discussion

Assign a value to this property to anchor the popover to the specified bar button item. When presented, the popover’s arrow points to the specified item. Alternatively, you may specify the anchor location for the popover using the [`sourceView`](./sourceview.md) and [`sourceRect`](./sourcerect.md) properties.

Prior to presentation, the presentation controller adds all sibling bar button items of the specified item (but not the item itself) to the popover’s list of passthrough views. UIKit automatically intercepts taps in the specified item and uses them to dismiss the popover. If you want taps in the other bar button items to dismiss the popover, you must add code to the action handlers of those items.

The default value of this property is `nil`.

## See Also

### Specifying the popover’s anchor point
- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](./sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](./sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var sourceRect: CGRect](./sourcerect.md)
  The area in the source view in which you anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/barbuttonitem)*