# buttonBorder

**Framework**: SwiftUI  
**Kind**: property

A shape that defers to the environment to determine the resolved button border shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var buttonBorder: ButtonBorderShape { get }
```

#### Discussion

You can override the resolved shape in a given view hierarchy by using the [`buttonBorderShape(_:)`](view/buttonbordershape(_:).md) modifier. If no button border shape is specified, it is resolved automatically for the given context and platform.

## See Also

- [static var capsule: Capsule](shape/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](shape/capsule(style:).md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](shape/circle.md)
  A circle centered on the frame of the view containing it.
- [static var containerRelative: ContainerRelativeShape](shape/containerrelative.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [static var ellipse: Ellipse](shape/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var textInputBorder: TextInputBorderShape](shape/textinputborder.md)
  A shape that defers to the environment to determine the resolved text input border shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/buttonborder)*