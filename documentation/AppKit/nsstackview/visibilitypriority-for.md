# visibilityPriority(for:)

**Framework**: AppKit  
**Kind**: method

Returns the visibility priority for a specified view in the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func visibilityPriority(for view: NSView) -> NSStackView.VisibilityPriority
```

#### Return Value

The visibility priority for the specified view.

#### Discussion

Visibility priority is the Auto Layout priority for a view to remain attached to a stack view when Auto Layout reduces the stack view’s size (such as when a user reduces the enclosing window’s size).

## Parameters

- `view`: The view that you are getting the visibility priority for.

## See Also

- [func customSpacing(after: NSView) -> CGFloat](nsstackview/customspacing(after:).md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](nsstackview/setcustomspacing(_:after:).md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [NSStackView.VisibilityPriority](nsstackview/visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority(for:))*