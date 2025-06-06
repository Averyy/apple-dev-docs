# CFCalendarGetIdentifier(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the given calendar’s identifier.

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
func CFCalendarGetIdentifier(_ calendar: CFCalendar!) -> CFCalendarIdentifier!
```

#### Return Value

A string representation of `calendar`’s identifier. Calendar identifier constants can be found in [`CFLocale`](cflocale.md). Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `calendar`: The calendar to examine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendargetidentifier(_:))*