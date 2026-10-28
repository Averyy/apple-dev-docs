---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcartesiangraphview"
framework: "CareKit/CareKitUI"
---

# OCKCartesianGraphView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A view that displays a graphable view above an axis.

## Declaration

```swift
@MainActor
class OCKCartesianGraphView
```

## Overview

The initializer takes a `PlotType` that allows you to choose from several common graph types.

## Topics

### Initializers
- [init(type: PlotType)](./ockcartesiangraphview/init%28type%29.md)
  Creates a graph view with the specified style.
### Instance Properties
- [var dataSeries: [OCKDataSeries]](./ockcartesiangraphview/dataseries.md)
  The data points in the graph.
- [var horizontalAxisMarkers: [String]](./ockcartesiangraphview/horizontalaxismarkers.md)
  The labels for the horizontal axis.
- [var numberFormatter: NumberFormatter](./ockcartesiangraphview/numberformatter.md)
  A number formatter for the vertical axis values.
- [var selectedIndex: Int?](./ockcartesiangraphview/selectedindex.md)
  The index of the selected label in the x-axis.
- [var xMaximum: CGFloat?](./ockcartesiangraphview/xmaximum.md)
  The maximum x value in the graph.
- [var xMinimum: CGFloat?](./ockcartesiangraphview/xminimum.md)
  The minimum x value in the graph.
- [var yMaximum: CGFloat?](./ockcartesiangraphview/ymaximum.md)
  The maximum y value in the graph.
- [var yMinimum: CGFloat?](./ockcartesiangraphview/yminimum.md)
  The minimum y value in the graph.
### Instance Methods
- [func graphBounds() -> CGRect](./ockcartesiangraphview/graphbounds%28%29.md)
  Gets the bounds of the graph.
- [func tintColorDidChange()](./ockcartesiangraphview/tintcolordidchange%28%29.md)
### Enumerations
- [OCKCartesianGraphView.PlotType](./ockcartesiangraphview/plottype.md)
  An enumeration that specifies the types of plots this view can display.

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
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
- [class OCKCartesianChartView](./ockcartesianchartview.md)
- [struct OCKDataSeries](./ockdataseries.md)
  Represents a single group of data to be plotted. In most cases, CareKit plots accept multiple data series, allowing for for several data series to be plotted on a single axis for easy comparison.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcartesiangraphview)*