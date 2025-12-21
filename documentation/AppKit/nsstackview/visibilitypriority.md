# NSStackView.VisibilityPriority

**Framework**: AppKit  
**Kind**: struct

The various Auto Layout priorities for a view in the stack view to remain attached.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct VisibilityPriority
```

#### Discussion

For an explanation of how visibility priority interacts with clipping resistance to determine the detachment behavior of a stack view’s views, see the discussions for the [`setClippingResistancePriority(_:for:)`](nsstackview/setclippingresistancepriority(_:for:).md) and [`setVisibilityPriority(_:for:)`](nsstackview/setvisibilitypriority(_:for:).md) methods.

A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory.

## Topics

### Initializers
- [init(Float)](nsstackview/visibilitypriority/init(_:).md)
- [init(rawValue: Float)](nsstackview/visibilitypriority/init(rawvalue:).md)
### Priorities
- [static let mustHold: NSStackView.VisibilityPriority](nsstackview/visibilitypriority/musthold.md)
  The default value, and maximum Auto Layout priority, that results in a view never detaching from the stack view.
- [static let detachOnlyIfNecessary: NSStackView.VisibilityPriority](nsstackview/visibilitypriority/detachonlyifnecessary.md)
  The Auto Layout priority that results in detachment of a view when there is insufficient space in the stack view to display it fully.
- [static let notVisible: NSStackView.VisibilityPriority](nsstackview/visibilitypriority/notvisible.md)
  The minimum Auto Layout priority that forces a view to detach from the stack view.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func customSpacing(after: NSView) -> CGFloat](nsstackview/customspacing(after:).md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](nsstackview/setcustomspacing(_:after:).md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](nsstackview/visibilitypriority(for:).md)
  Returns the visibility priority for a specified view in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](nsstackview/setvisibilitypriority(_:for:).md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority)*