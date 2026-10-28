# sourceRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The area in the source view in which you anchor the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceRect: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect sourceRect;
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](../getting-the-user-s-attention-with-alerts-and-action-sheets.md)

## Discussion

Use this property to define the rectangle that the popover’s arrow points to. The rectangle must be in the coordinate space of [`sourceView`](./sourceview.md).

In iOS 13.2 and later, the default value is [`CGRectNull`](../../CoreGraphics/cgrectnull.md), which instructs the system to use the current frame of [`sourceView`](./sourceview.md). The controller observes changes to this frame and updates the popover accordingly.

In iOS 13.1 and earlier, the default value is [`zero`](../../CoreFoundation/cgrect/zero.md) (Swift) or [`CGRectZero`](../../CoreGraphics/cgrectzero.md) (Objective-C); using [`CGRectNull`](../../CoreGraphics/cgrectnull.md) results in undefined behavior.

[`UIPopoverPresentationController`](../uipopoverpresentationcontroller.md) ignores this property if you set the [`barButtonItem`](./barbuttonitem.md) property.

## See Also

### Specifying the popover’s anchor point
- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](./sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](../uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](./sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var barButtonItem: UIBarButtonItem?](./barbuttonitem.md)
  The bar button item on which to anchor the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourcerect)*