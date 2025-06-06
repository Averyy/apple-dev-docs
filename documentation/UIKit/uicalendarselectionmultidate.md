# UICalendarSelectionMultiDate

**Framework**: UIKit  
**Kind**: class

An object that tracks multiple dates the user selects from a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICalendarSelectionMultiDate
```

## Topics

### Creating a multiple date selection
- [init(delegate: (any UICalendarSelectionMultiDateDelegate)?)](uicalendarselectionmultidate/init(delegate:).md)
  Creates an object that tracks multiple dates a user selects from a calendar view, with an optional delegate to manage selectable dates and selection changes.
### Setting the selection delegate
- [var delegate: (any UICalendarSelectionMultiDateDelegate)?](uicalendarselectionmultidate/delegate.md)
  A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.
- [protocol UICalendarSelectionMultiDateDelegate](uicalendarselectionmultidatedelegate.md)
  A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.
### Updating the selected dates
- [var selectedDates: [DateComponents]](uicalendarselectionmultidate/selecteddates.md)
  An array of date component objects that represent selected dates in a calendar view.
- [func setSelectedDates([DateComponents], animated: Bool)](uicalendarselectionmultidate/setselecteddates(_:animated:).md)
  Updates the array of date component objects that represent selected dates in a calendar view, with an option to animate the change.

## Relationships

### Inherits From
- [UICalendarSelection](uicalendarselection.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selectionBehavior: UICalendarSelection?](uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionSingleDate](uicalendarselectionsingledate.md)
  An object that tracks a date the user selects from a calendar view.
- [class UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md)
  An object that tracks a specific week a person selects from a calendar view.
- [class UICalendarSelection](uicalendarselection.md)
  A base object that tracks one or more dates a user selects from a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate)*