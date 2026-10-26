---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewsynchronizer"
framework: "CareKit/CareKit"
---

# OCKCartesianChartViewSynchronizer

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.

## Declaration

```swift
class OCKCartesianChartViewSynchronizer
```

## Topics

### Initializers
- [init(plotType: OCKCartesianGraphView.PlotType, selectedDate: Date)](./ockcartesianchartviewsynchronizer/init%28plottype,selecteddate%29.md)
  Initialize by providing a chart type and date.
### Instance Properties
- [let plotType: OCKCartesianGraphView.PlotType](./ockcartesianchartviewsynchronizer/plottype.md)
  The type of the plot that this view controller displays.
- [let selectedDate: Date](./ockcartesianchartviewsynchronizer/selecteddate.md)
  The currently selected date.
### Instance Methods
- [func makeView() -> OCKCartesianChartView](./ockcartesianchartviewsynchronizer/makeview%28%29.md)
- [func updateView(OCKCartesianChartView, context: OCKSynchronizationContext<[OCKDataSeries]>)](./ockcartesianchartviewsynchronizer/updateview%28_,context%29.md)

## Relationships

### Conforms To
- [ViewSynchronizing](./viewsynchronizing.md)

## See Also

### Displaying a chart in UIKit
- [class OCKChartViewController](./ockchartviewcontroller.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
- [class OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
  A view controller that displays a Cartesian chart view and keeps it synchronized with a store.
- [struct OCKDataSeriesConfiguration](./ockdataseriesconfiguration.md)
  A configuration object that specifies which data to query and how the graph displays it.
- [protocol OCKChartViewSynchronizerProtocol](./ockchartviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for charts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewsynchronizer)*