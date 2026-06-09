# shapeScaled

**Framework**: PaperKit  
**Kind**: property

The type of the shape with values scaled to the current frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shapeScaled: ShapeMarkup.Shape { get set }
```

#### Discussion

Coordinate values are specified in points relative to the shape’s `frame`. When you resize the shape, this property’s values automatically update to reflect the new dimensions.

Use `shape` if you need consistent relative proportions that don’t change when resizing.

```swift
var shape = ShapeMarkup(
    frame: CGRect(x: 0, y: 0, width: 100, height: 100),
    type: .roundedRectangle(cornerRadius: 0.2)
)

// shapeScaled returns .roundedRectangle(cornerRadius: 20.0) // 20 points

shape.frame = CGRect(x: 0, y: 0, width: 200, height: 200)
// shapeScaled now returns .roundedRectangle(cornerRadius: 40.0) // 40 points
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shapescaled)*