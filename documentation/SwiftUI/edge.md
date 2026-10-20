# Edge

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

An enumeration to indicate one edge of a rectangle.

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
enum Edge
```

## Topics

### Getting the edges
- [Edge.top](./edge/top.md)
- [Edge.bottom](./edge/bottom.md)
- [Edge.leading](./edge/leading.md)
- [Edge.trailing](./edge/trailing.md)
### Creating an edge
- [init?(Edge3D)](./edge/init%28_%29.md)
  Converts a 3D edge to a 2D edge, if possible.
### Accessing sets of edges
- [struct Set](./edge/set.md)
  An efficient set of edges.
### Enumerations
- [Edge.Corner](./edge/corner.md)
  An enumeration to indicate one corner of a rectangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing edges, regions, and layouts
- [enum Edge3D](./edge3d.md)
  An edge or face of a 3D volume.
- [enum HorizontalEdge](./horizontaledge.md)
  An edge on the horizontal axis.
- [enum VerticalEdge](./verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](./edgeinsets.md)
  The inset distances for the sides of a rectangle.
- [struct EdgeInsets3D](./edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge)*