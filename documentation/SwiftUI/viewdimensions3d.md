# ViewDimensions3D

**Framework**: SwiftUI  
**Kind**: struct

A view’s 3D size and alignment guides in its own coordinate space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ViewDimensions3D
```

## Topics

### Instance Properties
- [var depth: CGFloat](viewdimensions3d/depth.md)
  The view’s depth.
- [var height: CGFloat](viewdimensions3d/height.md)
  The view’s height.
- [var width: CGFloat](viewdimensions3d/width.md)
  The view’s width.
### Subscripts
- [subscript(_:)](viewdimensions3d/subscript(_:).md)
  Gets the value of the given depth guide.
- [subscript(explicit:)](viewdimensions3d/subscript(explicit:).md)
  Gets the explicit value of the given depth alignment guide

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

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
- [struct SpatialContainer](spatialcontainer.md)
  A layout container that aligns overlapping content in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewdimensions3d)*