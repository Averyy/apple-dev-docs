---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller"
framework: "CareKit/CareKit"
---

# OCKCartesianChartViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a Cartesian chart view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
class OCKCartesianChartViewController
```

## Topics

### Initializers
- [init(plotType: OCKCartesianGraphView.PlotType, selectedDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol)](./ockcartesianchartviewcontroller/init%28plottype,selecteddate,configurations,store%29.md)
  Creates a view controller that displays a chart view and keeps it synchronized with a store.
- [init(weekOfDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol, viewSynchronizer: OCKCartesianChartViewSynchronizer)](./ockcartesianchartviewcontroller/init%28weekofdate,configurations,store,viewsynchronizer%29.md)
  Creates a view controller that displays a chart view and keeps it synchronized with a store.

## Relationships

### Inherits From
- [OCKChartViewController](./ockchartviewcontroller.md)
### Conforms To
- CareKitUI.OCKChartViewDelegate
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- ObjectiveC.NSObjectProtocol
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearanceContainer
- UIKit.UIContentContainer
- UIKit.UIFocusEnvironment
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIResponderStandardEditActions
- UIKit.UIStateRestoring
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring

## See Also

### Displaying a chart in UIKit
- [class OCKChartViewController](./ockchartviewcontroller.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
- [struct OCKDataSeriesConfiguration](./ockdataseriesconfiguration.md)
  A configuration object that specifies which data to query and how the graph displays it.
- [class OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
  A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.
- [protocol OCKChartViewSynchronizerProtocol](./ockchartviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for charts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcartesianchartviewcontroller)*