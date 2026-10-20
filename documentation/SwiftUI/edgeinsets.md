# EdgeInsets

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The inset distances for the sides of a rectangle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct EdgeInsets
```

## Topics

### Getting edge insets
- [var top: CGFloat](./edgeinsets/top.md)
- [var bottom: CGFloat](./edgeinsets/bottom.md)
- [var leading: CGFloat](./edgeinsets/leading.md)
- [var trailing: CGFloat](./edgeinsets/trailing.md)
### Creating an edge inset
- [init()](./edgeinsets/init%28%29.md)
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](./edgeinsets/init%28top,leading,bottom,trailing%29.md)
- [init(_:)](./edgeinsets/init%28_%29.md)
  Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and `back` values.
### Instance Methods
- [func inset(by: RectangleCornerInsets, edges: Edge.Set) -> EdgeInsets](./edgeinsets/inset%28by,edges%29.md)
  Returns an inset that has been modified by the corner sizes in the specified edges. When two corner insets diverge in their values for the specified edge, the maximum inset value will be used. For example, when the top edge is specified, the top inset will be adjusted by the larger of the two heights from the top leading and trailing corner inset sizes.

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing edges, regions, and layouts
- [enum Edge](./edge.md)
  An enumeration to indicate one edge of a rectangle.
- [enum Edge3D](./edge3d.md)
  An edge or face of a 3D volume.
- [enum HorizontalEdge](./horizontaledge.md)
  An edge on the horizontal axis.
- [enum VerticalEdge](./verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets3D](./edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edgeinsets)*