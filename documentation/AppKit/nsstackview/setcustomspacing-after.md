# setCustomSpacing(_:after:)

**Framework**: AppKit  
**Kind**: method

Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func setCustomSpacing(_ spacing: CGFloat, after view: NSView)
```

#### Discussion

For a horizontal stack view, this method sets custom spacing between a specified view and the view to its right when the user interface direction is left to right. (See the inherited [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) property for information on layout direction.) For a vertical stack view, this method sets custom spacing below a specified view.

If you set custom spacing for a view, it overrides the stack view’s default spacing for that view, as set in the [`spacing`](nsstackview/spacing.md) property.

A stack view retains custom spacing across layout updates. Custom spacing for a view is lost if you remove the view from the stack view or specify a new value.

## Parameters

- `spacing`: Default value is  , which indicates that the view does not use custom spacing.
- `view`: The view whose trailing spacing you are setting.

## See Also

- [var spacing: CGFloat](nsstackview/spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [func customSpacing(after: NSView) -> CGFloat](nsstackview/customspacing(after:).md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](nsstackview/visibilitypriority(for:).md)
  Returns the visibility priority for a specified view in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [NSStackView.VisibilityPriority](nsstackview/visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/setcustomspacing(_:after:))*