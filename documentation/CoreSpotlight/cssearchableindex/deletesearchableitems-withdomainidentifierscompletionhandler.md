# deleteSearchableItems(withDomainIdentifiers:completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Removes from the index all searchable items associated with the specified domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String]) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func deleteSearchableItems(withDomainIdentifiers domainIdentifiers: [String]) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to delete groups of items. Note that the delete operation is recursive. For example, if domain identifiers are of the form `<account-id>.<mailbox-id>`, calling this method and specifying `<account-id>` deletes items with the specified account and any mailbox.

## Parameters

- `domainIdentifiers`: The domain identifier that describes the group of items to delete. To learn more about domain identifiers, see  .
- `completionHandler`: The block receives the following parameter:

## See Also

- [func indexSearchableItems([CSSearchableItem], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/indexsearchableitems(_:completionhandler:).md)
  Adds or updates items in the index.
- [func deleteAllSearchableItems(completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deleteallsearchableitems(completionhandler:).md)
  Deletes all searchable items from the index.
- [func deleteSearchableItems(withIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withidentifiers:completionhandler:).md)
  Removes from the index all items with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:))*