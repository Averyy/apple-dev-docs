---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogbuttoncell"
framework: "CareKit/CareKitUI"
---

# OCKLogButtonCell

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

## Declaration

```swift
@MainActor
class OCKLogButtonCell
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./ocklogbuttoncell/init%28coder%29.md)
- [init(frame: CGRect)](./ocklogbuttoncell/init%28frame%29.md)
### Instance Properties
- [let logButton: OCKLabeledButton](./ocklogbuttoncell/logbutton.md)
### Instance Methods
- [func prepareForReuse()](./ocklogbuttoncell/prepareforreuse%28%29.md)

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

### Log-based care tasks
- [class OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
  A card that displays a header, multi-line label, a collection of log buttons, and a dynamic vertical stack of logged items. In CareKit, this view is intended to display a particular event for a task. When the log button is presses, a new outcome is created for the event.
- [class OCKLogTaskView](./ocklogtaskview.md)
  Base class for all log view. Shows an `OCKHeaderView` and a dynamic stack view of log items.
- [class OCKLogItemButton](./ocklogitembutton.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogbuttoncell)*