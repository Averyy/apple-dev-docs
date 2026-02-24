# searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

Tells the delegate to reindex the searchable items associated with the specified identifiers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexSearchableItemsWithIdentifiers identifiers: [String], acknowledgementHandler: @escaping () -> Void)
```

#### Discussion

An app extension should not use the index passed in `searchableIndex` when a custom data protection class is needed.

## Parameters

- `searchableIndex`: The index in which to reindex the specified searchable data. To update the state of the items, the delegate or app extension should call [`indexSearchableItems(_:completionHandler:)`](cssearchableindex/indexsearchableitems(_:completionhandler:).md) passing in `searchableIndex`.
- `identifiers`: An array of identifiers that specify searchable items.
- `acknowledgementHandler`: The handler to call after all client state has been saved. Note that if the app passes client state information in a batch (for example, by calling [`endBatch(withClientState:completionHandler:)`](cssearchableindex/endbatch(withclientstate:completionhandler:).md)), the acknowledgement handler can be called immediately. The delegate or app extension must call the acknowledgement handler after all client state information has been saved, so that the indexer can call this method again in case of a crash.

## See Also

- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Tells the delegate to reindex all searchable data and clear all local state information.
- [func searchableItemsDidUpdate([CSSearchableItem])](cssearchableindexdelegate/searchableitemsdidupdate(_:).md)
  Tells the delegate that the framework updated the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:))*