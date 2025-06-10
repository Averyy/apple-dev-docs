# DepthAlignment

**Framework**: SwiftUI  
**Kind**: struct

An alignment position along the depth axis.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
struct DepthAlignment
```

## Topics

### Getting guides
- [static let back: DepthAlignment](depthalignment/back.md)
  A guide marking the bottom edge of the view.
- [static let center: DepthAlignment](depthalignment/center.md)
  A guide marking the vertical center of the view.
- [static let front: DepthAlignment](depthalignment/front.md)
  A guide marking the top edge of the view.
### Initializers
- [init(any DepthAlignmentID.Type)](depthalignment/init(_:).md)
### Instance Methods
- [func combineExplicit<S>(S) -> CGFloat?](depthalignment/combineexplicit(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
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
- [protocol AlignmentID](alignmentid.md)
  A type that you use to create custom alignment guides.
- [struct ViewDimensions](viewdimensions.md)
  A view’s size and alignment guides in its own coordinate space.
- [struct ViewDimensions3D](viewdimensions3d.md)
  A view’s 3D size and alignment guides in its own coordinate space.
- [struct SpatialContainer](spatialcontainer.md)
  A layout container that aligns overlapping content in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/depthalignment)*