# init(x:y:width:height:stacking:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a bar mark that plots values with x and y.

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
init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension = .automatic, height: MarkDimension = .automatic, stacking: MarkStackingMethod = .standard) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to create a chart with one or more bars.  For horizontal bars, plot categories or dates with y and numbers with x. For vertical bars, plot categories or dates with x and numbers with y:

```swift
Chart(data) {
    BarMark(
        x: .value("Department", $0.department),
        y: .value("Profit", $0.profit)
    )
}
```

![Vertical bar chart with x-axis showing department categories Production, Marketing, Finance and with y-axis ranging from 0 to 15000. There are 3 bars: Production 15000, Marketing 8000, Finance 10000.](https://developer.apple.com/tutorials/images/com.apple.Charts/BarMarkSwift.BarMarkBarChart@2x.png)

## Parameters

- `x`: The value plotted with x.
- `y`: The value plotted with y.
- `width`: The bar width. If `width` is `nil`, the default bar size will be applied.
- `height`: The bar height. If `height` is `nil`, the default bar size will be applied.
- `stacking`: The stacking method for the bars with the same categorical/date values. If `stacking` is `nil`, the bars will not be stacked.

## See Also

### Creating a bar mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](./init%28x,ystart,yend,width%29.md)
  Creates a bar mark that plots values with x and its y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](./init%28xstart,xend,y,height%29.md)
  Creates a bar mark that plots values with its x interval and y.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](./init%28xstart,xend,ystart,yend%29-98wo9.md)
  Creates a bar mark that plots values with its x interval and fixed y position.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](./init%28xstart,xend,ystart,yend%29-7541n.md)
  Creates a bar mark with fixed x interval that plots values with its y interval.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension, stacking: MarkStackingMethod)](./init%28x,ystart,yend,width,stacking%29.md)
  Creates a bar mark that plots a value on x with fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension, stacking: MarkStackingMethod)](./init%28xstart,xend,y,height,stacking%29.md)
  Creates a bar mark that plots values on y with fixed x interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(x:y:width:height:stacking:))*