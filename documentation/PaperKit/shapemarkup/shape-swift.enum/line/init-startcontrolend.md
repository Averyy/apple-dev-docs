# init(start:control:end:)

**Framework**: PaperKit  
**Kind**: init

Create a new quadratic Bézier curve line.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(start: CGPoint, control: CGPoint? = nil, end: CGPoint)
```

## Parameters

- `start`: The starting point in unit coordinate space.
- `control`: The control point that defines the curve in unit coordinate space. Defaults to `nil` which creates a straight line without a middle control point.
- `end`: The ending point in unit coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum/line/init(start:control:end:))*