# UICalendarSelection

**Framework**: UIKit  
**Kind**: class

A base object that tracks one or more dates a user selects from a calendar view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICalendarSelection
```

#### Overview

Don’t use this object directly in your calendar view to track date selection. Use the subclass [`UICalendarSelectionSingleDate`](uicalendarselectionsingledate.md) to track a single date selection, or [`UICalendarSelectionMultiDate`](uicalendarselectionmultidate.md) to track multiple date selections.

## Topics

### Updating selectable dates
- [func updateSelectableDates()](uicalendarselection/updateselectabledates.md)
  Informs the calendar view to update the view for selectable dates.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md)
- [UICalendarSelectionSingleDate](uicalendarselectionsingledate.md)
- [UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [var selectionBehavior: UICalendarSelection?](uicalendarview/selectionbehavior.md)
  The current date selection method of the calendar view.
- [class UICalendarSelectionSingleDate](uicalendarselectionsingledate.md)
  An object that tracks a date the user selects from a calendar view.
- [class UICalendarSelectionMultiDate](uicalendarselectionmultidate.md)
  An object that tracks multiple dates the user selects from a calendar view.
- [class UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md)
  An object that tracks a specific week a person selects from a calendar view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicalendarselection)*