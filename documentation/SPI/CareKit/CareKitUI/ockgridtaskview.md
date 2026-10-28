---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskview"
framework: "CareKit/CareKitUI"
---

# OCKGridTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays a header, grid of buttons, and a multi-line label In CareKit, this view is intended to display multiple events for a particular task. The state of each button in the grid indicates the completion state of the corresponding event.

## Declaration

```swift
@MainActor
class OCKGridTaskView
```

## Overview

To insert custom views vertically the view, see `contentStack`. To modify the data in the grid, set a `dataSource` for the `collectionView`.

## Topics

### Instance Properties
- [var collectionView: UICollectionView](./ockgridtaskview/collectionview.md)
  A collection view that sizes itself based on the size of its content.
- [let contentStackView: OCKStackView](./ockgridtaskview/contentstackview.md)
  The vertical stack view that holds the main content in the view.
- [var delegate: OCKTaskViewDelegate?](./ockgridtaskview/delegate.md)
  An object that handles events related to a task object.
- [let headerView: OCKHeaderView](./ockgridtaskview/headerview.md)
  A header view that shows a separator and a detail disclosure image.
- [let instructionsLabel: OCKLabel](./ockgridtaskview/instructionslabel.md)
  A multi-line label below the collection view.
### Instance Methods
- [func collectionView(UICollectionView, didSelectItemAt: IndexPath)](./ockgridtaskview/collectionview%28_,didselectitemat%29.md)
- [func styleDidChange()](./ockgridtaskview/styledidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ockgridtaskview/traitcollectiondidchange%28_%29.md)
### Type Aliases
- [OCKGridTaskView.DefaultCellType](./ockgridtaskview/defaultcelltype.md)
  The default cell type for the collection view.
### Type Properties
- [static let defaultCellIdentifier: String](./ockgridtaskview/defaultcellidentifier.md)
  The default cell identifier registered for the collection view.

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKStylable](./ockstylable.md)
- [OCKTaskDisplayable](./ocktaskdisplayable.md)
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
- UIKit.UICollectionViewDelegate
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIPopoverPresentationControllerSourceItem
- UIKit.UIResponderStandardEditActions
- UIKit.UIScrollViewDelegate
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace

## See Also

### Multiple care tasks
- [class OCKChecklistTaskView](./ockchecklisttaskview.md)
  A card that displays a vertically stacked checklist of items. In CareKit, this view is intended to display multiple events for a particular task.
- [class OCKChecklistItemButton](./ockchecklistitembutton.md)
  A button with an icon and title label.
- [class OCKGridTaskCell](./ockgridtaskcell.md)
  A cell used in the `collectionView` of the `OCKGridTaskView`. The cell shows a circular `completionButton` that has an image and a `titleLabel`. The default image is a checkmark.
- [class OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
  OCKCheckmarkButton button with a label.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskview)*