# removeView(_:)

**Framework**: AppKit  
**Kind**: method

Removes a specified view from the stack view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeView(_ view: NSView)
```

#### Discussion

This method removes a view from a stack view whether the view is attached or detached. For an attached view only, you can alternatively call the [`removeFromSuperview()`](https://developer.apple.com/documentation/UIKit/UIView/removeFromSuperview()) method on the view.

## Parameters

- `view`: The view you want to remove from the stack view.

## See Also

- [func addView(NSView, in: NSStackView.Gravity)](nsstackview/addview(_:in:).md)
  Adds a view to the end of the stack view gravity area.
- [func insertView(NSView, at: Int, in: NSStackView.Gravity)](nsstackview/insertview(_:at:in:).md)
  Adds a view to a stack view gravity area at a specified index position.
- [func setViews([NSView], in: NSStackView.Gravity)](nsstackview/setviews(_:in:).md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [NSStackView.Gravity](nsstackview/gravity.md)
  The gravity areas available in a stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/removeview(_:))*