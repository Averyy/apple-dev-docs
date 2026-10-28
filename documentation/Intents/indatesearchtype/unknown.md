# INDateSearchType.unknown

**Framework**: Intents  
**Kind**: case  
**Role**: Case

An unknown search type.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INDateSearchType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case unknown
```

```c
INDateSearchTypeUnknown
```

## Discussion

When specified, don’t consider date values as part of your search criteria.

## See Also

### Constants
- [INDateSearchType.byDueDate](./byduedate.md)
  A search type that requires matching the due date of a reminder to the specified value.
- [INDateSearchType.byModifiedDate](./bymodifieddate.md)
  A search type that requires matching the modification date of a note.
- [INDateSearchType.byCreatedDate](./bycreateddate.md)
  A search type that requires matching the creation date of a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatesearchtype/unknown)*