# CFCalendarCopyLocale(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a locale object for a specified calendar.

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
func CFCalendarCopyLocale(_ calendar: CFCalendar!) -> CFLocale!
```

#### Return Value

A copy of the locale object for the specified calendar. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `calendar`: The calendar to examine.

## See Also

- [func CFCalendarSetLocale(CFCalendar!, CFLocale!)](cfcalendarsetlocale(_:_:).md)
  Sets the locale for a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcopylocale(_:))*