# searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

Tells the delegate to reindex all searchable data and clear all local state information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func searchableIndex(_ searchableIndex: CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler acknowledgementHandler: @escaping () -> Void)
```

#### Discussion

Typically, the index tells the delegate to reindex its searchable data and clear local state when the index has been lost. An app extension should not use the index passed in `searchableIndex` when a custom data protection class is needed.

## Parameters

- `searchableIndex`: The index in which to reindex the searchable data. The delegate or app extension should pass   to  .
- `acknowledgementHandler`: The delegate or app extension must call the acknowledgement handler after all client state information has been saved, so that the indexer can call this method again in case of a crash.

## See Also

- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Tells the delegate to reindex the searchable items associated with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:))*