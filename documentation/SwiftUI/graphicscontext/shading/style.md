# style(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills with the given shape style.

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
static func style<S>(_ style: S) -> GraphicsContext.Shading where S : ShapeStyle
```

#### Return Value

A shading instance filled with a shape style.

#### Discussion

Styles with geometry defined in a unit coordinate space map that space to the rectangle associated with the drawn object. You can adjust that using the [`in(_:)`](shapestyle/in(_:).md) method. The shape style might affect the blend mode and opacity of the drawn object.

## Parameters

- `style`: A   instance to draw with.

## See Also

- [static var foreground: GraphicsContext.Shading](graphicscontext/shading/foreground.md)
  A shading instance that fills with the foreground style from the graphics context’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/style(_:))*