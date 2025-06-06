# show(from:)

**Framework**: UIKit  
**Kind**: method

Displays an action sheet that originates from the specified toolbar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func show(from view: UIToolbar)
```

#### Discussion

The appearance of the action sheet is animated.

On iPad, this method centers the action sheet in the middle of the screen. Generally, if you want to present an action sheet relative to a toolbar in an iPad application, you should use the [`show(from:animated:)`](uiactionsheet/show(from:animated:).md) method instead.

## Parameters

- `view`: The toolbar from which the action sheet originates.

## See Also

- [func show(from: UITabBar)](uiactionsheet/show(from:)-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(in: UIView)](uiactionsheet/show(in:).md)
  Displays an action sheet that originates from the specified view.
- [func show(from: UIBarButtonItem, animated: Bool)](uiactionsheet/show(from:animated:).md)
  Displays an action sheet that originates from the specified bar button item.
- [func show(from: CGRect, in: UIView, animated: Bool)](uiactionsheet/show(from:in:animated:).md)
  Displays an action sheet that originates from the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:)-1p4ap)*