# blendMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new style based on the current style that uses `mode` as its blend mode when drawing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func blendMode(_ mode: BlendMode) -> some ShapeStyle
```

#### Discussion

In most contexts the current style is the foreground but e.g. when setting the value of the background style, that becomes the current implicit style.

For example, a circle filled with the current foreground style and the overlay blend mode:

```swift
Circle().fill(.blendMode(.overlay))
```

## See Also

- [static func opacity(Double) -> some ShapeStyle](shapestyle/opacity(_:)-swift.type.method.md)
  Returns a new style based on the current style that multiplies by `opacity` when drawing.
- [static func shadow(ShadowStyle) -> some ShapeStyle](shapestyle/shadow(_:)-swift.type.method.md)
  Returns a shape style that applies the specified shadow style to the current style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/blendmode(_:)-swift.type.method)*