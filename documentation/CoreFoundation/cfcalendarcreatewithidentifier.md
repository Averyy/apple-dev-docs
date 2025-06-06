# CFCalendarCreateWithIdentifier(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a calendar object for the calendar identified by a calendar identifier.

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
func CFCalendarCreateWithIdentifier(_ allocator: CFAllocator!, _ identifier: CFCalendarIdentifier!) -> CFCalendar!
```

#### Return Value

A calendar object for the calendar identified by `ident`. If the identifier is unknown (if, for example, it is either an unrecognized string, or the calendar is not supported by the current version of the operating system), returns `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `identifier`: A calendar identifier. Calendar identifier constants are given in  .

## See Also

- [func CFCalendarCopyCurrent() -> CFCalendar!](cfcalendarcopycurrent().md)
  Returns a copy of the logical calendar for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcalendarcreatewithidentifier(_:_:))*