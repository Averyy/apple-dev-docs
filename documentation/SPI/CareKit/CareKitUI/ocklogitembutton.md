---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogitembutton"
framework: "CareKit/CareKitUI"
---

# OCKLogItemButton

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

## Declaration

```swift
@MainActor
class OCKLogItemButton
```

## Topics

### Initializers
- [init()](./ocklogitembutton/init%28%29.md)
- [init?(coder: NSCoder)](./ocklogitembutton/init%28coder%29.md)
### Instance Properties
- [let contentStackView: OCKStackView](./ocklogitembutton/contentstackview.md)
  Holds the main content in the button.
- [let detailLabel: OCKLabel](./ocklogitembutton/detaillabel.md)
  Tinted accessory label.
- [let imageView: UIImageView](./ocklogitembutton/imageview.md)
  The icon on the leading end of the button.
- [let titleLabel: OCKLabel](./ocklogitembutton/titlelabel.md)
  Main content label.
### Instance Methods
- [func styleDidChange()](./ocklogitembutton/styledidchange%28%29.md)
- [func tintColorDidChange()](./ocklogitembutton/tintcolordidchange%28%29.md)

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

### Log-based care tasks
- [class OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
  A card that displays a header, multi-line label, a collection of log buttons, and a dynamic vertical stack of logged items. In CareKit, this view is intended to display a particular event for a task. When the log button is presses, a new outcome is created for the event.
- [class OCKLogTaskView](./ocklogtaskview.md)
  Base class for all log view. Shows an `OCKHeaderView` and a dynamic stack view of log items.
- [class OCKLogButtonCell](./ocklogbuttoncell.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogitembutton)*