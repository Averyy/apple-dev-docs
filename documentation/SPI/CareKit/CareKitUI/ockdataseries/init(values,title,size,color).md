---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(values:title:size:color:)"
framework: "CareKit/CareKitUI"
---

# init(values:title:size:color:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Creates a new data series that can be passed to a chart to be plotted. The series will be plotted in a single solid color. Values will be evenly spaced when displayed on a chart. Use this option when the x coordinate is not particularly meaningful, such as when creating bar charts.

## Declaration

```swift
init(values: [CGFloat], title: String, size: CGFloat = 10, color: UIColor? = nil)
```

## Parameters

- `values`: An array of values in graph space Cartesian coordinates.
- `title`: A title that will be used to represent this data series in the plot legend.
- `size`: A size specifying how large this data series should appear on the plot.
- `color`: The color that this data series will be plotted in.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(values:title:size:color:))*