# UICalendarSelectionSingleDate

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that tracks a date the user selects from a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICalendarSelectionSingleDate
```

```objc
@interface UICalendarSelectionSingleDate : UICalendarSelection
```

## Topics

### Creating a single date selection
- [init(delegate: (any UICalendarSelectionSingleDateDelegate)?)](./uicalendarselectionsingledate/init%28delegate%29.md)
  Creates an object that tracks a date a user selects from a calendar view, with an optional delegate to manage selectable dates and selection changes.
### Setting the selection delegate
- [var delegate: (any UICalendarSelectionSingleDateDelegate)?](./uicalendarselectionsingledate/delegate.md)
  A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.
- [protocol UICalendarSelectionSingleDateDelegate](./uicalendarselectionsingledatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.
### Updating the selected date
- [var selectedDate: DateComponents?](./uicalendarselectionsingledate/selecteddate.md)
  A date component object that represents a selected date in a calendar view.
- [func setSelected(DateComponents?, animated: Bool)](./uicalendarselectionsingledate/setselected%28_,animated%29.md)
  Updates the date component object that represents a selected date in a calendar view, with an option to animate the change.

## Relationships

### Inherits From
- [UICalendarSelection](./uicalendarselection.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling date selections
- [var selectionBehavior: UICalendarSelection?](./uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionMultiDate](./uicalendarselectionmultidate.md)
  An object that tracks multiple dates the user selects from a calendar view.
- [class UICalendarSelectionWeekOfYear](./uicalendarselectionweekofyear.md)
  An object that tracks a specific week a person selects from a calendar view.
- [class UICalendarSelection](./uicalendarselection.md)
  A base object that tracks one or more dates a user selects from a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate)*