# insertView(_:at:in:)

**Framework**: AppKit  
**Kind**: method

Adds a view to a stack view gravity area at a specified index position.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertView(_ view: NSView, at index: Int, in gravity: NSStackView.Gravity)
```

#### Discussion

Calling this method updates the stack view’s layout, which can change the stack view size. As a result, views could detach or clip according to the clipping resistance of the stack view and the visibility priorities of its views.

A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory. To respond to detachment and reattachment of views, implement an [`NSStackViewDelegate`](nsstackviewdelegate.md) object and assign it to the [`delegate`](nsstackview/delegate.md) property.

## Parameters

- `view`: The view to add to the specified gravity area.
- `index`: See the   property and the   method.
- `gravity`: The gravity area that you are adding the specified view to. Valid values are those in the   enumeration.

## See Also

- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/setclippingresistancepriority(_:for:).md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func addView(NSView, in: NSStackView.Gravity)](nsstackview/addview(_:in:).md)
  Adds a view to the end of the stack view gravity area.
- [func setViews([NSView], in: NSStackView.Gravity)](nsstackview/setviews(_:in:).md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [func removeView(NSView)](nsstackview/removeview(_:).md)
  Removes a specified view from the stack view.
- [NSStackView.Gravity](nsstackview/gravity.md)
  The gravity areas available in a stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/insertview(_:at:in:))*