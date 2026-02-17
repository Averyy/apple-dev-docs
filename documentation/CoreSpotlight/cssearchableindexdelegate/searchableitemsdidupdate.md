# searchableItemsDidUpdate(_:)

**Framework**: Core Spotlight  
**Kind**: method

Tells the delegate that the framework updated the specified items.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func searchableItemsDidUpdate(_ items: [CSSearchableItem])
```

## Mentions

- [Generating summary and priority data for indexed items](generating-summary-and-priority-data-for-indexed-items.md)

#### Discussion

When the system updates properties of your searchable item’s [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md), it calls this method to notify you that the attributes changed. For example, it calls this method when summary or priority information from Apple Intelligence becomes available. For more information, see [`Generating summary and priority data for indexed items`](generating-summary-and-priority-data-for-indexed-items.md).

## Parameters

- `items`: The updated items.

## See Also

- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Tells the delegate to reindex all searchable data and clear all local state information.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Tells the delegate to reindex the searchable items associated with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitemsdidupdate(_:))*