# contentViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller responsible for the content portion of the popover.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
var contentViewController: UIViewController { get set }
```

```objc
@property (nonatomic, strong) UIViewController * contentViewController;
```

## Discussion

This property is initially set to the view controller passed to the [`init(contentViewController:)`](./init%28contentviewcontroller%29.md) method. You can change the value of this property later to reflect a new set of content. Changing the value of this property swaps the new view controller in for the old one immediately and does not trigger an animation. If you want to animate the change, use the [`setContentView(_:animated:)`](./setcontentview%28_,animated%29.md) method instead.

## See Also

### Configuring the popover content
- [func setContentView(UIViewController, animated: Bool)](./setcontentview%28_,animated%29.md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](./contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](./setcontentsize%28_,animated%29.md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](./passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/contentviewcontroller)*