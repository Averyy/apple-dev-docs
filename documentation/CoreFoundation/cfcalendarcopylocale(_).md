# CFCalendarCopyLocale(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a locale object for a specified calendar.

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
func CFCalendarCopyLocale(_ calendar: CFCalendar!) -> CFLocale!
```

```c
extern CFLocaleRefCFCalendarCopyLocale(CFCalendarRef calendar);
```

## Return Value

A copy of the locale object for the specified calendar. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `calendar`: The calendar to examine.

## See Also

### Getting and Setting the Locale
- [func CFCalendarSetLocale(CFCalendar!, CFLocale!)](./cfcalendarsetlocale%28_,_%29.md)
  Sets the locale for a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcopylocale(_:))*