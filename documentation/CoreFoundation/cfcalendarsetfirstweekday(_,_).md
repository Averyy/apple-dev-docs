# CFCalendarSetFirstWeekday(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the first weekday for a calendar.

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
func CFCalendarSetFirstWeekday(_ calendar: CFCalendar!, _ wkdy: CFIndex)
```

```c
extern void CFCalendarSetFirstWeekday(CFCalendarRef calendar, CFIndex wkdy);
```

## Parameters

- `calendar`: The calendar to modify.
- `wkdy`: The index to set for the first weekday of `calendar`.

## See Also

### Getting and Setting Day Information
- [func CFCalendarGetFirstWeekday(CFCalendar!) -> CFIndex](./cfcalendargetfirstweekday%28_%29.md)
  Returns the index of first weekday for a specified calendar.
- [func CFCalendarGetMinimumDaysInFirstWeek(CFCalendar!) -> CFIndex](./cfcalendargetminimumdaysinfirstweek%28_%29.md)
  Returns the minimum number of days in the first week of a specified calendar.
- [func CFCalendarSetMinimumDaysInFirstWeek(CFCalendar!, CFIndex)](./cfcalendarsetminimumdaysinfirstweek%28_,_%29.md)
  Sets the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarsetfirstweekday(_:_:))*