# Edge

**Framework**: SwiftUI  
**Kind**: enum

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
- [Edge.top](edge/top.md)
- [Edge.bottom](edge/bottom.md)
- [Edge.leading](edge/leading.md)
- [Edge.trailing](edge/trailing.md)
### Creating an edge
- [init?(Edge3D)](edge/init(_:).md)
  Converts a 3D edge to a 2D edge, if possible.
### Accessing sets of edges
- [struct Set](edge/set.md)
  An efficient set of edges.
### Enumerations
- [Edge.Corner](edge/corner.md)
  An enumeration to indicate one corner of a rectangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [CaseIterable](../swift/caseiterable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum Edge3D](edge3d.md)
  An edge or face of a 3D volume.
- [enum HorizontalEdge](horizontaledge.md)
  An edge on the horizontal axis.
- [enum VerticalEdge](verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](edgeinsets.md)
  The inset distances for the sides of a rectangle.
- [struct EdgeInsets3D](edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edge)*