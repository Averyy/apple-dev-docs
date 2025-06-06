# init(x:yStart:yEnd:width:)

**Framework**: Swift Charts  
**Kind**: init

Creates a rectangle mark with an y interval encoding and an x encoding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension = .automatic) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to map the y start, y end and x position to a rectangle for each data element. Optionally, specify the width of the rectangles.

The example below omits the optional `width` field and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (0,2), (0,4), (4,4), (4,2).

```swift
Chart(data) {
    RectangleMark(
        yStart: .value("Rect yStart", 2),
        yEnd: .value("Rect yEnd", 4),
        x: .value("Rect X", 4)
    )
    .opacity(0.2)

   PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,2), (0,4), (4,4), (4,2).](https://docs-assets.developer.apple.com/published/71d976601f96157b1e907c756304bd53/RectangleMarkSwift.RectangleMarkScatterWithRectangleYIntervalX%402x.png)

## Parameters

- `x`: The value plotted with y.
- `yStart`: The value plotted with x start.
- `yEnd`: The value plotted with x end.
- `width`: The rectangle width. If   is not specified, then 70% of the step size will be used. If there is no step size a default width (in pts) will be used.

## See Also

- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-1qbzg.md)
  Creates a rectangle mark with x and y interval encodings.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension)](rectanglemark/init(x:y:width:height:).md)
  Creates a rectangle that plots values with x and y.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(x:ystart:yend:width:)-vh2x)*