# init(x:yStart:yEnd:width:)

**Framework**: Swift Charts  
**Kind**: init

Creates a bar mark that plots values with x and its y interval.

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

Use this initializer to show vertical intervals for one or more categories:

```swift
Chart(data) {
   BarMark(
       x: .value("Job", $0.job),
       yStart: .value("Start Time", $0.start),
       yEnd: .value("End Time", $0.end)
   )
}
```

![Vertical bar chart with x-axis showing task name and y-axis showing start and end time. It has 5 bars, Task 1 range 0 to 15, range 20 to 35, and range 40 to 55, and Task 2 range 5 to 25 and range 30 to 60 task](https://docs-assets.developer.apple.com/published/a333671275f2473facafa580974b315e/BarMarkSwift.BarMarkVerticalIntervalBarChart%402x.png)

## Parameters

- `x`: The value plotted with x.
- `yStart`: The value plotted with y start.
- `yEnd`: The value plotted with y end.
- `width`: The bar width.  If   is  , the default bar size will be applied.

## See Also

- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](barmark/init(xstart:xend:y:height:).md)
  Creates a bar mark that plots values with its x interval and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:ystart:yend:width:stacking:).md)
  Creates a bar mark that plots a value on x with fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(xstart:xend:y:height:stacking:).md)
  Creates a bar mark that plots values on y with fixed x interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(x:ystart:yend:width:))*