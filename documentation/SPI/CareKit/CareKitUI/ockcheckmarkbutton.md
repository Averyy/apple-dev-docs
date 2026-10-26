---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcheckmarkbutton"
framework: "CareKit/CareKitUI"
---

# OCKCheckmarkButton

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A button that shows a checkmark in the selected state, and an empty ring in the deselected state.

## Declaration

```swift
@MainActor
class OCKCheckmarkButton
```

## Topics

### Initializers
- [init()](./ockcheckmarkbutton/init%28%29.md)
### Instance Properties
- [let imageView: UIImageView](./ockcheckmarkbutton/imageview.md)
  Checkmark image in the center of the view.
- [var intrinsicContentSize: CGSize](./ockcheckmarkbutton/intrinsiccontentsize.md)
### Instance Methods
- [func layoutSubviews()](./ockcheckmarkbutton/layoutsubviews%28%29.md)
- [func setSelected(Bool, animated: Bool)](./ockcheckmarkbutton/setselected%28_,animated%29.md)
- [func setStyleForSelectedState(Bool)](./ockcheckmarkbutton/setstyleforselectedstate%28_%29.md)
- [func styleDidChange()](./ockcheckmarkbutton/styledidchange%28%29.md)
- [func tintColorDidChange()](./ockcheckmarkbutton/tintcolordidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ockcheckmarkbutton/traitcollectiondidchange%28_%29.md)

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

### Single care tasks
- [struct SimpleTaskView](./simpletaskview.md)
  A card that displays a header view and a completion view. The whole view is tappable.
- [class OCKSimpleTaskView](./ocksimpletaskview.md)
  A card that displays an `OCKHeaderView` and a circular checkmark button `completionButton`. In CareKit, this view is intended to display a particular event for a task. The state of the `completionButton` indicates the completion state of the event.
- [struct InstructionsTaskView](./instructionstaskview.md)
  A card that displays a header view, multi-line label, and a completion button.
- [class OCKInstructionsTaskView](./ockinstructionstaskview.md)
  A card that displays a header, multi-line label, and a completion button.
- [struct CircularCompletionView](./circularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcheckmarkbutton)*