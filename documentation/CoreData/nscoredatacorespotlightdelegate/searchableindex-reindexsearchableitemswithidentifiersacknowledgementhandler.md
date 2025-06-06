# searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)

**Framework**: Core Data  
**Kind**: method

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

#### Discussion

For more information, see [`searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)`](nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md).

## Parameters

- `searchableIndex`: The index that contains the items that require reindexing.
- `identifiers`: An array of strings that identify the searchable items.
- `acknowledgementHandler`: The handler to call when you finish saving client state information.

## See Also

- [static let indexDidUpdateNotification: Notification.Name](nscoredatacorespotlightdelegate/indexdidupdatenotification.md)
  The notification the delegate posts after Spotlight updates the index.
- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Reindexes all searchable items and clears any local state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:))*