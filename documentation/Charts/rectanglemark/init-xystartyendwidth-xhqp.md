# init(x:yStart:yEnd:width:)

**Framework**: Swift Charts  
**Kind**: init

Creates a rectangle mark that plots values on x and has a fixed y interval.

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
init<X>(x: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil, width: MarkDimension = .automatic) where X : Plottable
```

#### Discussion

- x: The value plotted with x.
- width: The rectangle width.  If `width` is not specified, then 70% of the step size will be used. If there is no step size a default width (in pts) will be used.
- yStart: The y start position. If `yStart` is `nil` then the rectangle will start at the leading edge of the plotting area.
- yEnd: The y end position. If `yEnd` is `nil` then the rectangle will end at the trailing edge of the plotting area.

##### Discussion

Use this initializer to map an x position to a rectangle for each data element. Optionally, specify the width, yStart position, or yEnd positions of the rectangles.

The example below omits the optional `width`, `yStart`, and `yEnd` parameters and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (0,0), (0,6), (3,6), (3,0).

```swift
Chart(data) {
    RectangleMark(
        x: .value("Rect X", 3)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (0,0), (0,6), (3,6), (3,0).](https://docs-assets.developer.apple.com/published/5b61edfb70d84baa7eea6f9344a2612a/RectangleMarkSwift.RectangleMarkScatterWithRectangleX%402x.png)

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-4x46i.md)
  Creates a rectangle mark with a fixed x interval and y encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-1qbzg.md)
  Creates a rectangle mark with x and y interval encodings.
- [init(xStart: CGFloat?, xEnd: CGFloat?, yStart: CGFloat?, yEnd: CGFloat?)](rectanglemark/init(xstart:xend:ystart:yend:)-5682c.md)
  Creates a rectangle mark with fixed x and y intervals.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-5cbgh.md)
  Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](rectanglemark/init(xstart:xend:ystart:yend:)-6jeka.md)
  Creates a rectangle mark with an x interval encoding and a fixed y interval.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension)](rectanglemark/init(x:y:width:height:).md)
  Creates a rectangle that plots values with x and y.
- [init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)](rectanglemark/init(x:y:z:).md)
  Creates a rectangle mark for a 3D chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(x:ystart:yend:width:)-xhqp)*