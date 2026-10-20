# CFCalendarGetFirstWeekday(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the index of first weekday for a specified calendar.

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
func CFCalendarGetFirstWeekday(_ calendar: CFCalendar!) -> CFIndex
```

#### Return Value

The index of the first weekday of the specified calendar.

## Parameters

- `calendar`: The calendar to examine.

## See Also

- [func CFCalendarSetFirstWeekday(CFCalendar!, CFIndex)](cfcalendarsetfirstweekday(_:_:).md)
  Sets the first weekday for a calendar.
- [func CFCalendarGetMinimumDaysInFirstWeek(CFCalendar!) -> CFIndex](cfcalendargetminimumdaysinfirstweek(_:).md)
  Returns the minimum number of days in the first week of a specified calendar.
- [func CFCalendarSetMinimumDaysInFirstWeek(CFCalendar!, CFIndex)](cfcalendarsetminimumdaysinfirstweek(_:_:).md)
  Sets the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetfirstweekday(_:))*