# show(in:)

**Framework**: UIKit  
**Kind**: method

Displays an action sheet that originates from the specified view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func show(in view: UIView)
```

#### Discussion

The appearance of the action sheet is animated.

On iPad, this method centers the action sheet in the middle of the screen. Generally, if you want to present an action sheet in an iPad application, you should use the [`show(from:in:animated:)`](uiactionsheet/show(from:in:animated:).md) method to display the action sheet instead.

## Parameters

- `view`: The view from which the action sheet originates.

## See Also

- [func show(from: UITabBar)](uiactionsheet/show(from:)-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](uiactionsheet/show(from:)-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(from: UIBarButtonItem, animated: Bool)](uiactionsheet/show(from:animated:).md)
  Displays an action sheet that originates from the specified bar button item.
- [func show(from: CGRect, in: UIView, animated: Bool)](uiactionsheet/show(from:in:animated:).md)
  Displays an action sheet that originates from the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(in:))*