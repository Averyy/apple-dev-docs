# show(from:in:animated:)

**Framework**: UIKit  
**Kind**: method

Displays an action sheet that originates from the specified view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func show(from rect: CGRect, in view: UIView, animated: Bool)
```

#### Discussion

On iPad, this method displays the action sheet in a popover whose arrow points to the specified rectangle of the view. The popover does not overlap the specified rectangle.

## Parameters

- `rect`: The portion of   from which to originate the action sheet.
- `view`: The view from which to originate the action sheet.
- `animated`: Specify   to animate the presentation of the action sheet or   to present it immediately without any animation effects.

## See Also

- [func show(from: UITabBar)](uiactionsheet/show(from:)-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](uiactionsheet/show(from:)-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(in: UIView)](uiactionsheet/show(in:).md)
  Displays an action sheet that originates from the specified view.
- [func show(from: UIBarButtonItem, animated: Bool)](uiactionsheet/show(from:animated:).md)
  Displays an action sheet that originates from the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:in:animated:))*