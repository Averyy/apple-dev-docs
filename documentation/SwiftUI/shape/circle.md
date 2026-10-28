# circle

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A circle centered on the frame of the view containing it.

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
@export(implementation)
static var circle: Circle { get }
```

Available when `Self` is `Circle`.

## Discussion

The circle’s radius equals half the length of the frame rectangle’s smallest edge.

## See Also

### Getting standard shapes
- [static var buttonBorder: ButtonBorderShape](./buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
- [static var capsule: Capsule](./capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](./capsule%28style%29.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var containerRelative: ContainerRelativeShape](./containerrelative.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [static var ellipse: Ellipse](./ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var textInputBorder: TextInputBorderShape](./textinputborder.md)
  A shape that defers to the environment to determine the resolved text input border shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/circle)*