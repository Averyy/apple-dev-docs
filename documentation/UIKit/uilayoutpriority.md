# UILayoutPriority

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The layout priority is used to indicate to the constraint-based layout system which constraints are more important, allowing the system to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct UILayoutPriority
```

```c
typedef float UILayoutPriority;
```

## Topics

### Constants
- [static var required: UILayoutPriority](./uilayoutpriority/required.md)
  A required constraint.
- [static var defaultHigh: UILayoutPriority](./uilayoutpriority/defaulthigh.md)
  The priority level with which a button resists compressing its content.
- [static var dragThatCanResizeScene: UILayoutPriority](./uilayoutpriority/dragthatcanresizescene.md)
  The priority level for a drag that may end up resizing the window’s scene.
- [static var sceneSizeStayPut: UILayoutPriority](./uilayoutpriority/scenesizestayput.md)
  The priority level at which the window’s scene prefers to stay the same size.
- [static var dragThatCannotResizeScene: UILayoutPriority](./uilayoutpriority/dragthatcannotresizescene.md)
  The priority level for a drag that won’t resize the window’s scene.
- [static var defaultLow: UILayoutPriority](./uilayoutpriority/defaultlow.md)
  The priority level at which a button hugs its contents horizontally.
- [static var fittingSizeLevel: UILayoutPriority](./uilayoutpriority/fittingsizelevel.md)
  The priority level with which the view wants to conform to the target size in that computation.
### Initializers
- [init(Float)](./uilayoutpriority/init%28_%29.md)
  Creates a layout priority structure.
- [init(rawValue: Float)](./uilayoutpriority/init%28rawvalue%29.md)
  Creates a layout priority structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the layout priority
- [var priority: UILayoutPriority](./nslayoutconstraint/priority.md)
  The priority of the constraint.
- [NSLayoutConstraint.Priority](../AppKit/nslayoutconstraint/priority-swift.struct.md)
  Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority)*