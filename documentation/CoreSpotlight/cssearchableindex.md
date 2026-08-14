# CSSearchableIndex

**Framework**: Core Spotlight  
**Kind**: class

An on-device index for your app’s searchable content.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSSearchableIndex
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)
- [Generating summary and priority data for indexed items](generating-summary-and-priority-data-for-indexed-items.md)

#### Overview

A `CSSearchableIndex` object manages an on-device index for your app’s searchable content. To make your app’s content searchable, create one or more [`CSSearchableItem`](cssearchableitem.md) objects for your content and add those items to the index. If your app defines [`AppEntity`](https://developer.apple.com/documentation/appintents/appentity) types, you can also index those types directly or associate them with your [`CSSearchableItem`](cssearchableitem.md) objects. When you execute a query, Core Spotlight searches your indexes for the requested information and returns the results to your code.

Create custom `CSSearchableIndex` objects in your production code to store your app’s content, instead of using the default index. Custom indexes support data protection, which allows you to encrypt your data and protect it from unauthorized access. Custom indexes also support batch operations, which allow you to index large amounts of data more efficiently and with less risk. For example, you can add custom state information to each batch operation to make it easier to restart the indexing process if your app or app extension crashes. Use the default index only during testing or prototyping of your features.

Modify a `CSSearchableIndex` object from only one thread or task at a time, and modify it only from your signed app or app extension. It’s a programming error to access a custom index from multiple threads simultaneously or from an unsigned bundle. When performing batch updates on an index, start each new batch operation only after calling the [`endBatch(withClientState:completionHandler:)`](cssearchableindex/endbatch(withclientstate:completionhandler:).md) or [`endIndexBatch(expectedClientState:newClientState:completionHandler:)`](cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:).md) method of the previous batch operation.

> **Note**: If your app creates [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) objects, set the [`isEligibleForSearch`](https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforsearch) property of those objects to `true` if you want them to appear in search results.

## Topics

### Creating an index
- [class func `default`() -> Self](cssearchableindex/default.md)
  Returns the default on-device index.
- [init(name: String)](cssearchableindex/init(name:).md)
  Returns an on-device index with the specified name.
- [init(name: String, protectionClass: FileProtectionType?)](cssearchableindex/init(name:protectionclass:).md)
  Returns an on-device index with the specified name and data protection class.
### Determining if indexing is available
- [class func isIndexingAvailable() -> Bool](cssearchableindex/isindexingavailable.md)
  Returns a Boolean value that indicates whether indexing is available on the current device.
### Responding to index-related changes
- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.
- [var indexDelegate: (any CSSearchableIndexDelegate)?](cssearchableindex/indexdelegate.md)
  The delegate object that can handle index-management tasks.
### Managing items in an index
- [func indexSearchableItems([CSSearchableItem], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/indexsearchableitems(_:completionhandler:).md)
  Adds or updates items in the index.
- [func deleteAllSearchableItems(completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deleteallsearchableitems(completionhandler:).md)
  Deletes all searchable items from the index.
- [func deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:).md)
  Removes from the index all searchable items associated with the specified domain.
- [func deleteSearchableItems(withIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withidentifiers:completionhandler:).md)
  Removes from the index all items with the specified identifiers.
### Indexing app entities
- [func indexAppEntities([some IndexedEntity], priority: Int) async throws](cssearchableindex/indexappentities(_:priority:).md)
  Indexes one or more app entities and assigns an optional priority to them.
- [func deleteAppEntities<Entity>(ofType: Entity.Type) async throws](cssearchableindex/deleteappentities(oftype:).md)
  Deletes all app entities of the specified type from the current index.
- [func deleteAppEntities<Entity>(identifiedBy: [Entity.ID], ofType: Entity.Type) async throws](cssearchableindex/deleteappentities(identifiedby:oftype:).md)
  Deletes entities with the specified identifiers and type from the current index.
### Batching index updates
- [func beginBatch()](cssearchableindex/beginbatch.md)
  Begins a batch of updates to an index.
- [func endBatch(withClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endbatch(withclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func endIndexBatch(expectedClientState: Data?, newClientState: Data, completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/endindexbatch(expectedclientstate:newclientstate:completionhandler:).md)
  Ends a batch of index updates and stores the specified state information.
- [func fetchLastClientState(completionHandler: (Data?, (any Error)?) -> Void)](cssearchableindex/fetchlastclientstate(completionhandler:).md)
  Fetches the app’s most recent client state information asynchronously.
### Handling drag and drop content
- [func fetchData(forBundleIdentifier: String, itemIdentifier: String, contentType: UTType, completionHandler: (Data?, (any Error)?) -> Void)](cssearchableindex/fetchdata(forbundleidentifier:itemidentifier:contenttype:completionhandler:).md)
  Fetches data from an external provider.
### Getting the protection class
- [var protectionClass: FileProtectionType](cssearchableindex/protectionclass.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Generating summary and priority data for indexed items](generating-summary-and-priority-data-for-indexed-items.md)
  Summarize mail, message, and audio transcripts or assess the priority of mail and messages using Spotlight and Apple Intelligence.
- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.
- [class CSSearchableIndexDescription](cssearchableindexdescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex)*