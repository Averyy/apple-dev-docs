# UICalendarSelectionWeekOfYearDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol UICalendarSelectionWeekOfYearDelegate : NSObjectProtocol
```

## Topics

### Handling week-of-year selections
- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear: DateComponents?) -> Bool](uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:).md)
  Notifies the delegate after a person selects a week in the calendar view.
- [func week(ofYearSelection: UICalendarSelectionWeekOfYear, didSelectWeekOfYear: DateComponents?)](uicalendarselectionweekofyeardelegate/week(ofyearselection:didselectweekofyear:).md)
  Determines if a week is available for selection.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UICalendarSelectionWeekOfYearDelegate)?](uicalendarselectionweekofyear/delegate.md)
  A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate)*