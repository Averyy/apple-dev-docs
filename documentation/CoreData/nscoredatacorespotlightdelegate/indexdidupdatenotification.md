# indexDidUpdateNotification

**Framework**: Core Data  
**Kind**: property

The notification the delegate posts after Spotlight updates the index.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
static let indexDidUpdateNotification: Notification.Name
```

#### Discussion

The notification’s `userInfo` dictionary contains the keys [`NSStoreUUIDKey`](nsstoreuuidkey.md) and [`NSPersistentHistoryTokenKey`](nspersistenthistorytokenkey.md).

## See Also

- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Reindexes all searchable items and clears any local state.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Reindexes the searchable items for the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatenotification)*