# init(xStart:xEnd:y:height:)

**Framework**: Swift Charts  
**Kind**: init

Creates a bar mark that plots values with its x interval and y.

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

##### Discussion

Use this initializer to show horizontal intervals for one or more categories:

```swift
Chart(data) {
   BarMark(
       xStart: .value("Start Time", $0.start),
       xEnd: .value("End Time", $0.end),
       y: .value("Job", $0.job)
   )
}
```

![Horizontal bar chart with x-axis showing start and end time and y-axis showing task name. It has 5 bars, Task 1 range 0 to 15, range 20 to 35, and range 40 to 55, and Task 2 range 5 to 25 and range 30 to 60 task](https://docs-assets.developer.apple.com/published/fd3042845d4db04fed8b1cf4bff7e0c8/BarMarkSwift.BarMarkHorizontalIntervalBarChart%402x.png)

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.
- `y`: The value plotted with y.
- `height`: The bar height.  If   is  , the default bar size will be applied.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](barmark/init(x:ystart:yend:width:).md)
  Creates a bar mark that plots values with x and its y interval.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:y:width:height:stacking:).md)
  Creates a bar mark that plots values with x and y.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension, stacking: MarkStackingMethod)](barmark/init(x:ystart:yend:width:stacking:).md)
  Creates a bar mark that plots a value on x with fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension, stacking: MarkStackingMethod)](barmark/init(xstart:xend:y:height:stacking:).md)
  Creates a bar mark that plots values on y with fixed x interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(xstart:xend:y:height:))*