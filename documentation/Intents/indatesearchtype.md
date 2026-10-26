# INDateSearchType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of date-based search to perform.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INDateSearchType is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INDateSearchType
```

```c
enum INDateSearchType : NSInteger;
```

## Topics

### Constants
- [INDateSearchType.unknown](./indatesearchtype/unknown.md)
  An unknown search type.
- [INDateSearchType.byDueDate](./indatesearchtype/byduedate.md)
  A search type that requires matching the due date of a reminder to the specified value.
- [INDateSearchType.byModifiedDate](./indatesearchtype/bymodifieddate.md)
  A search type that requires matching the modification date of a note.
- [INDateSearchType.byCreatedDate](./indatesearchtype/bycreateddate.md)
  A search type that requires matching the creation date of a note.
### Initializers
- [init?(rawValue: Int)](./indatesearchtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching by Date
- [var dateTime: INDateComponentsRange?](./insearchfornotebookitemsintent/datetime.md)
  The value to use when performing date-based searches.
- [var dateSearchType: INDateSearchType](./insearchfornotebookitemsintent/datesearchtype.md)
  An indicator of how to apply date values to your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatesearchtype)*