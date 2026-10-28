# OSLogEntry.StoreCategory.longTerm14

**Framework**: OSLog  
**Kind**: case  
**Role**: Case

The entry was tagged with a hint indicating the system should try to preserve it for approximately 14 days.

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
case longTerm14
```

```c
OSLogEntryStoreCategoryLongTerm14
```

## Discussion

It was persisted in the filesystem-backed date store, and rotation of these entries was based on both time and space considerations.

## See Also

### Constants
- [OSLogEntry.StoreCategory.undefined](./undefined.md)
  This entry’s purpose is unknown.
- [OSLogEntry.StoreCategory.metadata](./metadata.md)
  This entry was generated as information about the other entries or about the sequence of entries as a whole.
- [OSLogEntry.StoreCategory.shortTerm](./shortterm.md)
  This entry was not intended to be long-lived, and was captured in the ring buffer.
- [OSLogEntry.StoreCategory.longTermAuto](./longtermauto.md)
  The entry was tagged with a hint indicating the system should try to preserve it based on the amount of space available.
- [OSLogEntry.StoreCategory.longTerm1](./longterm1.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 1 day.
- [OSLogEntry.StoreCategory.longTerm3](./longterm3.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 3 days.
- [OSLogEntry.StoreCategory.longTerm7](./longterm7.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 7 days.
- [OSLogEntry.StoreCategory.longTerm30](./longterm30.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 30 days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentry/storecategory-swift.enum/longterm14)*