# trashItem(withIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Moves an item into the trash.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func trashItem(withIdentifier itemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping @Sendable (NSFileProviderItem?, (any Error)?) -> Void)
```

```swift
func trashItem(withIdentifier itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
```

```objc
- (void) trashItemWithIdentifier:(NSFileProviderItemIdentifier) itemIdentifier completionHandler:(void (^)(NSFileProviderItem trashedItem, NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func trashItem(withIdentifier itemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method is called when the user moves a document or directory into the trash. Override this method to make any necessary local changes to move the item to the trash, including updates to the working set. Your implementation should return immediately. Call the completion handler before performing any network activity or other long-running tasks. Defer these tasks to the background. The `trashedItem` instance that you pass to the completion handler should match the item’s old file provider item, with only one change: set the item’s [`isTrashed`](../nsfileprovideritemprotocol/istrashed.md) property to [`true`](../../Swift/true.md).

Always include trashed items in your File Provider extension’s working set. Trashed items should be stored locally so that their content is available to offline users. However, if the trashed item is a directory, remove all of its children from the working set. If a shared document is trashed, stop sharing the document while it is trashed.

Be sure to record the item’s parent identifier, so that you can restore the item to its proper location in the [`untrashItem(withIdentifier:toParentItemIdentifier:completionHandler:)`](./untrashitem%28withidentifier,toparentitemidentifier,completionhandler%29.md) method. You can store this identifier in the `trashedItem` object’s [`parentItemIdentifier`](../nsfileprovideritemprotocol/parentitemidentifier.md) property.

The user’s ability to trash an item is controlled by the item’s [`allowsTrashing`](../nsfileprovideritemcapabilities/allowstrashing.md) capability.

## Parameters

- `itemIdentifier`: The item’s persistent identifier.
- `completionHandler`: A block that takes the following parameters:

  - **`trashedItem`**: A file provider item that represents the changed item, or `nil` if an error occurred.
  - **`error`**: An error object. If an error occurs, pass in an object that describes the error; otherwise, set it to `nil`.

## See Also

### Handling actions
- [Providing support for user-driven actions](../providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
- [func createDirectory(withName: String, inParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./createdirectory%28withname,inparentitemidentifier,completionhandler%29.md)
  Creates a directory with the given name inside the given parent directory.
- [func deleteItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./deleteitem%28withidentifier,completionhandler%29.md)
  Permanently deletes an item from the trash.
- [func importDocument(at: URL, toParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./importdocument%28at,toparentitemidentifier,completionhandler%29.md)
  Imports a file or package into the given parent directory.
- [func renameItem(withIdentifier: NSFileProviderItemIdentifier, toName: String, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./renameitem%28withidentifier,toname,completionhandler%29.md)
  Renames a document or directory.
- [func reparentItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemWithIdentifier: NSFileProviderItemIdentifier, newName: String?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./reparentitem%28withidentifier,toparentitemwithidentifier,newname,completionhandler%29.md)
  Moves the specified item into the given parent directory.
- [func setFavoriteRank(NSNumber?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./setfavoriterank%28_,foritemidentifier,completionhandler%29.md)
  Marks a directory as a favorite and sets its relative order in the Favorites list.
- [func setLastUsedDate(Date?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./setlastuseddate%28_,foritemidentifier,completionhandler%29.md)
  Marks an item as recently used and sets its relative order in the Recents list.
- [func setTagData(Data?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./settagdata%28_,foritemidentifier,completionhandler%29.md)
  Tags an item.
- [func untrashItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemIdentifier: NSFileProviderItemIdentifier?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./untrashitem%28withidentifier,toparentitemidentifier,completionhandler%29.md)
  Moves an item out of the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/trashitem(withidentifier:completionhandler:))*