# show(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays an action sheet that originates from the specified toolbar.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
func show(from view: UIToolbar)
```

```objc
- (void) showFromToolbar:(UIToolbar *) view;
```

#### Discussion

The appearance of the action sheet is animated.

On iPad, this method centers the action sheet in the middle of the screen. Generally, if you want to present an action sheet relative to a toolbar in an iPad application, you should use the [`show(from:animated:)`](./show%28from,animated%29.md) method instead.

## Parameters

- `view`: The toolbar from which the action sheet originates.

## See Also

### Presenting the action sheet
- [func show(from: UITabBar)](./show%28from%29-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(in: UIView)](./show%28in%29.md)
  Displays an action sheet that originates from the specified view.
- [func show(from: UIBarButtonItem, animated: Bool)](./show%28from,animated%29.md)
  Displays an action sheet that originates from the specified bar button item.
- [func show(from: CGRect, in: UIView, animated: Bool)](./show%28from,in,animated%29.md)
  Displays an action sheet that originates from the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:)-1p4ap)*