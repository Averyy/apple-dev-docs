---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(values:title:gradientstartcolor:gradientendcolor:size:)"
framework: "CareKit/CareKitUI"
---

# init(values:title:gradientStartColor:gradientEndColor:size:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Creates a new data series that can be passed to a chart to be plotted. The series will be plotted with a gradient color scheme. Values will be evenly spaced when displayed on a chart. Use this option when the x coordinate is not particularly meaningful, such as when creating bar charts.

## Declaration

```swift
init(values: [CGFloat], title: String, gradientStartColor: UIColor, gradientEndColor: UIColor, size: CGFloat = 10)
```

## Parameters

- `values`: An array of values in graph space Cartesian coordinates.
- `title`: A title that will be used to represent this data series in the plot legend.
- `gradientStartColor`: The start color for the gradient.
- `gradientEndColor`: The end color for the gradient.
- `size`: A size specifying how large this data series should appear on the plot.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(values:title:gradientstartcolor:gradientendcolor:size:))*