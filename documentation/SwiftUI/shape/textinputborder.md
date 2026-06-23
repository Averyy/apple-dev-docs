# textInputBorder

**Framework**: SwiftUI  
**Kind**: property

A shape that defers to the environment to determine the resolved text input border shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var textInputBorder: TextInputBorderShape { get }
```

#### Discussion

You can override the resolved shape in a given view hierarchy by using the [`textInputBorderShape(_:)`](view/textinputbordershape(_:).md) modifier. If no text input border shape is specified, it is resolved automatically for the given context and platform.

## See Also

- [static var buttonBorder: ButtonBorderShape](shape/buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/textinputborder)*