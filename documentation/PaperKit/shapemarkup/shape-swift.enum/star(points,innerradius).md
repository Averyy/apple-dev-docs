# star(points:innerRadius:)

**Framework**: PaperKit  
**Kind**: method

A star shape with alternating inner and outer points.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func star(points: Int, innerRadius: CGFloat) -> ShapeMarkup.Shape
```

## Parameters

- `points`: The number of points on the star.
- `innerRadius`: The radius of inner points relative to outer points, in unit coordinate space (0.0 to 1.0). A value of `0.5` creates inner points halfway to the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/shape-swift.enum/star(points:innerradius:))*