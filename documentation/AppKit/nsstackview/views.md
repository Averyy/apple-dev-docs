# views

**Framework**: AppKit  
**Kind**: property

The array of views owned by the stack view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var views: [NSView] { get }
```

#### Discussion

The `views` array always contains all of the views owned and managed by the stack view, regardless of their gravity area placement and regardless of whether or not they are attached. The index position of each view in the array matches the view ordering within the stack view. A detached view’s index position is its stack view position when attached.

## See Also

- [func views(in: NSStackView.Gravity) -> [NSView]](nsstackview/views(in:).md)
  Returns the array of views in the specified gravity area in the stack view.
- [var detachedViews: [NSView]](nsstackview/detachedviews.md)
  An array that contains the detached views from all the stack view’s gravity areas.
- [func clippingResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/clippingresistancepriority(for:).md)
  Returns the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func huggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsstackview/huggingpriority(for:).md)
  Returns the Auto Layout priority for the stack view to minimize its size to fit its contained views as closely as possible, for a specified user interface axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/views)*