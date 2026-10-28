# OSLogEntry.StoreCategory.longTermAuto

**Framework**: OSLog  
**Kind**: case  
**Role**: Case

The entry was tagged with a hint indicating the system should try to preserve it based on the amount of space available.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case longTermAuto
```

```c
OSLogEntryStoreCategoryLongTermAuto
```

## Discussion

Instead of tagging a hint with a number of days that the entry should be preserved, the `longTermAuto` case is preserved based on the amount of space available. Therefore, it will automatically make determinations on how long to preserve the entry. Entries using this case should be persisted in a filesystem-backed data store.

## See Also

### Constants
- [OSLogEntry.StoreCategory.undefined](./undefined.md)
  This entry’s purpose is unknown.
- [OSLogEntry.StoreCategory.metadata](./metadata.md)
  This entry was generated as information about the other entries or about the sequence of entries as a whole.
- [OSLogEntry.StoreCategory.shortTerm](./shortterm.md)
  This entry was not intended to be long-lived, and was captured in the ring buffer.
- [OSLogEntry.StoreCategory.longTerm1](./longterm1.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 1 day.
- [OSLogEntry.StoreCategory.longTerm3](./longterm3.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 3 days.
- [OSLogEntry.StoreCategory.longTerm7](./longterm7.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 7 days.
- [OSLogEntry.StoreCategory.longTerm14](./longterm14.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 14 days.
- [OSLogEntry.StoreCategory.longTerm30](./longterm30.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 30 days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentry/storecategory-swift.enum/longtermauto)*