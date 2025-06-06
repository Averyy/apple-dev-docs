# UICalendarSelectionSingleDateDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICalendarSelectionSingleDateDelegate : NSObjectProtocol
```

## Topics

### Getting selectable dates
- [func dateSelection(UICalendarSelectionSingleDate, canSelectDate: DateComponents?) -> Bool](uicalendarselectionsingledatedelegate/dateselection(_:canselectdate:).md)
  Returns whether a user can select a date represented by date components in the calendar view.
### Changing the selected date
- [func dateSelection(UICalendarSelectionSingleDate, didSelectDate: DateComponents?)](uicalendarselectionsingledatedelegate/dateselection(_:didselectdate:).md)
  Informs the delegate that a user selected a date represented by date components.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UICalendarSelectionSingleDateDelegate)?](uicalendarselectionsingledate/delegate.md)
  A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate)*