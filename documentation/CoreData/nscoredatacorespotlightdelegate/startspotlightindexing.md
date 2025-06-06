# startSpotlightIndexing()

**Framework**: Core Data  
**Kind**: method

Starts the indexing of the store’s entities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func startSpotlightIndexing()
```

#### Discussion

After you call this method, the delegate posts a notification whenever the index changes. The type of notification is [`indexDidUpdateNotification`](nscoredatacorespotlightdelegate/indexdidupdatenotification.md), and its `userInfo` dictionary contains the keys [`NSStoreUUIDKey`](nsstoreuuidkey.md) and [`NSPersistentHistoryTokenKey`](nspersistenthistorytokenkey.md).

## See Also

- [func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?](nscoredatacorespotlightdelegate/attributeset(for:).md)
  Returns the searchable attributes for the specified managed object.
- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:).md)
  Deletes all searchable items from the configured index.
- [func stopSpotlightIndexing()](nscoredatacorespotlightdelegate/stopspotlightindexing.md)
  Stops the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/startspotlightindexing())*