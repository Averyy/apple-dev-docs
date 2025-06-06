# shadow(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shape style that applies the specified shadow style to the current style.

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
static func shadow(_ style: ShadowStyle) -> some ShapeStyle
```

#### Return Value

A new shape style based on the current style that uses the specified shadow style.

#### Discussion

In most contexts the current style is the foreground, but not always. For example, when setting the value of the background style, that becomes the current implicit style.

The following example creates a circle filled with the current foreground style that uses an inner shadow:

```swift
Circle().fill(.shadow(.inner(radius: 1, y: 1)))
```

## Parameters

- `style`: The shadow style to apply.

## See Also

- [static func blendMode(BlendMode) -> some ShapeStyle](shapestyle/blendmode(_:)-swift.type.method.md)
  Returns a new style based on the current style that uses `mode` as its blend mode when drawing.
- [static func opacity(Double) -> some ShapeStyle](shapestyle/opacity(_:)-swift.type.method.md)
  Returns a new style based on the current style that multiplies by `opacity` when drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/shadow(_:)-swift.type.method)*