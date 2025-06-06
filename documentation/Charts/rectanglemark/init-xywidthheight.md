# init(x:y:width:height:)

**Framework**: Swift Charts  
**Kind**: init

Creates a rectangle that plots values with x and y.

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
init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension = .automatic, height: MarkDimension = .automatic) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to map an x and y position to a rectangle for each data element. Optionally, specify the width or height of the rectangles.

The example below omits the optional `width` and `height` parameters and uses a number scale starting at (0,0). The rectangle has the coordinates: (0,0), (0,3), (3,0), (3,3).

```swift
Chart(data) {
    RectangleMark(
        x: .value("Rect X", 3),
        y: .value("Rect Y", 3)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,0), (0,3), (3,0), (3,3).](https://docs-assets.developer.apple.com/published/b486caaff77bf328cb2280043d9b512a/RectangleMarkSwift.RectangleMarkScatterWithRectangleXY%402x.png)

## Parameters

- `x`: The value plotted with x.
- `y`: The value plotted with y.
- `width`: The rectangle width.  If   is not specified, then 70% of the step size will be used. If there is no step size a default width (in pts) will be used.
- `height`: The rectangle height.  If   is not specified, then 70% of the step size will be used. If there is no step size a default height (in pts) will be used.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-1qbzg.md)
  Creates a rectangle mark with x and y interval encodings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(x:y:width:height:))*