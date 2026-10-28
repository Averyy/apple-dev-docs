# strokeBorder(_:style:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.

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
func strokeBorder<S>(_ content: S, style: StrokeStyle, antialiased: Bool = true) -> some View where S : ShapeStyle
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func strokeBorder<S>(_ content: S = .foreground, style: StrokeStyle, antialiased: Bool = true) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/insettableshape/strokeborder(_:style:antialiased:)-3vmk4)*