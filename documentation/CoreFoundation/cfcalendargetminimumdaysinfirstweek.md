# CFCalendarGetMinimumDaysInFirstWeek(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the minimum number of days in the first week of a specified calendar.

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
func CFCalendarGetMinimumDaysInFirstWeek(_ calendar: CFCalendar!) -> CFIndex
```

#### Return Value

The minimum number of days in the first week of `calendar`.

## Parameters

- `calendar`: The calendar to examine.

## See Also

- [func CFCalendarGetFirstWeekday(CFCalendar!) -> CFIndex](cfcalendargetfirstweekday(_:).md)
  Returns the index of first weekday for a specified calendar.
- [func CFCalendarSetFirstWeekday(CFCalendar!, CFIndex)](cfcalendarsetfirstweekday(_:_:).md)
  Sets the first weekday for a calendar.
- [func CFCalendarSetMinimumDaysInFirstWeek(CFCalendar!, CFIndex)](cfcalendarsetminimumdaysinfirstweek(_:_:).md)
  Sets the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetminimumdaysinfirstweek(_:))*