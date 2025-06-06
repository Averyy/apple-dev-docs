# CFCalendarSetFirstWeekday(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the first weekday for a calendar.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFCalendarSetFirstWeekday(_ calendar: CFCalendar!, _ wkdy: CFIndex)
```

## Parameters

- `calendar`: The calendar to modify.
- `wkdy`: The index to set for the first weekday of  .

## See Also

- [func CFCalendarGetFirstWeekday(CFCalendar!) -> CFIndex](cfcalendargetfirstweekday(_:).md)
  Returns the index of first weekday for a specified calendar.
- [func CFCalendarGetMinimumDaysInFirstWeek(CFCalendar!) -> CFIndex](cfcalendargetminimumdaysinfirstweek(_:).md)
  Returns the minimum number of days in the first week of a specified calendar.
- [func CFCalendarSetMinimumDaysInFirstWeek(CFCalendar!, CFIndex)](cfcalendarsetminimumdaysinfirstweek(_:_:).md)
  Sets the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarsetfirstweekday(_:_:))*