# clippingResistancePriority(for:)

**Framework**: AppKit  
**Kind**: method

Returns the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func clippingResistancePriority(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority
```

#### Return Value

A layout constraint priority that identifies the clipping resistance for the stack view.

#### Discussion

For an explanation of clipping resistance and how to use it for a stack view, see the [`setClippingResistancePriority(_:for:)`](nsstackview/setclippingresistancepriority(_:for:).md) method.

## Parameters

- `orientation`: The stack view layout direction to which the clipping resistance priority applies.

## See Also

- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/setclippingresistancepriority(_:for:).md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [var views: [NSView]](nsstackview/views.md)
  The array of views owned by the stack view.
- [func views(in: NSStackView.Gravity) -> [NSView]](nsstackview/views(in:).md)
  Returns the array of views in the specified gravity area in the stack view.
- [var detachedViews: [NSView]](nsstackview/detachedviews.md)
  An array that contains the detached views from all the stack view’s gravity areas.
- [func huggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/huggingpriority(for:).md)
  Returns the Auto Layout priority for the stack view to minimize its size to fit its contained views as closely as possible, for a specified user interface axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/clippingresistancepriority(for:))*