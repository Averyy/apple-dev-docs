# plotFrame

**Framework**: Swift Charts  
**Kind**: property

An anchor to the frame of the chart’s plot, or `nil` if there is no chart in the context of the chart proxy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var plotFrame: Anchor<CGRect>? { get }
```

#### Discussion

The plot is the area between the x and y axes, not including the axes themselves. If the chart is scrollable, the plot frame includes both visible and invisible portions of the plot.

You can convert the anchor to a frame using a `GeometryProxy`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy/plotframe)*