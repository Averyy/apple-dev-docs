# init(xStart:xEnd:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a bar mark that plots values with its x interval and fixed y position.

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
init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil) where X : Plottable
```

### Discussion

Use this initializer to show horizontal intervals for one category:

```swift
Chart(data) {
   BarMark(
       xStart: .value("Start Time", $0.start),
       xEnd: .value("End Time", $0.end)
   )
}
```

![Horizontal bar chart with x-axis showing start and end time. It has 5 bars, Task 1 range 0 to 5, range 10 to 20, range 25 to 40, range 45 to 65, and range 70-95.](https://developer.apple.com/tutorials/images/com.apple.Charts/BarMarkSwift.BarMarkHorizontal1DIntervalBarChart@2x.png)

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.

## See Also

### Creating a bar mark
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, width: MarkDimension)](./init%28x,ystart,yend,width%29.md)
  Creates a bar mark that plots values with x and its y interval.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, height: MarkDimension)](./init%28xstart,xend,y,height%29.md)
  Creates a bar mark that plots values with its x interval and y.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](./init%28x,y,width,height,stacking%29.md)
  Creates a bar mark that plots values with x and y.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](./init%28xstart,xend,ystart,yend%29-7541n.md)
  Creates a bar mark with fixed x interval that plots values with its y interval.
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, width: MarkDimension, height: MarkDimension, stacking: MarkStackingMethod)](./init%28x,y,width,height,stacking%29.md)
  Creates a bar mark that plots values with x and y.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimension, stacking: MarkStackingMethod)](./init%28x,ystart,yend,width,stacking%29.md)
  Creates a bar mark that plots a value on x with fixed y interval.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>, height: MarkDimension, stacking: MarkStackingMethod)](./init%28xstart,xend,y,height,stacking%29.md)
  Creates a bar mark that plots values on y with fixed x interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(xstart:xend:ystart:yend:)-98wo9)*