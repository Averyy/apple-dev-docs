# show(from:in:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays an action sheet that originates from the specified view.

**Availability**:
- iOS 3.2+ - Deprecated in 8.3
- iPadOS 3.2+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func show(from rect: CGRect, in view: UIView, animated: Bool)
```

```objc
- (void) showFromRect:(CGRect) rect inView:(UIView *) view animated:(BOOL) animated;
```

## Discussion

On iPad, this method displays the action sheet in a popover whose arrow points to the specified rectangle of the view. The popover does not overlap the specified rectangle.

## Parameters

- `rect`: The portion of `view` from which to originate the action sheet.
- `view`: The view from which to originate the action sheet.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the presentation of the action sheet or [`false`](../../Swift/false.md) to present it immediately without any animation effects.

## See Also

### Presenting the action sheet
- [func show(from: UITabBar)](./show%28from%29-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](./show%28from%29-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(in: UIView)](./show%28in%29.md)
  Displays an action sheet that originates from the specified view.
- [func show(from: UIBarButtonItem, animated: Bool)](./show%28from,animated%29.md)
  Displays an action sheet that originates from the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:in:animated:))*