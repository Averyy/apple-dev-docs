# OSLogEntry.StoreCategory

**Framework**: OSLog  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum OSLogEntryStoreCategory : NSInteger;
```

#### Overview

The unified logging system keeps entries in one of two locations: a ring buffer in memory, or a persisted data store. Entries rotate out to free up resources; they are rotated out in bulk according to heuristics based on space, time, and entry classification.

## Topics

### Constants
- [OSLogEntry.StoreCategory.undefined](./storecategory-swift.enum/undefined.md)
  This entry’s purpose is unknown.
- [OSLogEntry.StoreCategory.metadata](./storecategory-swift.enum/metadata.md)
  This entry was generated as information about the other entries or about the sequence of entries as a whole.
- [OSLogEntry.StoreCategory.shortTerm](./storecategory-swift.enum/shortterm.md)
  This entry was not intended to be long-lived, and was captured in the ring buffer.
- [OSLogEntry.StoreCategory.longTermAuto](./storecategory-swift.enum/longtermauto.md)
  The entry was tagged with a hint indicating the system should try to preserve it based on the amount of space available.
- [OSLogEntry.StoreCategory.longTerm1](./storecategory-swift.enum/longterm1.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 1 day.
- [OSLogEntry.StoreCategory.longTerm3](./storecategory-swift.enum/longterm3.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 3 days.
- [OSLogEntry.StoreCategory.longTerm7](./storecategory-swift.enum/longterm7.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 7 days.
- [OSLogEntry.StoreCategory.longTerm14](./storecategory-swift.enum/longterm14.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 14 days.
- [OSLogEntry.StoreCategory.longTerm30](./storecategory-swift.enum/longterm30.md)
  The entry was tagged with a hint indicating the system should try to preserve it for approximately 30 days.
### Initializers
- [init?(rawValue: Int)](./storecategory-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Store Categories
- [var storeCategory: OSLogEntry.StoreCategory](./storecategory-swift.property.md)
  The current log entry’s storage tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentry/storecategory-swift.enum)*