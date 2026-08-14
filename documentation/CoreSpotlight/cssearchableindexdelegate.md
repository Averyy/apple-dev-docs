# CSSearchableIndexDelegate

**Framework**: Core Spotlight  
**Kind**: protocol

A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
protocol CSSearchableIndexDelegate : NSObjectProtocol
```

## Mentions

- [Regenerating your app’s indexes on demand](regenerating-your-app-s-indexes-on-demand.md)

#### Overview

The `CSSearchableIndexDelegate` protocol defines methods that a delegate object or an app extension can use to handle communication from the on-device index. Apps that are long-running or that perform batch updates to the index should implement the required methods of this protocol in either a delegate object or an app extension.

The index delegate methods are called when there is an issue with the index and more information is needed from an app. For example, the methods can be called when the entire index is lost or there was a failure to process data for some identifiers.

## Topics

### Updating the index
- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Tells the delegate to reindex all searchable data and clear all local state information.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Tells the delegate to reindex the searchable items associated with the specified identifiers.
- [func searchableItemsDidUpdate([CSSearchableItem])](cssearchableindexdelegate/searchableitemsdidupdate(_:).md)
  Tells the delegate that the framework updated the specified items.
### Providing data for an item
- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:).md)
  Requests that the delegate provide searchable items for the provided identifiers.
- [func searchableItems(forIdentifiers: [String], protectionClass: FileProtectionType, searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:protectionclass:searchableitemshandler:).md)
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md)
  Returns the data for the requested item during a drag-and-drop operation.
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:).md)
  Returns a file URL for the requested item during a drag-and-drop operation.
### Monitoring Spotlight status
- [func searchableIndexDidThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidthrottle(_:).md)
  Tells the delegate that indexing is being throttled.
- [func searchableIndexDidFinishThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidfinishthrottle(_:).md)
  Tells the delegate that the index throttling has finished.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [CSIndexExtensionRequestHandler](csindexextensionrequesthandler.md)

## See Also

- [Generating summary and priority data for indexed items](generating-summary-and-priority-data-for-indexed-items.md)
  Summarize mail, message, and audio transcripts or assess the priority of mail and messages using Spotlight and Apple Intelligence.
- [class CSSearchableIndex](cssearchableindex.md)
  An on-device index for your app’s searchable content.
- [class CSSearchableIndexDescription](cssearchableindexdescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate)*