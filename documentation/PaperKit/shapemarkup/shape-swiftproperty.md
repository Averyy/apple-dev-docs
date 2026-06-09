# shape

**Framework**: PaperKit  
**Kind**: property

The type of the shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shape: ShapeMarkup.Shape { get set }
```

#### Discussion

The coordinate values of the shape type are relative to the unit coordinate space. For example a corner radius of `0.1` is equivalent to a radius of 10% of the minimum dimension of the shape.

Use `shapeScaled` for a shape type with scaled values relative to the shape’s `frame`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.property)*