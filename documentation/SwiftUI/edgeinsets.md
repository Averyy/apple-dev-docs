# EdgeInsets

**Framework**: SwiftUI  
**Kind**: struct

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
- [var top: CGFloat](edgeinsets/top.md)
- [var bottom: CGFloat](edgeinsets/bottom.md)
- [var leading: CGFloat](edgeinsets/leading.md)
- [var trailing: CGFloat](edgeinsets/trailing.md)
### Creating an edge inset
- [init()](edgeinsets/init.md)
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](edgeinsets/init(top:leading:bottom:trailing:).md)
- [init(_:)](edgeinsets/init(_:).md)
  Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and `back` values.

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
- [struct EdgeInsets3D](edgeinsets3d.md)
  The inset distances for the faces of a 3D volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edgeinsets)*