# CFCalendarGetMinimumDaysInFirstWeek(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the minimum number of days in the first week of a specified calendar.

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
func CFCalendarGetMinimumDaysInFirstWeek(_ calendar: CFCalendar!) -> CFIndex
```

```c
extern CFIndex CFCalendarGetMinimumDaysInFirstWeek(CFCalendarRef calendar);
```

#### Return Value

The minimum number of days in the first week of `calendar`.

## Parameters

- `calendar`: The calendar to examine.

## See Also

### Getting and Setting Day Information
- [func CFCalendarGetFirstWeekday(CFCalendar!) -> CFIndex](./cfcalendargetfirstweekday%28_%29.md)
  Returns the index of first weekday for a specified calendar.
- [func CFCalendarSetFirstWeekday(CFCalendar!, CFIndex)](./cfcalendarsetfirstweekday%28_,_%29.md)
  Sets the first weekday for a calendar.
- [func CFCalendarSetMinimumDaysInFirstWeek(CFCalendar!, CFIndex)](./cfcalendarsetminimumdaysinfirstweek%28_,_%29.md)
  Sets the minimum number of days in the first week of a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetminimumdaysinfirstweek(_:))*