# OSLogEntry.StoreCategory.longTermAuto

**Framework**: OSLog  
**Kind**: case

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

#### Discussion

Instead of tagging a hint with a number of days that the entry should be preserved, the `longTermAuto` case is preserved based on the amount of space available. Therefore, it will automatically make determinations on how long to preserve the entry. Entries using this case should be persisted in a filesystem-backed data store.

## See Also

- [OSLogEntry.StoreCategory.undefined](oslogentry/storecategory-swift.enum/undefined.md)
  This entry’s purpose is unknown.
- [OSLogEntry.StoreCategory.metadata](oslogentry/storecategory-swift.enum/metadata.md)
  This entry was generated as information about the other entries or about the sequence of entries as a whole.
- [OSLogEntry.StoreCategory.shortTerm](oslogentry/storecategory-swift.enum/shortterm.md)
  This entry was not intended to be long-lived, and was captured in the ring buffer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentry/storecategory-swift.enum/longtermauto)*