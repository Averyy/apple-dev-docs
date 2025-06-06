# shadow(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies the specified shadow effect to the shape style.

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
func shadow(_ style: ShadowStyle) -> some ShapeStyle
```

#### Return Value

A new shape style that uses the specified shadow style.

#### Discussion

For example, you can create a rectangle that adds a drop shadow to the [`red`](shapestyle/red.md) shape style.

```swift
Rectangle().fill(.red.shadow(.drop(radius: 2, y: 3)))
```

## Parameters

- `style`: The shadow style to apply.

## See Also

- [func blendMode(BlendMode) -> some ShapeStyle](shapestyle/blendmode(_:)-swift.method.md)
  Returns a new style based on `self` that applies the specified blend mode when drawing.
- [func opacity(Double) -> some ShapeStyle](shapestyle/opacity(_:)-swift.method.md)
  Returns a new style based on `self` that multiplies by the specified opacity when drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/shadow(_:)-swift.method)*