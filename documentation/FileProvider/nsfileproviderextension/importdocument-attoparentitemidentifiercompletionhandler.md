# importDocument(at:toParentItemIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Imports a file or package into the given parent directory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func importDocument(at fileURL: URL, toParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func importDocument(at fileURL: URL, toParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method is called when the user imports a document or directory. Override this method to move the file at the provided security-scoped URL to the file provider’s storage. Your implementation should return immediately. Call the completion handler before performing any network activity or other long-running tasks. Defer these tasks to the background.

The `importedDocumentItem` instance that you pass to the completion handler must define the following properties:

The user’s ability to import an item into a directory is controlled by the parent directory’s [`allowsAddingSubItems`](nsfileprovideritemcapabilities/allowsaddingsubitems.md) capability.

## Parameters

- `fileURL`: A security-scoped URL for the file to import. Call   on the URL before accessing it and    when finished.
- `parentItemIdentifier`: The persistent identifier for the directory where the item will be imported.
- `completionHandler`: A block that takes the following parameters:

## See Also

- [Providing support for user-driven actions](providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
- [func createDirectory(withName: String, inParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/createdirectory(withname:inparentitemidentifier:completionhandler:).md)
  Creates a directory with the given name inside the given parent directory.
- [func deleteItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/deleteitem(withidentifier:completionhandler:).md)
  Permanently deletes an item from the trash.
- [func renameItem(withIdentifier: NSFileProviderItemIdentifier, toName: String, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/renameitem(withidentifier:toname:completionhandler:).md)
  Renames a document or directory.
- [func reparentItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemWithIdentifier: NSFileProviderItemIdentifier, newName: String?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/reparentitem(withidentifier:toparentitemwithidentifier:newname:completionhandler:).md)
  Moves the specified item into the given parent directory.
- [func setFavoriteRank(NSNumber?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/setfavoriterank(_:foritemidentifier:completionhandler:).md)
  Marks a directory as a favorite and sets its relative order in the Favorites list.
- [func setLastUsedDate(Date?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/setlastuseddate(_:foritemidentifier:completionhandler:).md)
  Marks an item as recently used and sets its relative order in the Recents list.
- [func setTagData(Data?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/settagdata(_:foritemidentifier:completionhandler:).md)
  Tags an item.
- [func trashItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/trashitem(withidentifier:completionhandler:).md)
  Moves an item into the trash.
- [func untrashItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemIdentifier: NSFileProviderItemIdentifier?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](nsfileproviderextension/untrashitem(withidentifier:toparentitemidentifier:completionhandler:).md)
  Moves an item out of the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/importdocument(at:toparentitemidentifier:completionhandler:))*