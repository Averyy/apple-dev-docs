# sourceRect

**Framework**: UIKit  
**Kind**: property

The area in the source view in which you anchor the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceRect: CGRect { get set }
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

Use this property to define the rectangle that the popover’s arrow points to. The rectangle must be in the coordinate space of [`sourceView`](uipopoverpresentationcontroller/sourceview.md).

In iOS 13.2 and later, the default value is [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull), which instructs the system to use the current frame of [`sourceView`](uipopoverpresentationcontroller/sourceview.md). The controller observes changes to this frame and updates the popover accordingly.

In iOS 13.1 and earlier, the default value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGRect/zero) (Swift) or [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) (Objective-C); using [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull) results in undefined behavior.

[`UIPopoverPresentationController`](uipopoverpresentationcontroller.md) ignores this property if you set the [`barButtonItem`](uipopoverpresentationcontroller/barbuttonitem.md) property.

## See Also

- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](uipopoverpresentationcontroller/sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](uipopoverpresentationcontroller/sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var barButtonItem: UIBarButtonItem?](uipopoverpresentationcontroller/barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourcerect)*