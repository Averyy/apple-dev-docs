# init(xStart:xEnd:y:height:stacking:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a bar mark that plots values on y with fixed x interval.

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
init<Y>(xStart: CGFloat? = nil, xEnd: CGFloat? = nil, y: PlottableValue<Y>, height: MarkDimension = .automatic, stacking: MarkStackingMethod = .standard) where Y : Plottable
```

##### Discussion

Use this initializer to create a chart with a single vertical bar:

```swift
Chart(data) {
    BarMark(
        y: .value("Profit", $0.profit)
    )
    .foregroundStyle(by: .value("Product Category", $0.productCategory))
}
```

![Vertical bar chart with one bar on the y-axis showing profit ranging from 0 to 15000 with stacked categories Gizmos, Gadgets and Widgets. Legend showing the color mapped to a product category.](https://developer.apple.com/tutorials/images/com.apple.Charts/BarMarkSwift.BarMarkVerticalStacked1DBarChartWithForegroundColor@2x.png)

## Parameters

- `xStart`: The x start position. If `xStart` is `nil` then the rectangle will start at the leading edge of the plotting area.
- `xEnd`: The x end position. If `xStart` is `nil` then the rectangle will end at the trailing edge of the plotting area.
- `y`: The value plotted with y.
- `height`: The bar height.  If `height` is `nil`, the default bar size will be applied.
- `stacking`: The stacking method for the bars with the same categorical/date values. If `stacking` is `nil`, the bars will not be stacked.

## See Also

### Creating a bar mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](./init%28x,ystart,yend,width%29.md)
  Creates a bar mark that plots values with x and its y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](./init%28xstart,xend,y,height%29.md)
  Creates a bar mark that plots values with its x interval and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](./init%28x,y,width,height,stacking%29.md)
  Creates a bar mark that plots values with x and y.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](./init%28xstart,xend,ystart,yend%29-98wo9.md)
  Creates a bar mark that plots values with its x interval and fixed y position.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](./init%28xstart,xend,ystart,yend%29-7541n.md)
  Creates a bar mark with fixed x interval that plots values with its y interval.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](./init%28x,y,width,height,stacking%29.md)
  Creates a bar mark that plots values with x and y.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension, stacking: MarkStackingMethod)](./init%28x,ystart,yend,width,stacking%29.md)
  Creates a bar mark that plots a value on x with fixed y interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(xstart:xend:y:height:stacking:))*