---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(datapoints:title:size:color:)"
framework: "CareKit/CareKitUI"
---

# init(dataPoints:title:size:color:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Creates a new data series that can be passed to a chart to be plotted. The series will be plotted in a single solid color. Use this initialize if you wish to plot data at precise or irregular intervals.

## Declaration

```swift
init(dataPoints: [CGPoint], title: String, size: CGFloat = 10, color: UIColor? = nil)
```

## Parameters

- `dataPoints`: An array of points in graph space Cartesian coordinates. The origin is in bottom left corner.
- `title`: A title that will be used to represent this data series in the plot legend.
- `size`: A size specifying how large this data series should appear on the plot.
- `color`: A solid color to be used when plotting the data series.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(datapoints:title:size:color:))*