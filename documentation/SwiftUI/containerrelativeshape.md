# ContainerRelativeShape

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A shape whose dimensions the system calculates from an inset version of the current container shape.

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

#### Overview

If there is not a current container shape, the system provides a rectangle.

## Topics

### Creating the shape
- [init()](./containerrelativeshape/init%28%29.md)

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [InsettableShape](./insettableshape.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Shape](./shape.md)
- [View](./view.md)

## See Also

### Setting a container shape
- [func containerShape(_:)](./view/containershape%28_%29.md)
  Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [protocol InsettableShape](./insettableshape.md)
  A shape type that is able to inset itself to produce another shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerrelativeshape)*