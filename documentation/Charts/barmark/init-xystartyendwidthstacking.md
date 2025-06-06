# init(x:yStart:yEnd:width:stacking:)

**Framework**: Swift Charts  
**Kind**: init

Creates a bar mark that plots a value on x with fixed y interval.

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
init<X>(x: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil, width: MarkDimension = .automatic, stacking: MarkStackingMethod = .standard) where X : Plottable
```

##### Discussion

Use this initializer to create a chart with a single horizontal bar:

```swift
Chart(data) {
    BarMark(
        x: .value("Profit", $0.profit)
    )
    .foregroundStyle(by: .value("Product Category", $0.productCategory))
}
```

![Horizontal bar chart with one bar on the x-axis showing profit ranging from 0 to 15000 with stacked categories Gizmos, Gadgets and Widgets. Legend showing the color mapped to a product category.](https://docs-assets.developer.apple.com/published/866989cb862990508465e796c804535b/BarMarkSwift.BarMarkHorizontalStacked1DBarChartWithForegroundColor%402x.png)

## Parameters

- `x`: The value plotted with x.
- `yStart`: The y start position. If   is   then the rectangle will start at the leading edge of the plotting area.
- `yEnd`: The y end position. If   is   then the rectangle will end at the trailing edge of the plotting area.
- `width`: The bar width.  If   is  , the default bar size will be applied.
- `stacking`: The stacking method for the bars with the same categorical/date values.   If   is  , the bars will not be stacked.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](barmark/init(x:ystart:yend:width:).md)
  Creates a bar mark that plots values with x and its y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](barmark/init(xstart:xend:y:height:).md)
  Creates a bar mark that plots values with its x interval and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(xstart:xend:y:height:stacking:).md)
  Creates a bar mark that plots values on y with fixed x interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(x:ystart:yend:width:stacking:))*