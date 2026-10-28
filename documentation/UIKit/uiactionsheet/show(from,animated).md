# show(from:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays an action sheet that originates from the specified bar button item.

**Availability**:
- iOS 3.2+ - Deprecated in 8.3
- iPadOS 3.2+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func show(from item: UIBarButtonItem, animated: Bool)
```

```objc
- (void) showFromBarButtonItem:(UIBarButtonItem *) item animated:(BOOL) animated;
```

## Discussion

On iPad, this method presents the action sheet in a popover and adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## Parameters

- `item`: The bar button item from which the action sheet originates.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the presentation of the action sheet or [`false`](../../Swift/false.md) to present it immediately without any animation effects.

## See Also

### Presenting the action sheet
- [func show(from: UITabBar)](./show%28from%29-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](./show%28from%29-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(in: UIView)](./show%28in%29.md)
  Displays an action sheet that originates from the specified view.
- [func show(from: CGRect, in: UIView, animated: Bool)](./show%28from,in,animated%29.md)
  Displays an action sheet that originates from the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:animated:))*