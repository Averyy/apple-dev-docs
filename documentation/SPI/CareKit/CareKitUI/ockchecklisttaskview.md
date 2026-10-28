---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockchecklisttaskview"
framework: "CareKit/CareKitUI"
---

# OCKChecklistTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays a vertically stacked checklist of items. In CareKit, this view is intended to display multiple events for a particular task.

## Declaration

```swift
@MainActor
class OCKChecklistTaskView
```

## Overview

To insert custom views vertically the view, see `contentStack`. The header is an `OCKHeaderView`. The body has a stack of checklist items and an instructions label underneath. To access the checklist item buttons, for instance to hook them up to target actions, see the `items` array. To modify the checklist, see `updateItem`, `appendItem`, `insertItem`, `removeItem` and `clearItems`.

## Topics

### Instance Properties
- [let contentStackView: OCKStackView](./ockchecklisttaskview/contentstackview.md)
  The vertical stack view that holds the main content in the view.
- [var delegate: OCKTaskViewDelegate?](./ockchecklisttaskview/delegate.md)
  An object that handles events related to a task object.
- [let headerView: OCKHeaderView](./ockchecklisttaskview/headerview.md)
  A header that shows a detailed disclosure image.
- [let instructionsLabel: OCKLabel](./ockchecklisttaskview/instructionslabel.md)
  Multi-line label beneath the checklist items.
- [var items: [OCKChecklistItemButton]](./ockchecklisttaskview/items.md)
  The buttons in the checklist.
### Instance Methods
- [func appendItem(withTitle: String, animated: Bool) -> OCKChecklistItemButton](./ockchecklisttaskview/appenditem%28withtitle,animated%29.md)
  Append an item to the checklist.
- [func clearItems(animated: Bool)](./ockchecklisttaskview/clearitems%28animated%29.md)
  Clear all items from the checklist.
- [func insertItem(withTitle: String, at: Int, animated: Bool) -> OCKChecklistItemButton](./ockchecklisttaskview/insertitem%28withtitle,at,animated%29.md)
  Insert an item in the checklist.
- [func removeItem(at: Int, animated: Bool) -> OCKChecklistItemButton?](./ockchecklisttaskview/removeitem%28at,animated%29.md)
  Remove an item from the checklist.
- [func styleDidChange()](./ockchecklisttaskview/styledidchange%28%29.md)
- [func updateItem(at: Int, withTitle: String) -> OCKChecklistItemButton?](./ockchecklisttaskview/updateitem%28at,withtitle%29.md)
  Update an item with text.

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
- [class OCKChecklistItemButton](./ockchecklistitembutton.md)
  A button with an icon and title label.
- [class OCKGridTaskCell](./ockgridtaskcell.md)
  A cell used in the `collectionView` of the `OCKGridTaskView`. The cell shows a circular `completionButton` that has an image and a `titleLabel`. The default image is a checkmark.
- [class OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
  OCKCheckmarkButton button with a label.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockchecklisttaskview)*