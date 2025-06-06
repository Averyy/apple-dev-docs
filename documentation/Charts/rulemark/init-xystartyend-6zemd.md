# init(x:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates a vertical rule mark with value plotted with x.

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
init<X>(x: PlottableValue<X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil) where X : Plottable
```

##### Discussion

Use this initializer to create a vertical rule across a chart’s plotting area at an x position:

```swift
Chart {
    ForEach(data) {
        BarMark(
            x: .value("Profit", $0.profit),
            y: .value("Department", $0.department)
        )
    }
    RuleMark(x: .value("Break Even Threshold", 9000))
        .foregroundStyle(.red)
}
```

![Horizontal bar chart with y-axis showing department categories Production, Marketing, Finance, and R&D, and with x-axis ranging from 0 to 15000. There are 3 bars: Production 15000, Marketing 8000, Finance 10000. A vertical rule mark at 9000 shows the break even threshold.](https://docs-assets.developer.apple.com/published/63208ff663b147d47e606172f5ada383/LineSegmentMarkSwift.LineSegmentMarkBarChartWithVerticalLineSegmentMark%402x.png)

See the first code example in [`RuleMark`](rulemark.md) for the setup of the structure that contains `department` and `profit` properties.

## Parameters

- `x`: The value plotted with x.
- `yStart`: The y start position. If   is   the rule will start at the leading edge of the plotting area.
- `yEnd`: The y end position. If   is   the rule will end at the trailing edge of the plotting area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(x:ystart:yend:)-6zemd)*