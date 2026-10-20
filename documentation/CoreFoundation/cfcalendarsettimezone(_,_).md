# CFCalendarSetTimeZone(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the time zone for a calendar.

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
func CFCalendarSetTimeZone(_ calendar: CFCalendar!, _ tz: CFTimeZone!)
```

```c
extern void CFCalendarSetTimeZone(CFCalendarRef calendar, CFTimeZoneRef tz);
```

## Parameters

- `calendar`: The calendar to modify.
- `tz`: The time zone to set for `calendar`.

## See Also

### Getting and Setting the Time Zone
- [func CFCalendarCopyTimeZone(CFCalendar!) -> CFTimeZone!](./cfcalendarcopytimezone%28_%29.md)
  Returns a time zone object for a specified calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarsettimezone(_:_:))*