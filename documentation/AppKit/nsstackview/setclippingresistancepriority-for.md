# setClippingResistancePriority(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func setClippingResistancePriority(_ clippingResistancePriority: NSLayoutConstraint.Priority, for orientation: NSLayoutConstraint.Orientation)
```

#### Discussion

A clipped view is one that is partially hidden beyond the border of its enclosing stack view. When Auto Layout attempts to reduce the stack view’s size (such as when a user attempts to reduce the size of the enclosing window), causing a view to no longer fit, the stack view clips or detaches the view, or else prevents further reduction of the stack view’s size.

To allow view clipping, set a clipping resistance lower than the default value of NSLayoutPriorityRequired and set the visibility priority of all the stack view’s views to [`mustHold`](nsstackview/visibilitypriority/musthold.md).

To ensure that views detach rather than clip, lower the clipping resistance for the stack view to a value less than the default of NSLayoutPriorityRequired and set the visibility priority for at least one view to a value less than [`mustHold`](nsstackview/visibilitypriority/musthold.md).

If you disallow view clipping and disallow view detachment, which is the default behavior for a stack view, Auto Layout prevents the stack view from being reduced in size beyond the minimum needed to show all of its views.

Clipping begins from the right and bottom sides of a stack view.

## Parameters

- `clippingResistancePriority`: The clipping resistance Auto Layout priority you want to apply to the stack view for a given user interface axis. The default value is NSLayoutPriorityRequired, which disallows clipping. Other valid values are those in the   enumeration.
- `orientation`: The horizontal or vertical user interface axis that the clipping resistance priority applies to; one of the constants from the   enumeration.

## See Also

- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [func clippingResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/clippingresistancepriority(for:).md)
  Returns the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [var detachesHiddenViews: Bool](nsstackview/detacheshiddenviews.md)
  A Boolean value that indicates whether the stack view removes hidden views from its view hierarchy.
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/sethuggingpriority(_:for:).md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/setclippingresistancepriority(_:for:))*