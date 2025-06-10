# UICalendarSelectionWeekOfYear

**Framework**: UIKit  
**Kind**: class

An object that tracks a specific week a person selects from a calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UICalendarSelectionWeekOfYear
```

#### Overview

Use the [`UICalendarSelectionWeekOfYear`](uicalendarselectionweekofyear.md) selection behavior to allow selecting dates in a calendar view by week. The following code example shows how to configure a calendar view’s selection behavior to use week-of-year selection:

```swift
// Create a calendar view.
let calendarView = UICalendarView()
calendarView.calendar = Calendar(identifier: .gregorian)

// Set the selection behavior.
let selection = UICalendarSelectionWeekOfYear(delegate: self)
calendarView.selectionBehavior = selection

// Set the 11th week in the year 2024.
selection.selectedWeekOfYear = DateComponents(
    calendar: Calendar(identifier: .gregorian),
    weekOfYear: 11,
    yearForWeekOfYear: 2024)
```

## Topics

### Creating a week-of-year selection
- [init(delegate: (any UICalendarSelectionWeekOfYearDelegate)?)](uicalendarselectionweekofyear/init(delegate:).md)
  Creates an object that tracks a week a person selects from a calendar view, with an optional delegate to manage selectable weeks and selection changes.
### Setting the selection delegate
- [var delegate: (any UICalendarSelectionWeekOfYearDelegate)?](uicalendarselectionweekofyear/delegate.md)
  A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.
- [protocol UICalendarSelectionWeekOfYearDelegate](uicalendarselectionweekofyeardelegate.md)
  A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.
### Updating the selected week
- [var selectedWeekOfYear: DateComponents?](uicalendarselectionweekofyear/selectedweekofyear.md)
  The current week-of-year selection in the calendar view.
- [func setSelected(DateComponents?, animated: Bool)](uicalendarselectionweekofyear/setselected(_:animated:).md)
  Updates the date component object that represents a selected week in a calendar view, with an option to animate the change.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var selectionBehavior: UICalendarSelection?](uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionSingleDate](uicalendarselectionsingledate.md)
  An object that tracks a date the user selects from a calendar view.
- [class UICalendarSelectionMultiDate](uicalendarselectionmultidate.md)
  An object that tracks multiple dates the user selects from a calendar view.
- [class UICalendarSelection](uicalendarselection.md)
  A base object that tracks one or more dates a user selects from a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear)*