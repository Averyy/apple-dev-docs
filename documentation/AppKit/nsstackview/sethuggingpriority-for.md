# setHuggingPriority(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func setHuggingPriority(_ huggingPriority: NSLayoutConstraint.Priority, for orientation: NSLayoutConstraint.Orientation)
```

#### Discussion

This method lets you specify a different hugging priority for each user interface axis. The default value for hugging priority, on both user interface axes, is [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md). If you have not added constraints between the stack view and its enclosing view, the stack view stays as small as possible to fully contain its views—independent of the size of the view that contains it.

To configure a stack view to grow and shrink according to the size of its enclosing view, add constraints between the stack view and its enclosing view by using Auto Layout priorities higher than the hugging priority.

To configure a stack view to prevent its enclosing view from growing, use priorities for the constraints between the stack view and its enclosing view that are lower than the hugging priority.

The value of the hugging priority also affects spacing between views and between gravity areas, as described in the discussion for the [`spacing`](nsstackview/spacing.md) property.

> **Note**:  The hugging priority for a stack view behaves differently than the content hugging priority for a generic view as configured with the [`NSView`](nsview.md) method [`setContentHuggingPriority(_:for:)`](nsview/setcontenthuggingpriority(_:for:).md). A stack view has no intrinsic content size and does not have a configurable content compression resistance. Calling the [`setContentCompressionResistancePriority(_:for:)`](nsview/setcontentcompressionresistancepriority(_:for:).md) method on a stack view has no effect.

 The hugging priority for a stack view behaves differently than the content hugging priority for a generic view as configured with the [`NSView`](nsview.md) method [`setContentHuggingPriority(_:for:)`](nsview/setcontenthuggingpriority(_:for:).md). A stack view has no intrinsic content size and does not have a configurable content compression resistance. Calling the [`setContentCompressionResistancePriority(_:for:)`](nsview/setcontentcompressionresistancepriority(_:for:).md) method on a stack view has no effect.

## Parameters

- `huggingPriority`: The Auto Layout priority for the stack view to minimize its size. The default value is  . Other valid values are those in the   enumeration.
- `orientation`: The horizontal or vertical user interface axis for which you’re setting the stack view’s hugging priority; one of the constants from the   enumeration.

## See Also

- [func huggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/huggingpriority(for:).md)
  Returns the Auto Layout priority for the stack view to minimize its size to fit its contained views as closely as possible, for a specified user interface axis.
- [var detachesHiddenViews: Bool](nsstackview/detacheshiddenviews.md)
  A Boolean value that indicates whether the stack view removes hidden views from its view hierarchy.
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/setclippingresistancepriority(_:for:).md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/sethuggingpriority(_:for:))*