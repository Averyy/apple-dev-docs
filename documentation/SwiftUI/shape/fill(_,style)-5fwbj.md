# fill(_:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Fills this shape with a color or gradient.

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
nonisolated
func fill<S>(_ content: S, style: FillStyle = FillStyle()) -> some View where S : ShapeStyle
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func fill<S>(_ content: S = .foreground, style: FillStyle = FillStyle()) -> _ShapeView<Self, S> where S : ShapeStyle
```

## Return Value

A shape filled with the color or gradient you supply.

## Parameters

- `content`: The color or gradient to use when filling this shape.
- `style`: The style options that determine how the fill renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/fill(_:style:)-5fwbj)*