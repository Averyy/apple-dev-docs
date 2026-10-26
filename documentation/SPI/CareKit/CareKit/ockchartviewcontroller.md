---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewcontroller"
framework: "CareKit/CareKit"
---

# OCKChartViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that displays a chart view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
class OCKChartViewController<ViewSynchronizer> where ViewSynchronizer : ViewSynchronizing, ViewSynchronizer.View : OCKChartDisplayable, ViewSynchronizer.ViewModel == [OCKDataSeries]
```

## Topics

### Initializers
- [init(weekOfDate: Date, configurations: [OCKDataSeriesConfiguration], store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer)](./ockchartviewcontroller/init%28weekofdate,configurations,store,viewsynchronizer%29.md)
  A view controller that displays a chart view and keeps it synchronized with a store.
### Instance Properties
- [var chartView: ViewSynchronizer.View](./ockchartviewcontroller/chartview.md)
  The view that is being synchronized against the store.
### Instance Methods
- [func didSelectChartView(UIView & OCKChartDisplayable)](./ockchartviewcontroller/didselectchartview%28_%29.md)
- [func viewDidLoad()](./ockchartviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- [SynchronizedViewController](./synchronizedviewcontroller.md)
### Inherited By
- [OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
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
- [class OCKCartesianChartViewController](./ockcartesianchartviewcontroller.md)
  A view controller that displays a Cartesian chart view and keeps it synchronized with a store.
- [struct OCKDataSeriesConfiguration](./ockdataseriesconfiguration.md)
  A configuration object that specifies which data to query and how the graph displays it.
- [class OCKCartesianChartViewSynchronizer](./ockcartesianchartviewsynchronizer.md)
  A chart view controller capable of displaying charts drawn on a Cartesian coordinate system.
- [protocol OCKChartViewSynchronizerProtocol](./ockchartviewsynchronizerprotocol.md)
  A protocol that describes a view synchronizer for charts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockchartviewcontroller)*