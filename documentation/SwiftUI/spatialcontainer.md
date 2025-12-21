# SpatialContainer

**Framework**: SwiftUI  
**Kind**: struct

A layout container that aligns overlapping content in 3D space.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@frozen
struct SpatialContainer
```

#### Overview

The container will take the max size of each dimension of each of its children, aligning its children based on the `alignment`.

## Topics

### Initializers
- [init(alignment: Alignment3D)](spatialcontainer/init(alignment:).md)
  Creates a spatial container layout with the specified 3D alignment.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [Layout](layout.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Aligning views within a stack](aligning-views-within-a-stack.md)
  Position views inside a stack using alignment guides.
- [Aligning views across stacks](aligning-views-across-stacks.md)
  Create a custom alignment and use it to align views across multiple stacks.
- [func alignmentGuide(_:computeValue:)](view/alignmentguide(_:computevalue:).md)
  Sets the view’s horizontal alignment.
- [struct Alignment](alignment.md)
  An alignment in both axes.
- [struct HorizontalAlignment](horizontalalignment.md)
  An alignment position along the horizontal axis.
- [struct VerticalAlignment](verticalalignment.md)
  An alignment position along the vertical axis.
- [struct DepthAlignment](depthalignment.md)
  An alignment position along the depth axis.
- [protocol AlignmentID](alignmentid.md)
  A type that you use to create custom alignment guides.
- [struct ViewDimensions](viewdimensions.md)
  A view’s size and alignment guides in its own coordinate space.
- [struct ViewDimensions3D](viewdimensions3d.md)
  A view’s 3D size and alignment guides in its own coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialcontainer)*