# CFCalendarCopyTimeZone(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a time zone object for a specified calendar.

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
func CFCalendarCopyTimeZone(_ calendar: CFCalendar!) -> CFTimeZone!
```

```c
extern CFTimeZoneRefCFCalendarCopyTimeZone(CFCalendarRef calendar);
```

#### Return Value

A copy of the time zone object for the specified calendar. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `calendar`: The calendar to examine.

## See Also

### Getting and Setting the Time Zone
- [func CFCalendarSetTimeZone(CFCalendar!, CFTimeZone!)](./cfcalendarsettimezone%28_,_%29.md)
  Sets the time zone for a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcopytimezone(_:))*