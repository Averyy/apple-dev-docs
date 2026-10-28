# strokeBorder(_:lineWidth:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.

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
func strokeBorder<S>(_ content: S, lineWidth: CGFloat = 1, antialiased: Bool = true) -> some View where S : ShapeStyle
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func strokeBorder<S>(_ content: S = .foreground, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/insettableshape/strokeborder(_:linewidth:antialiased:)-6rs04)*