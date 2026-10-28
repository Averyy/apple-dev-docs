# shape

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The type of the shape.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var shape: ShapeMarkup.Shape { get set }
```

## Discussion

The coordinate values of the shape type are relative to the unit coordinate space. For example a corner radius of `0.1` is equivalent to a radius of 10% of the minimum dimension of the shape.

Use `shapeScaled` for a shape type with scaled values relative to the shape’s `frame`.

## See Also

### Choosing a shape type
- [var shapeScaled: ShapeMarkup.Shape](./shapescaled.md)
  The type of the shape with values scaled to the current frame.
- [ShapeMarkup.Shape](./shape-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.property)*