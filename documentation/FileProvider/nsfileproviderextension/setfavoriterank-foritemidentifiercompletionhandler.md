# setFavoriteRank(_:forItemIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Marks a directory as a favorite and sets its relative order in the Favorites list.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setFavoriteRank(_ favoriteRank: NSNumber?, forItemIdentifier itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setFavoriteRank(_ favoriteRank: NSNumber?, forItemIdentifier itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method is called when the user marks a directory as a favorite. Override this method to make any necessary local changes. Your implementation should return immediately. Call the completion handler before performing any network activity or other long-running tasks. Defer these tasks to the background.

The `favoriteItem` instance that you pass to the completion handler should match the item’s old file provider item, with only one change: set the [`favoriteRank`](nsfileprovideritemprotocol/favoriterank.md) property with the value of the `favoriteRank` parameter.

Always include items with a non-`nil` [`favoriteRank`](nsfileprovideritemprotocol/favoriterank.md) property in your File Provider extension’s working set; however, you don’t need to include the directory’s content. You also don’t need to make the directory’s content available offline.

## Parameters

- `favoriteRank`: A value used to determine the relative order of directories in the Favorites list.
- `itemIdentifier`: The item’s persistent identifier.
- `completionHandler`: A block that takes the following parameters:

## See Also

- [Providing support for user-driven actions](providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
- [func createDirectory(withName: String, inParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/createdirectory(withname:inparentitemidentifier:completionhandler:).md)
  Creates a directory with the given name inside the given parent directory.
- [func deleteItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/deleteitem(withidentifier:completionhandler:).md)
  Permanently deletes an item from the trash.
- [func importDocument(at: URL, toParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/importdocument(at:toparentitemidentifier:completionhandler:).md)
  Imports a file or package into the given parent directory.
- [func renameItem(withIdentifier: NSFileProviderItemIdentifier, toName: String, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/renameitem(withidentifier:toname:completionhandler:).md)
  Renames a document or directory.
- [func reparentItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemWithIdentifier: NSFileProviderItemIdentifier, newName: String?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/reparentitem(withidentifier:toparentitemwithidentifier:newname:completionhandler:).md)
  Moves the specified item into the given parent directory.
- [func setLastUsedDate(Date?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/setlastuseddate(_:foritemidentifier:completionhandler:).md)
  Marks an item as recently used and sets its relative order in the Recents list.
- [func setTagData(Data?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/settagdata(_:foritemidentifier:completionhandler:).md)
  Tags an item.
- [func trashItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/trashitem(withidentifier:completionhandler:).md)
  Moves an item into the trash.
- [func untrashItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemIdentifier: NSFileProviderItemIdentifier?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/untrashitem(withidentifier:toparentitemidentifier:completionhandler:).md)
  Moves an item out of the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/setfavoriterank(_:foritemidentifier:completionhandler:))*