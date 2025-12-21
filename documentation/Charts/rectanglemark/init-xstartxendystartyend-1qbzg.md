# init(xStart:xEnd:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates a rectangle mark with x and y interval encodings.

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
init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to map the x start, x end, y start, and y end position to a rectangle for each data element.

The example below uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (2,2), (2,4), (4,4), (4,2).

```swift
Chart(data) {
    RectangleMark(
        xStart: .value("Rect xStart", 2),
        xEnd: .value("Rect xEnd", 4),
        yStart: .value("Rect yStart", 2),
        yEnd: .value("Rect yEnd", 4)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (2,2), (2,4), (4,4), (4,2).](https://docs-assets.developer.apple.com/published/a027d86f7339b410bff6be08697a73cb/RectangleMarkSwift.RectangleMarkScatterWithRectangleXAndYIntervals%402x.png)

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.
- `yStart`: The value plotted with y start.
- `yEnd`: The value plotted with y end.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-xhqp.md)
  Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-4x46i.md)
  Creates a rectangle mark with a fixed x interval and y encoding.
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

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:ystart:yend:)-1qbzg)*