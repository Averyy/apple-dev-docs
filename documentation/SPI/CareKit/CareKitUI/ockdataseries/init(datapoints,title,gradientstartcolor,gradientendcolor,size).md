---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(datapoints:title:gradientstartcolor:gradientendcolor:size:)"
framework: "CareKit/CareKitUI"
---

# init(dataPoints:title:gradientStartColor:gradientEndColor:size:)

**Framework**: CareKit/CareKitUI  
**Kind**: init  
**Role**: Initializer

Creates a new data series that can be passed to a chart to be plotted. The series will be plotted with a gradient color scheme. Use this initialize if you wish to plot data at precise or irregular intervals.

## Declaration

```swift
init(dataPoints: [CGPoint], title: String, gradientStartColor: UIColor, gradientEndColor: UIColor, size: CGFloat = 10)
```

## Parameters

- `dataPoints`: An array of points in graph space Cartesian coordinates. The origin is in bottom left corner.
- `title`: A title that will be used to represent this data series in the plot legend.
- `gradientStartColor`: The start color for the gradient.
- `gradientEndColor`: The end color for the gradient.
- `size`: A size specifying how large this data series should appear on the plot.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries/init(datapoints:title:gradientstartcolor:gradientendcolor:size:))*