---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcartesianchartview"
framework: "CareKit/CareKitUI"
---

# OCKCartesianChartView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

## Declaration

```swift
@MainActor
class OCKCartesianChartView
```

## Topics

### Initializers
- [init(type: OCKCartesianGraphView.PlotType)](./ockcartesianchartview/init%28type%29.md)
  Creates a chart with a specified type.
### Instance Properties
- [let contentStackView: OCKStackView](./ockcartesianchartview/contentstackview.md)
  A vertical stack view that contains the primary content in the chart view.
- [var delegate: OCKChartViewDelegate?](./ockcartesianchartview/delegate.md)
  An object that handles events related to a chart object.
- [let graphView: OCKCartesianGraphView](./ockcartesianchartview/graphview.md)
  The main content of the view.
- [let headerView: OCKHeaderView](./ockcartesianchartview/headerview.md)
  A default header view.
### Instance Methods
- [func styleDidChange()](./ockcartesianchartview/styledidchange%28%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKChartDisplayable](./ockchartdisplayable.md)
- [OCKStylable](./ockstylable.md)
- ObjectiveC.NSObjectProtocol
- QuartzCore.CALayerDelegate
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIAccessibilityIdentification
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearance
- UIKit.UIAppearanceContainer
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIPopoverPresentationControllerSourceItem
- UIKit.UIResponderStandardEditActions
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace

## See Also

### Charts
- [class OCKCartesianGraphView](./ockcartesiangraphview.md)
  A view that displays a graphable view above an axis.
- [struct OCKDataSeries](./ockdataseries.md)
  Represents a single group of data to be plotted. In most cases, CareKit plots accept multiple data series, allowing for for several data series to be plotted on a single axis for easy comparison.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcartesianchartview)*