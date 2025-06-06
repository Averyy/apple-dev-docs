# customSpacing(after:)

**Framework**: AppKit  
**Kind**: method

Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func customSpacing(after view: NSView) -> CGFloat
```

#### Return Value

The number of points between the trailing edge of the specified view and the one that follows it (that is, the one with the next highest index order).

#### Discussion

If you set custom spacing for a view using the [`setCustomSpacing(_:after:)`](nsstackview/setcustomspacing(_:after:).md) method, it overrides the stack view’s default spacing as set in the [`spacing`](nsstackview/spacing.md) property.

A stack view retains custom spacing across layout updates. Custom spacing for a view is lost if you remove the view from the stack view or specify a new value.

## Parameters

- `view`: The view whose trailing spacing you are getting.

## See Also

- [func setCustomSpacing(CGFloat, after: NSView)](nsstackview/setcustomspacing(_:after:).md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](nsstackview/visibilitypriority(for:).md)
  Returns the visibility priority for a specified view in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [NSStackView.VisibilityPriority](nsstackview/visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/customspacing(after:))*