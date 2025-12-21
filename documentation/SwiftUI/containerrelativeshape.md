# ContainerRelativeShape

**Framework**: SwiftUI  
**Kind**: struct

A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct ContainerRelativeShape
```

## Topics

### Creating the shape
- [init()](containerrelativeshape/init.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [InsettableShape](insettableshape.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [func containerShape(_:)](view/containershape(_:).md)
  Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [protocol InsettableShape](insettableshape.md)
  A shape type that is able to inset itself to produce another shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerrelativeshape)*