# init(xStart:xEnd:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates a bar mark with fixed x interval that plots values with its y interval.

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
init<Y>(xStart: CGFloat? = nil, xEnd: CGFloat? = nil, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where Y : Plottable
```

##### Discussion

Use this initializer to show vertical intervals for one category:

```swift
Chart(data) {
   BarMark(
       yStart: .value("Start Time", $0.start),
       yEnd: .value("End Time", $0.end)
   )
}
```

![Vertical bar chart with y-axis showing start and end time. It has 5 bars, Task 1 range 0 to 5, range 10 to 20, range 25 to 40, range 45 to 65, and range 70-95.](https://docs-assets.developer.apple.com/published/eb30e9ab77f971d57cc83c2abd6f7a59/BarMarkSwift.BarMarkVertical1DIntervalBarChart%402x.png)

## Parameters

- `xStart`: The x start position. If   is   then the rectangle will start at the leading edge of the plotting area.
- `xEnd`: The x end position. If   is   then the rectangle will end at the trailing edge of the plotting area.
- `yStart`: The value plotted to y start.
- `yEnd`: The value plotted to y end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barmark/init(xstart:xend:ystart:yend:)-7541n)*