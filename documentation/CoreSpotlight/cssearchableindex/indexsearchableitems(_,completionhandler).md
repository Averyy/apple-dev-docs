# indexSearchableItems(_:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Adds or updates items in the index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func indexSearchableItems(_ items: [CSSearchableItem], completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func indexSearchableItems(_ items: [CSSearchableItem]) async throws
```

```objc
- (void) indexSearchableItems:(NSArray<CSSearchableItem *> *) items completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func indexSearchableItems(_ items: [CSSearchableItem]) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The [`searchableIndex(_:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:)`](../cssearchableindexdelegate/searchableindex%28_,reindexsearchableitemswithidentifiers,acknowledgementhandler%29.md) protocol method is called in the case that the journaling completed successfully but the data was not able to be indexed for some reason.

## Parameters

- `items`: An array of searchable items to add or update.
- `completionHandler`: The block that’s called when the data has been journaled by the index, which means that the index makes a note that it has to perform this operation. If the completion handler returns an error, it means that the data wasn’t journaled correctly and the client should retry the request.

  The block receives the following parameter:

  - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

### Managing items in an index
- [func deleteAllSearchableItems(completionHandler: (((any Error)?) -> Void)?)](./deleteallsearchableitems%28completionhandler%29.md)
  Deletes all searchable items from the index.
- [func deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](./deletesearchableitems%28withdomainidentifiers,completionhandler%29.md)
  Removes from the index all searchable items associated with the specified domain.
- [func deleteSearchableItems(withIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](./deletesearchableitems%28withidentifiers,completionhandler%29.md)
  Removes from the index all items with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexsearchableitems(_:completionhandler:))*