# init(xStart:xEnd:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

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

##### Discussion

Use this initializer to show horizontal intervals for one category:

```swift
Chart(data) {
   BarMark(
       xStart: .value("Start Time", $0.start),
       xEnd: .value("End Time", $0.end)
   )
}
```

![Horizontal bar chart with x-axis showing start and end time. It has 5 bars, Task 1 range 0 to 5, range 10 to 20, range 25 to 40, range 45 to 65, and range 70-95.](https://docs-assets.developer.apple.com/published/bd883356139b55d3a3236e5a3cfa659b/BarMarkSwift.BarMarkHorizontal1DIntervalBarChart%402x.png)

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(xstart:xend:ystart:yend:)-98wo9)*