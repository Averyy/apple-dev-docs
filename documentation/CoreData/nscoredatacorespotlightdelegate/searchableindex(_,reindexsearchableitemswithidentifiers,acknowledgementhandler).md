# searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Reindexes the searchable items for the specified identifiers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler: @escaping () -> Void)
```

```objc
- (void) searchableIndex:(CSSearchableIndex *) searchableIndex reindexSearchableItemsWithIdentifiers:(NSArray<NSString *> *) identifiers acknowledgementHandler:(void (^)()) acknowledgementHandler;
```

#### Discussion

For more information, see [`searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)`](./searchableindex%28_,reindexsearchableitemswithidentifiers,acknowledgementhandler%29.md).

## Parameters

- `searchableIndex`: The index that contains the items that require reindexing.
- `identifiers`: An array of strings that identify the searchable items.
- `acknowledgementHandler`: The handler to call when you finish saving client state information.

## See Also

### Updating the Index
- [static let indexDidUpdateNotification: Notification.Name](./indexdidupdatenotification.md)
  The notification the delegate posts after Spotlight updates the index.
- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](./searchableindex%28_,reindexallsearchableitemswithacknowledgementhandler%29.md)
  Reindexes all searchable items and clears any local state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:))*