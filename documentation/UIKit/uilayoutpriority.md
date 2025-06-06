# UILayoutPriority

**Framework**: UIKit  
**Kind**: struct

The layout priority is used to indicate to the constraint-based layout system which constraints are more important, allowing the system to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UILayoutPriority
```

## Topics

### Constants
- [static let required: UILayoutPriority](uilayoutpriority/required.md)
  A required constraint.
- [static let defaultHigh: UILayoutPriority](uilayoutpriority/defaulthigh.md)
  The priority level with which a button resists compressing its content.
- [static let dragThatCanResizeScene: UILayoutPriority](uilayoutpriority/dragthatcanresizescene.md)
  The priority level for a drag that may end up resizing the window’s scene.
- [static let sceneSizeStayPut: UILayoutPriority](uilayoutpriority/scenesizestayput.md)
  The priority level at which the window’s scene prefers to stay the same size.
- [static let dragThatCannotResizeScene: UILayoutPriority](uilayoutpriority/dragthatcannotresizescene.md)
  The priority level for a drag that won’t resize the window’s scene.
- [static let defaultLow: UILayoutPriority](uilayoutpriority/defaultlow.md)
  The priority level at which a button hugs its contents horizontally.
- [static let fittingSizeLevel: UILayoutPriority](uilayoutpriority/fittingsizelevel.md)
  The priority level with which the view wants to conform to the target size in that computation.
### Initializers
- [init(Float)](uilayoutpriority/init(_:).md)
  Creates a layout priority structure.
- [init(rawValue: Float)](uilayoutpriority/init(rawvalue:).md)
  Creates a layout priority structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var priority: UILayoutPriority](nslayoutconstraint/priority.md)
  The priority of the constraint.
- [NSLayoutConstraint.Priority](../AppKit/NSLayoutConstraint/Priority-swift.struct.md)
  Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority)*