# NSLayoutConstraint.Priority

**Framework**: AppKit  
**Kind**: struct

Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct Priority
```

## Topics

### Constants
- [static let required: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/required.md)
  A required constraint.
- [static let defaultHigh: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/defaulthigh.md)
  Priority level with which a button resists compressing its content.
- [static let dragThatCanResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcanresizewindow.md)
  Appropriate priority level for a drag that may end up resizing the window.
- [static let windowSizeStayPut: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/windowsizestayput.md)
  Priority level for the window’s current size.
- [static let dragThatCannotResizeWindow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/dragthatcannotresizewindow.md)
  Priority level at which a split view divider, say, is dragged.
- [static let defaultLow: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/defaultlow.md)
  Priority level at which a button hugs its contents horizontally.
- [static let fittingSizeCompression: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.struct/fittingsizecompression.md)
  When you send a [`fittingSize`](nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.
### Initializers
- [init(Float)](nslayoutconstraint/priority-swift.struct/init(_:).md)
- [init(rawValue: Float)](nslayoutconstraint/priority-swift.struct/init(rawvalue:).md)

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

- [var priority: NSLayoutConstraint.Priority](nslayoutconstraint/priority-swift.property.md)
  The priority of the constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct)*