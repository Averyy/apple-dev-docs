# show(from:animated:)

**Framework**: UIKit  
**Kind**: method

Displays an action sheet that originates from the specified bar button item.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func show(from item: UIBarButtonItem, animated: Bool)
```

#### Discussion

On iPad, this method presents the action sheet in a popover and adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## Parameters

- `item`: The bar button item from which the action sheet originates.
- `animated`: Specify   to animate the presentation of the action sheet or   to present it immediately without any animation effects.

## See Also

- [func show(from: UITabBar)](uiactionsheet/show(from:)-9i3tw.md)
  Displays an action sheet that originates from the specified tab bar.
- [func show(from: UIToolbar)](uiactionsheet/show(from:)-1p4ap.md)
  Displays an action sheet that originates from the specified toolbar.
- [func show(in: UIView)](uiactionsheet/show(in:).md)
  Displays an action sheet that originates from the specified view.
- [func show(from: CGRect, in: UIView, animated: Bool)](uiactionsheet/show(from:in:animated:).md)
  Displays an action sheet that originates from the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:animated:))*