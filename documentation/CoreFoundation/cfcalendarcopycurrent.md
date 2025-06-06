# CFCalendarCopyCurrent()

**Framework**: Core Foundation  
**Kind**: func

Returns a copy of the logical calendar for the current user.

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
func CFCalendarCopyCurrent() -> CFCalendar!
```

#### Return Value

The logical calendar for the current user that is formed from the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences. This function may return a retained cached object, not a new object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Settings you get from this calendar do not change if user defaults change so that your operations are consistent.

Typically you perform some operations on the returned object and then release it. The returned object may be cached, so you do not need to hold on to it indefinitely.

## See Also

- [func CFCalendarCreateWithIdentifier(CFAllocator!, CFCalendarIdentifier!) -> CFCalendar!](cfcalendarcreatewithidentifier(_:_:).md)
  Returns a calendar object for the calendar identified by a calendar identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcopycurrent())*