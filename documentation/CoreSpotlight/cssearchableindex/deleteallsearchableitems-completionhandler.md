# deleteAllSearchableItems(completionHandler:)

**Framework**: Core Spotlight  
**Kind**: method

Deletes all searchable items from the index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func deleteAllSearchableItems() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func deleteAllSearchableItems() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The block that’s called when the request has been journaled by the index (“journaled” means that the index makes a note that it has to perform this operation). Note that the request may not have completed. The block receives the following parameter: - **error**: If an error occurred, this parameter holds an error object that explains the error. Otherwise, the value of this parameter is `nil`.

## See Also

- [func indexSearchableItems([CSSearchableItem], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/indexsearchableitems(_:completionhandler:).md)
  Adds or updates items in the index.
- [func deleteSearchableItems(withDomainIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:).md)
  Removes from the index all searchable items associated with the specified domain.
- [func deleteSearchableItems(withIdentifiers: [String], completionHandler: (((any Error)?) -> Void)?)](cssearchableindex/deletesearchableitems(withidentifiers:completionhandler:).md)
  Removes from the index all items with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deleteallsearchableitems(completionhandler:))*