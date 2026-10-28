# NSStackView.VisibilityPriority

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The various Auto Layout priorities for a view in the stack view to remain attached.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct VisibilityPriority
```

```c
typedef float NSStackViewVisibilityPriority;
```

## Discussion

For an explanation of how visibility priority interacts with clipping resistance to determine the detachment behavior of a stack view’s views, see the discussions for the [`setClippingResistancePriority(_:for:)`](./setclippingresistancepriority%28_,for%29.md) and [`setVisibilityPriority(_:for:)`](./setvisibilitypriority%28_,for%29.md) methods.

A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory.

## Topics

### Initializers
- [init(Float)](./visibilitypriority/init%28_%29.md)
- [init(rawValue: Float)](./visibilitypriority/init%28rawvalue%29.md)
### Priorities
- [static var mustHold: NSStackView.VisibilityPriority](./visibilitypriority/musthold.md)
  The default value, and maximum Auto Layout priority, that results in a view never detaching from the stack view.
- [static var detachOnlyIfNecessary: NSStackView.VisibilityPriority](./visibilitypriority/detachonlyifnecessary.md)
  The Auto Layout priority that results in detachment of a view when there is insufficient space in the stack view to display it fully.
- [static var notVisible: NSStackView.VisibilityPriority](./visibilitypriority/notvisible.md)
  The minimum Auto Layout priority that forces a view to detach from the stack view.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring Views in a Stack View
- [func customSpacing(after: NSView) -> CGFloat](./customspacing%28after%29.md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](./setcustomspacing%28_,after%29.md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func visibilityPriority(for: NSView) -> NSStackView.VisibilityPriority](./visibilitypriority%28for%29.md)
  Returns the visibility priority for a specified view in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](./setvisibilitypriority%28_,for%29.md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [class let useDefaultSpacing: CGFloat](./usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority)*