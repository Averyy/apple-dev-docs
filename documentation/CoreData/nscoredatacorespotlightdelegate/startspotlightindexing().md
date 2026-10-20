# startSpotlightIndexing()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startSpotlightIndexing;
```

#### Discussion

After you call this method, the delegate posts a notification whenever the index changes. The type of notification is [`indexDidUpdateNotification`](./indexdidupdatenotification.md), and its `userInfo` dictionary contains the keys [`NSStoreUUIDKey`](../nsstoreuuidkey.md) and [`NSPersistentHistoryTokenKey`](../nspersistenthistorytokenkey.md).

## See Also

### Managing the Index
- [func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?](./attributeset%28for%29.md)
  Returns the searchable attributes for the specified managed object.
- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](./deletespotlightindex%28completionhandler%29.md)
  Deletes all searchable items from the configured index.
- [func stopSpotlightIndexing()](./stopspotlightindexing%28%29.md)
  Stops the indexing of the store’s entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/startspotlightindexing())*