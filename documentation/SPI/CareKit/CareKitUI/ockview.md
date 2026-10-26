---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockview"
framework: "CareKit/CareKitUI"
---

# OCKView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

## Declaration

```swift
@MainActor
class OCKView
```

## Topics

### Initializers
- [init()](./ockview/init%28%29.md)
- [init?(coder: NSCoder)](./ockview/init%28coder%29.md)
- [init(frame: CGRect)](./ockview/init%28frame%29.md)
### Instance Properties
- [var customStyle: OCKStyler?](./ockview/customstyle.md)
### Instance Methods
- [func didMoveToSuperview()](./ockview/didmovetosuperview%28%29.md)
- [func removeFromSuperview()](./ockview/removefromsuperview%28%29.md)
- [func styleDidChange()](./ockview/styledidchange%28%29.md)
### Default Implementations
- [OCKStylable Implementations](./ockview/ockstylable-implementations.md)

## Relationships

### Inherits From
- UIKit.UIView
### Inherited By
- [OCKCartesianChartView](./ockcartesianchartview.md)
- [OCKCartesianGraphView](./ockcartesiangraphview.md)
- [OCKChecklistTaskView](./ockchecklisttaskview.md)
- [OCKCompletionRingView](./ockcompletionringview.md)
- [OCKDetailView](./ockdetailview.md)
- [OCKDetailedContactView](./ockdetailedcontactview.md)
- [OCKFeaturedContentView](./ockfeaturedcontentview.md)
- [OCKGridTaskView](./ockgridtaskview.md)
- [OCKHeaderView](./ockheaderview.md)
- [OCKInstructionsTaskView](./ockinstructionstaskview.md)
- [OCKLogTaskView](./ocklogtaskview.md)
- [OCKSeparatorView](./ockseparatorview.md)
- [OCKSimpleContactView](./ocksimplecontactview.md)
- [OCKSimpleTaskView](./ocksimpletaskview.md)
- [OCKWeekCalendarView](./ockweekcalendarview.md)
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

### Common view components
- [struct CardView](./cardview.md)
  A card whose content can be injected.
- [protocol OCKCardable](./ockcardable.md)
  Has the ability to display one’s self as a card. A card has a particular corner radius and shadow.
- [struct HeaderView](./headerview.md)
  Header used for most CareKit cards.
- [class OCKHeaderView](./ockheaderview.md)
  A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.
- [class OCKStackView](./ockstackview.md)
  A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.
- [class OCKSeparatorView](./ockseparatorview.md)
  Horizontal separator view.
- [class OCKLabel](./ocklabel.md)
  A label that handles animating state changes and provides accessibility features.
- [class OCKLabeledButton](./ocklabeledbutton.md)
  A button with a filled background color.
- [class OCKAnimatedButton](./ockanimatedbutton.md)
  A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockview)*