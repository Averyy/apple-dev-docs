---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogtaskview"
framework: "CareKit/CareKitUI"
---

# OCKLogTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

Base class for all log view. Shows an `OCKHeaderView` and a dynamic stack view of log items.

## Declaration

```swift
@MainActor
class OCKLogTaskView
```

## Topics

### Instance Properties
- [let contentStackView: OCKStackView](./ocklogtaskview/contentstackview.md)
  A vertical stack view that holds the main content for the view.
- [var delegate: OCKTaskViewDelegate?](./ocklogtaskview/delegate.md)
  An object that handles events related to a task object.
- [let headerView: OCKHeaderView](./ocklogtaskview/headerview.md)
  The header view that shows a separator and a detailed disclosure image.
- [var items: [OCKLogItemButton]](./ocklogtaskview/items.md)
  The list of buttons in the log.
### Instance Methods
- [func appendItem(withTitle: String?, detail: String?, animated: Bool) -> OCKLogItemButton](./ocklogtaskview/appenditem%28withtitle,detail,animated%29.md)
  Appends an item to the list of logged items.
- [func clearItems(animated: Bool)](./ocklogtaskview/clearitems%28animated%29.md)
  Clear all items from the list of logged items.
- [func insertItem(withTitle: String?, detail: String?, at: Int, animated: Bool) -> OCKLogItemButton](./ocklogtaskview/insertitem%28withtitle,detail,at,animated%29.md)
  Inserts an item in the list of logged items.
- [func removeItem(at: Int, animated: Bool) -> OCKLogItemButton?](./ocklogtaskview/removeitem%28at,animated%29.md)
  Remove an item from the list of logged items.
- [func styleDidChange()](./ocklogtaskview/styledidchange%28%29.md)
- [func updateItem(at: Int, withTitle: String?, detail: String?) -> OCKLogItemButton?](./ocklogtaskview/updateitem%28at,withtitle,detail%29.md)
  Updates the text for an item at a particular index.

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Inherited By
- [OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
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

### Log-based care tasks
- [class OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
  A card that displays a header, multi-line label, a collection of log buttons, and a dynamic vertical stack of logged items. In CareKit, this view is intended to display a particular event for a task. When the log button is presses, a new outcome is created for the event.
- [class OCKLogButtonCell](./ocklogbuttoncell.md)
- [class OCKLogItemButton](./ocklogitembutton.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogtaskview)*