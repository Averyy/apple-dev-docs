# searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Reindexes all searchable items and clears any local state.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Void)
```

```objc
- (void) searchableIndex:(CSSearchableIndex *) searchableIndex reindexAllSearchableItemsWithAcknowledgementHandler:(void (^)()) acknowledgementHandler;
```

#### Discussion

For more information, see [`searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)`](../../CoreSpotlight/cssearchableindexdelegate/searchableindex%28_,reindexallsearchableitemswithacknowledgementhandler%29.md).

## Parameters

- `searchableIndex`: The index that requires reindexing.
- `acknowledgementHandler`: The handler to call when you finish saving client state information.

## See Also

### Updating the Index
- [static let indexDidUpdateNotification: Notification.Name](./indexdidupdatenotification.md)
  The notification the delegate posts after Spotlight updates the index.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](./searchableindex%28_,reindexsearchableitemswithidentifiers,acknowledgementhandler%29.md)
  Reindexes the searchable items for the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:))*