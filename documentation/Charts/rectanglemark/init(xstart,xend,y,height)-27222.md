# init(xStart:xEnd:y:height:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a rectangle mark with an x interval encoding and a y encoding.

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
init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension = .automatic) where X : Plottable, Y : Plottable
```

### Discussion

Use this initializer to map the x start, x end and y position to a rectangle for each data element. Optionally, specify the height of the rectangles.

The example below omits the optional `height` parameter and uses a number scale starting at (0,0) and ending at (6,6). The rectangle has the coordinates: (2,0), (2,4), (4,4), (4,0).

```swift
Chart(data) {
    RectangleMark(
        xStart: .value("Rect xStart", 2),
        xEnd: .value("Rect xEnd", 4),
        y: .value("Rect Y", 4)
    )
    .opacity(0.2)

    PointMark(
        x: .value("X", $0.x),
        y: .value("Y", $0.y)
    )
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) the rectangle highlights a rectangular area with coordinates: (2,0), (2,4), (4,4), (4,0).](https://developer.apple.com/tutorials/images/com.apple.Charts/RectangleMarkSwift.RectangleMarkScatterWithRectangleXIntervalY@2x.png)

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.
- `y`: The value plotted with y.
- `height`: The rectangle height. If `height` is not specified, then 70% of the step size will be used. If there is no step size a default height (in pts) will be used.

## See Also

### Creating a rectangle mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](./init%28x,ystart,yend,width%29-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension)](./init%28x,ystart,yend,width%29-xhqp.md)
  Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension)](./init%28xstart,xend,y,height%29-4x46i.md)
  Creates a rectangle mark with a fixed x interval and y encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](./init%28xstart,xend,ystart,yend%29-1qbzg.md)
  Creates a rectangle mark with x and y interval encodings.
- [init(xStart: CGFloat?, xEnd: CGFloat?, yStart: CGFloat?, yEnd: CGFloat?)](./init%28xstart,xend,ystart,yend%29-5682c.md)
  Creates a rectangle mark with fixed x and y intervals.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](./init%28xstart,xend,ystart,yend%29-5cbgh.md)
  Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](./init%28xstart,xend,ystart,yend%29-6jeka.md)
  Creates a rectangle mark with an x interval encoding and a fixed y interval.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension)](./init%28x,y,width,height%29.md)
  Creates a rectangle that plots values with x and y.
- [init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)](./init%28x,y,z%29.md)
  Creates a rectangle mark for a 3D chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(xstart:xend:y:height:)-27222)*