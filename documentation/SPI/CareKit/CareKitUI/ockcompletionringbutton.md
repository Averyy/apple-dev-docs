---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcompletionringbutton"
framework: "CareKit/CareKitUI"
---

# OCKCompletionRingButton

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A selectable completion ring with an inner check view and a title label.

## Declaration

```swift
@MainActor
class OCKCompletionRingButton
```

## Topics

### Initializers
- [init()](./ockcompletionringbutton/init%28%29.md)
- [init?(coder: NSCoder)](./ockcompletionringbutton/init%28coder%29.md)
### Instance Properties
- [var completionState: OCKCompletionState](./ockcompletionringbutton/completionstate.md)
  The completion state of the ring
- [let contentStackView: OCKStackView](./ockcompletionringbutton/contentstackview.md)
- [let label: OCKLabel](./ockcompletionringbutton/label.md)
  Label above the completion ring.
- [let ring: OCKCompletionRingView](./ockcompletionringbutton/ring.md)
  A fillable ring view.
### Instance Methods
- [func setState(OCKCompletionState, animated: Bool)](./ockcompletionringbutton/setstate%28_,animated%29.md)
  Changes the display state of the button
- [func setStyleForSelectedState(Bool)](./ockcompletionringbutton/setstyleforselectedstate%28_%29.md)
- [func styleDidChange()](./ockcompletionringbutton/styledidchange%28%29.md)
- [func tintColorDidChange()](./ockcompletionringbutton/tintcolordidchange%28%29.md)
  Called when the tint color of the view changes.

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

### Calendar
- [class OCKWeekCalendarView](./ockweekcalendarview.md)
  A horizontal row of seven selectable completion rings and corresponding labels.
- [class OCKCompletionRingView](./ockcompletionringview.md)
  A fillable ring with an inner checkmark.
- [enum OCKCompletionState](./ockcompletionstate.md)
  A completion state that marks progress.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcompletionringbutton)*