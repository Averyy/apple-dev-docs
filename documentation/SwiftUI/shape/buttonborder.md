# buttonBorder

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

Available when `Self` is `ButtonBorderShape`.

## Discussion

You can override the resolved shape in a given view hierarchy by using the [`buttonBorderShape(_:)`](../view/buttonbordershape%28_%29.md) modifier. If no button border shape is specified, it is resolved automatically for the given context and platform.

## See Also

### Getting standard shapes
- [static var capsule: Capsule](./capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](./capsule%28style%29.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](./circle.md)
  A circle centered on the frame of the view containing it.
- [static var containerRelative: ContainerRelativeShape](./containerrelative.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [static var ellipse: Ellipse](./ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var textInputBorder: TextInputBorderShape](./textinputborder.md)
  A shape that defers to the environment to determine the resolved text input border shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/buttonborder)*