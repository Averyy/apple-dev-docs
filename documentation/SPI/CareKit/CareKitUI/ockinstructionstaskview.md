---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockinstructionstaskview"
framework: "CareKit/CareKitUI"
---

# OCKInstructionsTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays a header, multi-line label, and a completion button.

## Declaration

```swift
@MainActor
class OCKInstructionsTaskView
```

#### Overview

In CareKit, this view displays a particular event for a task. The state of the completion button indicates the completion state of the event.

To insert custom views vertically the view, see `contentStack`.

## Topics

### Instance Properties
- [let completionButton: OCKLabeledButton](./ockinstructionstaskview/completionbutton.md)
  The button on the bottom of the instructions task view.
- [let contentStackView: OCKStackView](./ockinstructionstaskview/contentstackview.md)
  A vertical stack view that holds the main content for the view.
- [var delegate: OCKTaskViewDelegate?](./ockinstructionstaskview/delegate.md)
  An object that handles events related to a task object.
- [let headerView: OCKHeaderView](./ockinstructionstaskview/headerview.md)
  A header view that shows a separator and a detail disclosure image.
- [let instructionsLabel: OCKLabel](./ockinstructionstaskview/instructionslabel.md)
  A multi-line label over the completion button.
### Instance Methods
- [func styleDidChange()](./ockinstructionstaskview/styledidchange%28%29.md)

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

### Single care tasks
- [struct SimpleTaskView](./simpletaskview.md)
  A card that displays a header view and a completion view. The whole view is tappable.
- [class OCKSimpleTaskView](./ocksimpletaskview.md)
  A card that displays an `OCKHeaderView` and a circular checkmark button `completionButton`. In CareKit, this view is intended to display a particular event for a task. The state of the `completionButton` indicates the completion state of the event.
- [struct InstructionsTaskView](./instructionstaskview.md)
  A card that displays a header view, multi-line label, and a completion button.
- [struct CircularCompletionView](./circularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.
- [class OCKCheckmarkButton](./ockcheckmarkbutton.md)
  A button that shows a checkmark in the selected state, and an empty ring in the deselected state.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockinstructionstaskview)*