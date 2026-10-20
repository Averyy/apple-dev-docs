# plotAreaFrame

**Framework**: Swift Charts  
**Kind**: property  
**Role**: Instance Property

An anchor to the frame of the chart’s plot.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0 (renamed: plotFrame)
- iPadOS 16.0+ - Deprecated in 17.0 (renamed: plotFrame)
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: plotFrame)
- macOS 13.0+ - Deprecated in 14.0 (renamed: plotFrame)
- tvOS 16.0+ - Deprecated in 17.0 (renamed: plotFrame)
- visionOS 1.0+
- watchOS 9.0+ - Deprecated in 10.0 (renamed: plotFrame)

## Declaration

```swift
var plotAreaFrame: Anchor<CGRect> { get }
```

#### Discussion

The plot is the area between the x and y axes, not including the axes themselves. If the chart is scrollable, the plot frame includes both visible and invisible portions of the plot.

A chart must exist in the context of the chart proxy. You can convert the anchor to a frame using a `GeometryProxy`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy/plotareaframe)*