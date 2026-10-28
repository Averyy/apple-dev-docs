# fill(_:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Fills this shape with a color or gradient.

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
@export(implementation)
nonisolated func fill<S>(_ content: S = .foreground, style: FillStyle = FillStyle()) -> _ShapeView<Self, S> where S : ShapeStyle
```

**Other overloads**:

```swift
nonisolated
func fill<S>(_ content: S, style: FillStyle = FillStyle()) -> some View where S : ShapeStyle
```

## Return Value

A shape filled with the color or gradient you supply.

## Parameters

- `content`: The color or gradient to use when filling this shape.
- `style`: The style options that determine how the fill renders.

## See Also

### Filling a shape
- [func fill(style: FillStyle) -> some View](./fill%28style%29.md)
  Fills this shape with the foreground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/fill(_:style:))*