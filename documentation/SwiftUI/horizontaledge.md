# HorizontalEdge

**Framework**: SwiftUI  
**Kind**: enum

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

Use a horizontal edge for tasks like setting a swipe action with the [`swipeActions(edge:allowsFullSwipe:content:)`](view/swipeactions(edge:allowsfullswipe:content:).md) view modifier. The positions of the leading and trailing edges depend on the locale chosen by the user.

## Topics

### Getting the edges
- [HorizontalEdge.leading](horizontaledge/leading.md)
  The leading edge.
- [HorizontalEdge.trailing](horizontaledge/trailing.md)
  The trailing edge.
### Accessing sets of edges
- [HorizontalEdge.Set](horizontaledge/set.md)
  An efficient set of horizontal edges.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [CaseIterable](../swift/caseiterable.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum Edge](edge.md)
  An enumeration to indicate one edge of a rectangle.
- [enum Edge3D](edge3d.md)
  An edge or face of a 3D volume.
- [enum VerticalEdge](verticaledge.md)
  An edge on the vertical axis.
- [struct EdgeInsets](edgeinsets.md)
  The inset distances for the sides of a rectangle.
- [struct EdgeInsets3D](edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontaledge)*