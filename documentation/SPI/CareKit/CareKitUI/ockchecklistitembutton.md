---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockchecklistitembutton"
framework: "CareKit/CareKitUI"
---

# OCKChecklistItemButton

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A button with an icon and title label.

## Declaration

```swift
@MainActor
class OCKChecklistItemButton
```

## Overview

```
    +--------------------------+
    | [Title]           [Icon] |
    +--------------------------+
```

## Topics

### Initializers
- [init()](./ockchecklistitembutton/init%28%29.md)
- [init?(coder: NSCoder)](./ockchecklistitembutton/init%28coder%29.md)
### Instance Properties
- [let checkmarkButton: OCKCheckmarkButton](./ockchecklistitembutton/checkmarkbutton.md)
  The checkmark button on the trailing end of the view.
- [let contentStackView: OCKStackView](./ockchecklistitembutton/contentstackview.md)
  Holds the main content in the button.
- [let label: OCKLabel](./ockchecklistitembutton/label.md)
  The label on the leading side of the button.
### Instance Methods
- [func setSelected(Bool, animated: Bool)](./ockchecklistitembutton/setselected%28_,animated%29.md)
- [func setStyleForSelectedState(Bool)](./ockchecklistitembutton/setstyleforselectedstate%28_%29.md)
- [func styleDidChange()](./ockchecklistitembutton/styledidchange%28%29.md)

## Relationships

### Inherits From
- [OCKAnimatedButton](./ockanimatedbutton.md)
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
- UIKit.UIContextMenuInteractionDelegate
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

### Multiple care tasks
- [class OCKGridTaskView](./ockgridtaskview.md)
  A card that displays a header, grid of buttons, and a multi-line label In CareKit, this view is intended to display multiple events for a particular task. The state of each button in the grid indicates the completion state of the corresponding event.
- [class OCKChecklistTaskView](./ockchecklisttaskview.md)
  A card that displays a vertically stacked checklist of items. In CareKit, this view is intended to display multiple events for a particular task.
- [class OCKGridTaskCell](./ockgridtaskcell.md)
  A cell used in the `collectionView` of the `OCKGridTaskView`. The cell shows a circular `completionButton` that has an image and a `titleLabel`. The default image is a checkmark.
- [class OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
  OCKCheckmarkButton button with a label.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockchecklistitembutton)*