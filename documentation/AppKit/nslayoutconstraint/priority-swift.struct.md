# NSLayoutConstraint.Priority

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct Priority
```

```c
typedef float NSLayoutPriority;
```

## Topics

### Constants
- [static var required: NSLayoutConstraint.Priority](./priority-swift.struct/required.md)
  A required constraint.
- [static var defaultHigh: NSLayoutConstraint.Priority](./priority-swift.struct/defaulthigh.md)
  Priority level with which a button resists compressing its content.
- [static var dragThatCanResizeWindow: NSLayoutConstraint.Priority](./priority-swift.struct/dragthatcanresizewindow.md)
  Appropriate priority level for a drag that may end up resizing the window.
- [static var windowSizeStayPut: NSLayoutConstraint.Priority](./priority-swift.struct/windowsizestayput.md)
  Priority level for the window’s current size.
- [static var dragThatCannotResizeWindow: NSLayoutConstraint.Priority](./priority-swift.struct/dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static var defaultLow: NSLayoutConstraint.Priority](./priority-swift.struct/defaultlow.md)
  Priority level at which a button hugs its contents horizontally.
- [static var fittingSizeCompression: NSLayoutConstraint.Priority](./priority-swift.struct/fittingsizecompression.md)
  When you send a [`fittingSize`](../nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.
### Initializers
- [init(Float)](./priority-swift.struct/init%28_%29.md)
- [init(rawValue: Float)](./priority-swift.struct/init%28rawvalue%29.md)

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

### Getting the layout priority
- [var priority: NSLayoutConstraint.Priority](./priority-swift.property.md)
  The priority of the constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct)*