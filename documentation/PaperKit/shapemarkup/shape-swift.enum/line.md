# ShapeMarkup.Shape.Line

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Line
```

## Topics

### Initializers
- [init(start: CGPoint, control: CGPoint?, end: CGPoint)](./line/init%28start,control,end%29.md)
  Create a new quadratic Bézier curve line.
### Instance Properties
- [var control: CGPoint?](./line/control.md)
  The control point that defines the curve in unit coordinate space.
- [var end: CGPoint](./line/end.md)
  The ending point in unit coordinate space.
- [var path: CGPath](./line/path.md)
  The path of the shape.
- [var start: CGPoint](./line/start.md)
  The starting point in unit coordinate space.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum/line)*