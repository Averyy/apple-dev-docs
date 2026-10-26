---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskcell"
framework: "CareKit/CareKitUI"
---

# OCKGridTaskCell

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A cell used in the `collectionView` of the `OCKGridTaskView`. The cell shows a circular `completionButton` that has an image and a `titleLabel`. The default image is a checkmark.

## Declaration

```swift
@MainActor
class OCKGridTaskCell
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./ockgridtaskcell/init%28coder%29.md)
- [init(frame: CGRect)](./ockgridtaskcell/init%28frame%29.md)
### Instance Properties
- [let completionButton: OCKLabeledCheckmarkButton](./ockgridtaskcell/completionbutton.md)
  Circular button that shows an image and label. The default image is a checkmark when selected. The text for the deselected state will automatically adapt to the `tintColor`.
### Instance Methods
- [func prepareForReuse()](./ockgridtaskcell/prepareforreuse%28%29.md)

## Relationships

### Inherits From
- UIKit.UICollectionViewCell
### Conforms To
- Foundation.NSCoding
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
- [class OCKChecklistTaskView](./ockchecklisttaskview.md)
  A card that displays a vertically stacked checklist of items. In CareKit, this view is intended to display multiple events for a particular task.
- [class OCKChecklistItemButton](./ockchecklistitembutton.md)
  A button with an icon and title label.
- [class OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
  OCKCheckmarkButton button with a label.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskcell)*