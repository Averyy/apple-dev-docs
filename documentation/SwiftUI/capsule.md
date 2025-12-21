# Capsule

**Framework**: SwiftUI  
**Kind**: struct

A capsule shape aligned inside the frame of the view containing it.

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
struct Capsule
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Overview

A capsule shape is equivalent to a rounded rectangle where the corner radius is chosen as half the length of the rectangle’s smallest edge.

## Topics

### Creating a capsule
- [init(style: RoundedCornerStyle)](capsule/init(style:).md)
  Creates a new capsule shape.
### Getting the shape’s characteristics
- [var style: RoundedCornerStyle](capsule/style.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [InsettableShape](insettableshape.md)
- [RoundedRectangularShape](roundedrectangularshape.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [struct Circle](circle.md)
  A circle centered on the frame of the view containing it.
- [struct Ellipse](ellipse.md)
  An ellipse aligned inside the frame of the view containing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/capsule)*