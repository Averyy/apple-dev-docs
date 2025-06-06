# OSLogEntry.StoreCategory

**Framework**: OSLog  
**Kind**: enum

A classification of how the entry was to be stored and rotated at the point when it was created.

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
enum StoreCategory
```

#### Overview

The unified logging system keeps entries in one of two locations: a ring buffer in memory, or a persisted data store. Entries rotate out to free up resources; they are rotated out in bulk according to heuristics based on space, time, and entry classification.

## Topics

### Constants
- [OSLogEntry.StoreCategory.undefined](oslogentry/storecategory-swift.enum/undefined.md)
  This entry’s purpose is unknown.
- [OSLogEntry.StoreCategory.metadata](oslogentry/storecategory-swift.enum/metadata.md)
  This entry was generated as information about the other entries or about the sequence of entries as a whole.
- [OSLogEntry.StoreCategory.shortTerm](oslogentry/storecategory-swift.enum/shortterm.md)
  This entry was not intended to be long-lived, and was captured in the ring buffer.
- [OSLogEntry.StoreCategory.longTermAuto](oslogentry/storecategory-swift.enum/longtermauto.md)
  The entry was tagged with a hint indicating the system should try to preserve it based on the amount of space available.
- [OSLogEntry.StoreCategory.longTerm1](oslogentry/storecategory-swift.enum/longterm1.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 1 day.
- [OSLogEntry.StoreCategory.longTerm3](oslogentry/storecategory-swift.enum/longterm3.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 3 days.
- [OSLogEntry.StoreCategory.longTerm7](oslogentry/storecategory-swift.enum/longterm7.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 7 days.
- [OSLogEntry.StoreCategory.longTerm14](oslogentry/storecategory-swift.enum/longterm14.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 14 days.
- [OSLogEntry.StoreCategory.longTerm30](oslogentry/storecategory-swift.enum/longterm30.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 30 days.
### Initializers
- [init?(rawValue: Int)](oslogentry/storecategory-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var storeCategory: OSLogEntry.StoreCategory](oslogentry/storecategory-swift.property.md)
  The current log entry’s storage tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentry/storecategory-swift.enum)*