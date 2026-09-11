# line(start:control:end:)

**Framework**: PaperKit  
**Kind**: method

A quadratic Bézier curve line.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func line(start: CGPoint, control: CGPoint? = nil, end: CGPoint) -> ShapeMarkup.Shape
```

## Parameters

- `start`: The starting point in unit coordinate space.
- `control`: The control point that defines the curve in unit coordinate space. Defaults to `nil` which creates a straight line without a middle control point.
- `end`: The ending point in unit coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum/line(start:control:end:))*