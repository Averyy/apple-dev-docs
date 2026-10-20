# HorizontalEdge

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

An edge on the horizontal axis.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum HorizontalEdge
```

#### Overview

Use a horizontal edge for tasks like setting a swipe action with the [`swipeActions(edge:allowsFullSwipe:content:)`](./view/swipeactions%28edge,allowsfullswipe,content%29.md) view modifier. The positions of the leading and trailing edges depend on the locale chosen by the user.

## Topics

### Getting the edges
- [HorizontalEdge.leading](./horizontaledge/leading.md)
  The leading edge.
- [HorizontalEdge.trailing](./horizontaledge/trailing.md)
  The trailing edge.
### Accessing sets of edges
- [HorizontalEdge.Set](./horizontaledge/set.md)
  An efficient set of horizontal edges.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing edges, regions, and layouts
- [enum Edge](./edge.md)
  An enumeration to indicate one edge of a rectangle.
- [enum Edge3D](./edge3d.md)
  An edge or face of a 3D volume.
- [enum VerticalEdge](./verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](./edgeinsets.md)
  The inset distances for the sides of a rectangle.
- [struct EdgeInsets3D](./edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontaledge)*