# containerRelative

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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
@export(implementation)
static var containerRelative: ContainerRelativeShape { get }
```

Available when `Self` is `ContainerRelativeShape`.

## See Also

### Getting standard shapes
- [static var buttonBorder: ButtonBorderShape](./buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
- [static var capsule: Capsule](./capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](./capsule%28style%29.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](./circle.md)
  A circle centered on the frame of the view containing it.
- [static var ellipse: Ellipse](./ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var textInputBorder: TextInputBorderShape](./textinputborder.md)
  A shape that defers to the environment to determine the resolved text input border shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/containerrelative)*