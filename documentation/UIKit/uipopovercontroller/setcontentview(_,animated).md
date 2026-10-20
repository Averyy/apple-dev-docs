# setContentView(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the view controller responsible for the content portion of the popover.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
func setContentView(_ viewController: UIViewController, animated: Bool)
```

```objc
- (void) setContentViewController:(UIViewController *) viewController animated:(BOOL) animated;
```

## Parameters

- `viewController`: The new view controller whose content should be displayed by the popover.
- `animated`: Specify [`true`](../../Swift/true.md) if the change of view controllers should be animated or [`false`](../../Swift/false.md) if the change should occur immediately.

## See Also

### Configuring the popover content
- [var contentViewController: UIViewController](./contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](./contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](./setcontentsize%28_,animated%29.md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](./passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/setcontentview(_:animated:))*