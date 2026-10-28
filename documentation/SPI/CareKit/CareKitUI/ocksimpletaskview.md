---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocksimpletaskview"
framework: "CareKit/CareKitUI"
---

# OCKSimpleTaskView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A card that displays an `OCKHeaderView` and a circular checkmark button `completionButton`. In CareKit, this view is intended to display a particular event for a task. The state of the `completionButton` indicates the completion state of the event.

## Declaration

```swift
@MainActor
class OCKSimpleTaskView
```

## Overview

To insert custom views vertically the view, see `contentStack`

```
    +-------------------------------------------------------+
    |                                                       |
    | [title]                                 [completion   |
    | [detail]                                 button]      |
    |                                                       |
    +-------------------------------------------------------+
```

## Topics

### Instance Properties
- [let completionButton: OCKCheckmarkButton](./ocksimpletaskview/completionbutton.md)
  The button in the trailing end of the card.
- [var delegate: OCKTaskViewDelegate?](./ocksimpletaskview/delegate.md)
  An object that handles events related to a task object.
- [let headerView: OCKHeaderView](./ocksimpletaskview/headerview.md)
  A default implementation of a header view.
### Instance Methods
- [func styleDidChange()](./ocksimpletaskview/styledidchange%28%29.md)

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
- [struct InstructionsTaskView](./instructionstaskview.md)
  A card that displays a header view, multi-line label, and a completion button.
- [class OCKInstructionsTaskView](./ockinstructionstaskview.md)
  A card that displays a header, multi-line label, and a completion button.
- [struct CircularCompletionView](./circularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.
- [class OCKCheckmarkButton](./ockcheckmarkbutton.md)
  A button that shows a checkmark in the selected state, and an empty ring in the deselected state.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocksimpletaskview)*