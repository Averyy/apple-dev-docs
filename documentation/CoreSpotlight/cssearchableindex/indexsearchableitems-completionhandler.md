# indexSearchableItems(_:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Adds or updates items in the index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func indexSearchableItems(_ items: [CSSearchableItem]) async throws
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func indexSearchableItems(_ items: [CSSearchableItem]) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The [`searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)`](cssearchableindexdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md) protocol method is called in the case that the journaling completed successfully but the data was not able to be indexed for some reason.

## Parameters

- `items`: An array of searchable items to add or update.
- `completionHandler`: The block receives the following parameter:

## See Also

- [func deleteAllSearchableItems(completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deleteallsearchableitems(completionhandler:).md)
  Deletes all searchable items from the index.
- [func deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:).md)
  Removes from the index all searchable items associated with the specified domain.
- [func deleteSearchableItems(withIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withidentifiers:completionhandler:).md)
  Removes from the index all items with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexsearchableitems(_:completionhandler:))*