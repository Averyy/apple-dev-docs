---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries"
framework: "CareKit/CareKitUI"
---

# OCKDataSeries

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

Represents a single group of data to be plotted. In most cases, CareKit plots accept multiple data series, allowing for for several data series to be plotted on a single axis for easy comparison.

## Declaration

```swift
struct OCKDataSeries
```

## Overview

> **See Also**: `OCKGraphView`

## Topics

### Initializers
- [init(dataPoints: [CGPoint], title: String, gradientStartColor: UIColor, gradientEndColor: UIColor, size: CGFloat)](./ockdataseries/init%28datapoints,title,gradientstartcolor,gradientendcolor,size%29.md)
  Creates a new data series that can be passed to a chart to be plotted. The series will be plotted with a gradient color scheme. Use this initialize if you wish to plot data at precise or irregular intervals.
- [init(dataPoints: [CGPoint], title: String, size: CGFloat, color: UIColor?)](./ockdataseries/init%28datapoints,title,size,color%29.md)
  Creates a new data series that can be passed to a chart to be plotted. The series will be plotted in a single solid color. Use this initialize if you wish to plot data at precise or irregular intervals.
- [init(values: [CGFloat], title: String, gradientStartColor: UIColor, gradientEndColor: UIColor, size: CGFloat)](./ockdataseries/init%28values,title,gradientstartcolor,gradientendcolor,size%29.md)
  Creates a new data series that can be passed to a chart to be plotted. The series will be plotted with a gradient color scheme. Values will be evenly spaced when displayed on a chart. Use this option when the x coordinate is not particularly meaningful, such as when creating bar charts.
- [init(values: [CGFloat], title: String, size: CGFloat, color: UIColor?)](./ockdataseries/init%28values,title,size,color%29.md)
  Creates a new data series that can be passed to a chart to be plotted. The series will be plotted in a single solid color. Values will be evenly spaced when displayed on a chart. Use this option when the x coordinate is not particularly meaningful, such as when creating bar charts.
### Instance Properties
- [var accessibilityLabels: [String]](./ockdataseries/accessibilitylabels.md)
  Used to set the accessibility labels of each of the data points. This array should either be empty or contain the same number of elements as the data series array.
- [var dataPoints: [CGPoint]](./ockdataseries/datapoints.md)
  An array of points given in plot space Cartesian coordinates The plot origin (0, 0) is in the bottom left hand corner.
- [var gradientEndColor: UIColor?](./ockdataseries/gradientendcolor.md)
  The end color of the gradient this data series will be plotted in.
- [var gradientStartColor: UIColor?](./ockdataseries/gradientstartcolor.md)
  The start color of the gradient this data series will be plotted in.
- [var size: CGFloat](./ockdataseries/size.md)
  A size specifying how large this data series should appear on the plot. Its precise interpretation may vary depending on plot type used.
- [var title: String](./ockdataseries/title.md)
  A title for this data series that will be displayed in the plot legend.
### Default Implementations
- [Equatable Implementations](./ockdataseries/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable

## See Also

### Charts
- [class OCKCartesianChartView](./ockcartesianchartview.md)
- [class OCKCartesianGraphView](./ockcartesiangraphview.md)
  A view that displays a graphable view above an axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockdataseries)*