---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockbuttonlogtaskview"
framework: "CareKit/CareKitUI"
---

# OCKButtonLogTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays a header, multi-line label, a collection of log buttons, and a dynamic vertical stack of logged items. In CareKit, this view is intended to display a particular event for a task. When the log button is presses, a new outcome is created for the event.

## Declaration

```swift
@MainActor
class OCKButtonLogTaskView
```

#### Overview

See `logButtonsCollectionView` to customize the layout or number of log buttons.

To insert custom views vertically the view, see `contentStack`. To modify the logged items, see `updateItem`, `appendItem`, `insertItem`, `removeItem` and `clearItems`.

```
    +-------------------------------------------------------+
    |                                                       |
    | [title]                                [detail        |
    | [detail]                               disclosure]    |
    |                                                       |
    |                                                       |
    |  --------------------------------------------------   |
    |                                                       |
    |   [instructions]                                      |
    |                                                       |
    |   +-----------------------------------------------+   |
    |   |                 [log button]                  |   |
    |   +-----------------------------------------------+   |
    |                                                       |
    |   [img]  [detail]  [title]                            |
    |   -------------------------------------------------   |
    |   [img]  [detail]  [title]                            |
    |   -------------------------------------------------   |
    |   ...                                                 |
    |   ...                                                 |
    |   -------------------------------------------------   |
    |   [img]  [detail]  [title]                            |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Instance Properties
- [let instructionsLabel: OCKLabel](./ockbuttonlogtaskview/instructionslabel.md)
  Multi-line label below the header.
- [var logButtonsCollectionView: UICollectionView!](./ockbuttonlogtaskview/logbuttonscollectionview.md)
  Collection view holding the log buttons.
### Instance Methods
- [func collectionView(UICollectionView, cellForItemAt: IndexPath) -> UICollectionViewCell](./ockbuttonlogtaskview/collectionview%28_,cellforitemat%29.md)
- [func collectionView(UICollectionView, numberOfItemsInSection: Int) -> Int](./ockbuttonlogtaskview/collectionview%28_,numberofitemsinsection%29.md)
- [func styleDidChange()](./ockbuttonlogtaskview/styledidchange%28%29.md)
### Type Aliases
- [OCKButtonLogTaskView.DefaultCellType](./ockbuttonlogtaskview/defaultcelltype.md)
  The default cell type used for the `logButtonCollectionView`.
### Type Properties
- [static let defaultCellIdentifier: String](./ockbuttonlogtaskview/defaultcellidentifier.md)
  The identifier used for the default cell in the `logButtonCollectionView`.

## Relationships

### Inherits From
- [OCKLogTaskView](./ocklogtaskview.md)
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
- UIKit.UICollectionViewDataSource
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

### Log-based care tasks
- [class OCKLogTaskView](./ocklogtaskview.md)
  Base class for all log view. Shows an `OCKHeaderView` and a dynamic stack view of log items.
- [class OCKLogButtonCell](./ocklogbuttoncell.md)
- [class OCKLogItemButton](./ocklogitembutton.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockbuttonlogtaskview)*