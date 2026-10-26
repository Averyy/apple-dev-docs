---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdataseriesconfiguration"
framework: "CareKit/CareKit"
---

# OCKDataSeriesConfiguration

**Framework**: CareKit/CareKit  
**Kind**: struct  
**Role**: Structure

A configuration object that specifies which data to query and how the graph displays it.

## Declaration

```swift
struct OCKDataSeriesConfiguration
```

## Topics

### Initializers
- [init(taskID: String, legendTitle: String, gradientStartColor: UIColor, gradientEndColor: UIColor, markerSize: CGFloat, computeProgress: (OCKAnyEvent) -> LinearCareTaskProgress)](./ockdataseriesconfiguration/init%28taskid,legendtitle,gradientstartcolor,gradientendcolor,markersize,computeprogress%29.md)
  Initialize a new `OCKDataSeriesConfiguration`.
### Instance Properties
- [var gradientEndColor: UIColor](./ockdataseriesconfiguration/gradientendcolor.md)
  The second of two colors that will be used in the gradient when plotting the data.
- [var gradientStartColor: UIColor](./ockdataseriesconfiguration/gradientstartcolor.md)
  The first of two colors that will be used in the gradient when plotting the data.
- [var legendTitle: String](./ockdataseriesconfiguration/legendtitle.md)
  The title that will be used to represent this data series in the legend.
- [var markerSize: CGFloat](./ockdataseriesconfiguration/markersize.md)
  The marker size determines the size of the line, bar, or scatter plot elements. The precise behavior is different for each type of plot.
- [var taskID: String](./ockdataseriesconfiguration/taskid.md)
  A user-provided unique id for a task.

## See Also

### Displaying a chart in UIKit
- [class OCKChartViewController](./ockchartviewcontroller.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
- [class OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
  A view controller that displays a Cartesian chart view and keeps it synchronized with a store.
- [class OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
  A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.
- [protocol OCKChartViewSynchronizerProtocol](./ockchartviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for charts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdataseriesconfiguration)*