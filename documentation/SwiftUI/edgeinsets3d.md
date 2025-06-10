# EdgeInsets3D

**Framework**: SwiftUI  
**Kind**: struct

The inset distances for the faces of a 3D volume.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
struct EdgeInsets3D
```

## Topics

### Getting edge insets
- [var top: CGFloat](edgeinsets3d/top.md)
  The inset distance along the top face of a 3D volume.
- [var bottom: CGFloat](edgeinsets3d/bottom.md)
  The inset distance along the bottom face of a 3D volume.
- [var leading: CGFloat](edgeinsets3d/leading.md)
  The inset distance along the leading face of a 3D volume.
- [var trailing: CGFloat](edgeinsets3d/trailing.md)
  The inset distance along the top trailing of a 3D volume.
- [var front: CGFloat](edgeinsets3d/front.md)
  The inset distance along the top front of a 3D volume.
- [var back: CGFloat](edgeinsets3d/back.md)
  The inset distance along the top back of a 3D volume.
### Creating an edge inset
- [init(horizontal: CGFloat, vertical: CGFloat, depth: CGFloat)](edgeinsets3d/init(horizontal:vertical:depth:).md)
  Creates an `EdgeInsets3D` value with values provided for each axis.
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat, front: CGFloat, back: CGFloat)](edgeinsets3d/init(top:leading:bottom:trailing:front:back:).md)
  Creates an `EdgeInsets3D` value with values provided for each face.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Edge](edge.md)
  An enumeration to indicate one edge of a rectangle.
- [enum Edge3D](edge3d.md)
  An edge or face of a 3D volume.
- [enum HorizontalEdge](horizontaledge.md)
  An edge on the horizontal axis.
- [enum VerticalEdge](verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](edgeinsets.md)
  The inset distances for the sides of a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edgeinsets3d)*