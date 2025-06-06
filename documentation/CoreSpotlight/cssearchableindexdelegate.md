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

### Getting item-related details
- [func data(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String) throws -> Data](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md)
- [func fileURL(for: CSSearchableIndex, itemIdentifier: String, typeIdentifier: String, inPlace: Bool) throws -> URL](cssearchableindexdelegate/fileurl(for:itemidentifier:typeidentifier:inplace:).md)
### Updating the index
- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Tells the delegate to reindex all searchable data and clear all local state information.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Tells the delegate to reindex the searchable items associated with the specified identifiers.
### Getting information about indexing
- [func searchableIndexDidThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidthrottle(_:).md)
  Tells the delegate that indexing is being throttled.
- [func searchableIndexDidFinishThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidfinishthrottle(_:).md)
  Tells the delegate that the index throttling has finished.
### Instance Methods
- [func searchableItems(forIdentifiers: [String], searchableItemsHandler: ([CSSearchableItem]) -> Void)](cssearchableindexdelegate/searchableitems(foridentifiers:searchableitemshandler:).md)
- [func searchableItemsDidUpdate([CSSearchableItem])](cssearchableindexdelegate/searchableitemsdidupdate(_:).md)
  Tells the delegate that the framework updated the list of searchable items.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [CSIndexExtensionRequestHandler](csindexextensionrequesthandler.md)

## See Also

- [class CSSearchableIndex](cssearchableindex.md)
  An on-device index for your app’s searchable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate)*