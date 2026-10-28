# init(x:y:z:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a rectangle mark for a 3D chart.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)
```

## Discussion

> ❗ **Important**: A 3D RectangleMark requires one parameter to be a single numeric value and the other two parameters to be numeric ranges.

For example, the following `Chart3D` shows a rectangle mark that extends along the x-axis and y-axis.

```swift
Chart3D {
    RectangleMark(
        x: .value("x", -0.5..<0.5),
        y: .value("y", -0.5..<0.5),
        z: .value("z", 0)
    )
}
```

## Parameters

- `x`: The x value.
- `y`: The y value.
- `z`: The z value.

## See Also

### Creating a rectangle mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](./init%28x,ystart,yend,width%29-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension)](./init%28x,ystart,yend,width%29-xhqp.md)
  Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](./init%28xstart,xend,y,height%29-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark/init(x:y:z:))*