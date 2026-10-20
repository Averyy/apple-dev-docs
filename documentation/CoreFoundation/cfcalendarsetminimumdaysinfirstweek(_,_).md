# CFCalendarSetMinimumDaysInFirstWeek(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the minimum number of days in the first week of a specified calendar.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFCalendarSetMinimumDaysInFirstWeek(_ calendar: CFCalendar!, _ mwd: CFIndex)
```

```c
extern void CFCalendarSetMinimumDaysInFirstWeek(CFCalendarRef calendar, CFIndex mwd);
```

## Parameters

- `calendar`: The calendar to modify.
- `mwd`: The number to set as the minimum number of days in the first week of `calendar`.

## See Also

### Getting and Setting Day Information
- [func CFCalendarGetFirstWeekday(CFCalendar!) -> CFIndex](./cfcalendargetfirstweekday%28_%29.md)
  Returns the index of first weekday for a specified calendar.
- [func CFCalendarSetFirstWeekday(CFCalendar!, CFIndex)](./cfcalendarsetfirstweekday%28_,_%29.md)
  Sets the first weekday for a calendar.
- [func CFCalendarGetMinimumDaysInFirstWeek(CFCalendar!) -> CFIndex](./cfcalendargetminimumdaysinfirstweek%28_%29.md)
  Returns the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarsetminimumdaysinfirstweek(_:_:))*