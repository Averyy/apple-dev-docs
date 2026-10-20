# sourceView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view containing the anchor rectangle for the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * sourceView;
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](../getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

Use this property in conjunction with the [`sourceRect`](./sourcerect.md) property to specify the anchor location for the popover. Alternatively, you may specify the anchor location for the popover using the [`barButtonItem`](./barbuttonitem.md) property.

## See Also

### Specifying the popover’s anchor point
- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](./sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceRect: CGRect](./sourcerect.md)
  The area in the source view in which you anchor the popover.
- [var barButtonItem: UIBarButtonItem?](./barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceview)*