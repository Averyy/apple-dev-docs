---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewsynchronizerprotocol"
framework: "CareKit/CareKit"
---

# OCKChartViewSynchronizerProtocol

**Framework**: CareKit/CareKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that describes a view synchronizer for charts.

## Declaration

```swift
protocol OCKChartViewSynchronizerProtocol
```

## Topics

### Associated Types
- [associatedtype View : UIView, OCKChartDisplayable](./ockchartviewsynchronizerprotocol/view.md)
  The type of the view that will be synchronized
### Instance Methods
- [func makeView() -> View](./ockchartviewsynchronizerprotocol/makeview%28%29.md)
  Initialize a view to be synchronized.
- [func updateView(View, context: OCKSynchronizationContext<[OCKDataSeries]>)](./ockchartviewsynchronizerprotocol/updateview%28_,context%29.md)
  Update a view using the given context.

## See Also

### Displaying a chart in UIKit
- [class OCKChartViewController](./ockchartviewcontroller.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
- [class OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
  A view controller that displays a Cartesian chart view and keeps it synchronized with a store.
- [struct OCKDataSeriesConfiguration](./ockdataseriesconfiguration.md)
  A configuration object that specifies which data to query and how the graph displays it.
- [class OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
  A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewsynchronizerprotocol)*