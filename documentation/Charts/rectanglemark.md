# RectangleMark

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents data using rectangles.

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
@MainActor
@preconcurrency struct RectangleMark
```

#### Overview

Use rectangle mark to map data fields to rectangles. You can use the rectangle mark to create heat map charts or to annotate rectangular areas in a chart.

##### Create a Heat Map with Rectangle Marks

When presenting data about the effectiveness of a machine learning model, you typically organize the data using a confusion matrix which shows the predicted versus the actual results of the model. To create a 2D heat map that represents a machine learning model you use [`init(x:y:width:height:)`](rectanglemark/init(x:y:width:height:).md). The example below uses a 2D heat map to visualize a basic confusion matrix with the following layout:

|  | Negative | Positive |
| --- | --- | --- |
|  | True Negative | False Negative |
|  | False Positive | True Positive |

The number of records in each cell, `num`,  is represented by the color of its corresponding rectangle. This is done by applying the [`foregroundStyle(by:)`](chartcontent/foregroundstyle(by:).md) modifier to the rectangle mark and passing it a [`PlottableValue`](plottablevalue.md) constructed with [`value(_:_:)`](plottablevalue/value(_:_:)-13lvv.md) which takes a label and the value to plot, in this case `num`. A scale from values of `num` to color will be automatically generated and used to color the rectangles based on the value.

```swift
struct MatrixEntry {
    var positive: String
    var negative: String
    var num: Double
}

var data: [MatrixEntry] = [
    MatrixEntry(positive: "+", negative: "+", num: 125),
    MatrixEntry(positive: "+", negative: "-", num: 10),
    MatrixEntry(positive: "-", negative: "-", num: 80),
    MatrixEntry(positive: "-", negative: "+", num: 1)
]

var body: some View {
    Chart(data) {
        RectangleMark(
            x: .value("Positive", $0.positive),
            y: .value("Negative", $0.negative)
        )
        .foregroundStyle(by: .value("Number", $0.num))
    }
}
```

![2D heat map chart that represents a simple confusion matrix in a 2x2 grid. The number of records is represented by the color of its corresponding rectangle. Darker colors represent higher values.](https://docs-assets.developer.apple.com/published/f585a7db900f8c450c88cdcfe7b0a8a9/RectangleMarkSwift.RectangleMarkHistogramHeatmap2D%402x.png)

##### Annotate a Rectangular Area with Rectangle Marks

You can annotate a specific region in a chart with a rectangle mark by providing the coordinates of one or more rectangles. For example you can annotate point marks with rectangle marks using a shared data source like in the example below:

```swift
struct Coord {
    var x: Double
    var y: Double
}

var data: [Coord] = [
    Coord(x: 5, y: 5),
    Coord(x: 2.5, y: 2.5),
    Coord(x: 3, y: 3)
]

var body: some View {
    Chart(data) {
        RectangleMark(
            xStart: .value("Rect Start Width", $0.x - 0.25),
            xEnd: .value("Rect End Width", $0.x + 0.25),
            yStart: .value("Rect Start Height", $0.y - 0.25),
            yEnd: .value("Rect End Height", $0.y + 0.25)
        )
        .opacity(0.2)

        PointMark(
            x: .value("X", $0.x),
            y: .value("Y", $0.y)
        )
    }
}
```

![Scatter plot chart with a rectangle mark annotation. 3 points on the chart at: (5, 5), (2.5, 2.5), (3, 3) each point mark is highlighted with an opaque rectangle.](https://docs-assets.developer.apple.com/published/25ed6d8c79ed66cfd15feff0a8264741/RectangleMarkSwift.RectangleMarkScatter%402x.png)

## Topics

### Creating a rectangle mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-vh2x.md)
  Creates a rectangle mark with an y interval encoding and an x encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-27222.md)
  Creates a rectangle mark with an x interval encoding and a y encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-1qbzg.md)
  Creates a rectangle mark with x and y interval encodings.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension)](rectanglemark/init(x:y:width:height:).md)
  Creates a rectangle that plots values with x and y.
### Initializers
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension)](rectanglemark/init(x:ystart:yend:width:)-xhqp.md)
  Creates a rectangle mark that plots values on x and has a fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension)](rectanglemark/init(xstart:xend:y:height:)-4x46i.md)
  Creates a rectangle mark with a fixed x interval and y encoding.
- [init(xStart: CGFloat?, xEnd: CGFloat?, yStart: CGFloat?, yEnd: CGFloat?)](rectanglemark/init(xstart:xend:ystart:yend:)-5682c.md)
  Creates a rectangle mark with fixed x and y intervals.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rectanglemark/init(xstart:xend:ystart:yend:)-5cbgh.md)
  Creates a rectangle mark with a y interval encoding and a fixed x interval.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](rectanglemark/init(xstart:xend:ystart:yend:)-6jeka.md)
  Creates a rectangle mark with an x interval encoding and a fixed y interval.

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AreaMark](areamark.md)
  Chart content that represents data using the area of one or more regions.
- [struct LineMark](linemark.md)
  Chart content that represents data using a sequence of connected line segments.
- [struct PointMark](pointmark.md)
  Chart content that represents data using points.
- [struct RuleMark](rulemark.md)
  Chart content that represents data using a single horizontal or vertical rule.
- [struct BarMark](barmark.md)
  Chart content that represents data using bars.
- [struct SectorMark](sectormark.md)
  A sector of a pie or donut chart, which shows how individual categories make up a meaningful total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectanglemark)*