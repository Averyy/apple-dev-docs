# setVisibilityPriority(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func setVisibilityPriority(_ priority: NSStackView.VisibilityPriority, for view: NSView)
```

#### Discussion

When Auto Layout reduces the stack view’s size (such as when a user reduces the size of the window containing the stack view), causing one or more views to no longer fit, the stack view detaches views in order of increasing . A view with lower visibility priority detaches before a view with higher visibility priority. A set of views with identical, detachable visibility priority are all detached or reattached together. A view with the highest possible visibility priority never detaches.

A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory.

The default visibility priority for a view is [`mustHold`](nsstackview/visibilitypriority/musthold.md), resulting in the view never detaching.

To allow a view to detach as needed by the stack view, set a visibility priority of [`detachOnlyIfNecessary`](nsstackview/visibilitypriority/detachonlyifnecessary.md). To force a view to detach regardless of the enclosing view’s size, set a visibility priority of [`notVisible`](nsstackview/visibilitypriority/notvisible.md). To explicitly reattach a view to a stack view, set a visibility priority of [`mustHold`](nsstackview/visibilitypriority/musthold.md).

## Parameters

- `priority`: The visibility priority for a specified view. Valid values are those in the   enumeration.
- `view`: The view whose visibility priority you are setting.

## See Also

- [func customSpacing(after: NSView) -> CGFloat](nsstackview/customspacing(after:).md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](nsstackview/setcustomspacing(_:after:).md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](nsstackview/visibilitypriority(for:).md)
  Returns the visibility priority for a specified view in the stack view.
- [NSStackView.VisibilityPriority](nsstackview/visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/setvisibilitypriority(_:for:))*