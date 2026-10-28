---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockweekcalendarview"
framework: "CareKit/CareKitUI"
---

# OCKWeekCalendarView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A horizontal row of seven selectable completion rings and corresponding labels.

## Declaration

```swift
@MainActor
class OCKWeekCalendarView
```

## Overview

```
+--------------------------------------+
|  [title] [title] [title]     [title] |
|                                      |
|    o o     o o     o o         o o   |
|   o   o   o   o   o   o  ...  o   o  |
|    o o     o o     o o         o o   |
+--------------------------------------+
```

## Topics

### Initializers
- [init(weekOfDate: Date)](./ockweekcalendarview/init%28weekofdate%29.md)
  A view that displays interactable completion rings for each day in a week. The week is computed based on the provided date parameter.
### Instance Properties
- [var completionRingButtons: [OCKCompletionRingButton]](./ockweekcalendarview/completionringbuttons.md)
  The completion ring buttons in the view. There will be one ring for each day in the `dateInterval`.
- [var dateInterval: DateInterval](./ockweekcalendarview/dateinterval.md)
  The date interval of the week currently being displayed.
- [var delegate: OCKCalendarViewDelegate?](./ockweekcalendarview/delegate.md)
  An object that handles events related to a calendar object.
- [var selectedDate: Date](./ockweekcalendarview/selecteddate.md)
  The currently selected date in the calendar.
### Instance Methods
- [func completionRingFor(date: Date) -> OCKCompletionRingButton?](./ockweekcalendarview/completionringfor%28date%29.md)
  Get the completion ring that corresponds to a particular date.
- [func selectDate(Date)](./ockweekcalendarview/selectdate%28_%29.md)
  Select the completion ring that corresponds to the given date.
- [func showDate(Date)](./ockweekcalendarview/showdate%28_%29.md)
  Display the week for the given date. Each ring will correspond to one day in the week.
- [func styleDidChange()](./ockweekcalendarview/styledidchange%28%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKCalendarDisplayable](./ockcalendardisplayable.md)
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
- [class OCKCompletionRingButton](./ockcompletionringbutton.md)
  A selectable completion ring with an inner check view and a title label.
- [class OCKCompletionRingView](./ockcompletionringview.md)
  A fillable ring with an inner checkmark.
- [enum OCKCompletionState](./ockcompletionstate.md)
  A completion state that marks progress.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockweekcalendarview)*