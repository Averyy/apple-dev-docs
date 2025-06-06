# UICalendarSelectionMultiDateDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICalendarSelectionMultiDateDelegate : NSObjectProtocol
```

## Topics

### Getting selectable dates
- [func multiDateSelection(UICalendarSelectionMultiDate, canSelectDate: DateComponents) -> Bool](uicalendarselectionmultidatedelegate/multidateselection(_:canselectdate:).md)
  Returns whether a user can select a date represented by date components in the calendar view.
- [func multiDateSelection(UICalendarSelectionMultiDate, canDeselectDate: DateComponents) -> Bool](uicalendarselectionmultidatedelegate/multidateselection(_:candeselectdate:).md)
  Returns whether a user can deselect a date represented by date components in the calendar view.
### Changing selected dates
- [func multiDateSelection(UICalendarSelectionMultiDate, didSelectDate: DateComponents)](uicalendarselectionmultidatedelegate/multidateselection(_:didselectdate:).md)
  Informs the delegate that a user selected a date represented by date components.
- [func multiDateSelection(UICalendarSelectionMultiDate, didDeselectDate: DateComponents)](uicalendarselectionmultidatedelegate/multidateselection(_:diddeselectdate:).md)
  Informs the delegate that a user deselected a date represented by date components.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UICalendarSelectionMultiDateDelegate)?](uicalendarselectionmultidate/delegate.md)
  A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate)*