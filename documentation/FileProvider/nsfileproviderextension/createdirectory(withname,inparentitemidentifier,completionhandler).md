# createDirectory(withName:inParentItemIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Creates a directory with the given name inside the given parent directory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func createDirectory(withName directoryName: String, inParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping @Sendable (NSFileProviderItem?, (any Error)?) -> Void)
```

```swift
func createDirectory(withName directoryName: String, inParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
```

```objc
- (void) createDirectoryWithName:(NSString *) directoryName inParentItemIdentifier:(NSFileProviderItemIdentifier) parentItemIdentifier completionHandler:(void (^)(NSFileProviderItem createdDirectoryItem, NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func createDirectory(withName directoryName: String, inParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method is called when the user creates a directory. Override this method to create the directory locally. Your implementation should return immediately. Call the completion handler before performing any network activity or other long-running tasks. Defer these tasks to the background.

The `createdDirectoryItem` instance that you pass to the completion handler must define the following properties:

- **[`itemIdentifier`](../nsfileprovideritemprotocol/itemidentifier.md)**: This identifier may be temporary. If you later receive a permanent identifier from your server, delete the temporary item and add the permanent one.
- **[`parentItemIdentifier`](../nsfileprovideritemprotocol/parentitemidentifier.md)**: Set to the value passed to the `parentItemIdentifier` parameter.
- **[`filename`](../nsfileprovideritemprotocol/filename.md)**: Set to the value passed to the `directoryName` parameter.
- **[`creationDate`](../nsfileprovideritemprotocol/creationdate.md)**: Set to the current date and time.
- **[`typeIdentifier`](../nsfileprovideritemprotocol/typeidentifier.md)**: Set to `public.folder`.
- **[`childItemCount`](../nsfileprovideritemprotocol/childitemcount.md)**: Set to `0`.
- **[`capabilities`](../nsfileprovideritemprotocol/capabilities.md)**: Set to define the actions that the user can perform on the directory (for example, [`allowsAddingSubItems`](../nsfileprovideritemcapabilities/allowsaddingsubitems.md), [`allowsReading`](../nsfileprovideritemcapabilities/allowsreading.md), and [`allowsWriting`](../nsfileprovideritemcapabilities/allowswriting.md)).

The user’s ability to create a directory is controlled by the parent directory’s [`allowsAddingSubItems`](../nsfileprovideritemcapabilities/allowsaddingsubitems.md) capability.

## Parameters

- `directoryName`: The name of the directory to be created.
- `parentItemIdentifier`: The persistent identifier for the parent directory.
- `completionHandler`: A block that takes the following parameters:

  - **`createdDirectoryItem`**: A provider item that describes the newly created directory, or `nil` if an error occurred.
  - **`error`**: An error object. If an error occurs, pass in an object that describes the error; otherwise, set it to `nil`.

## See Also

### Handling actions
- [Providing support for user-driven actions](../providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
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
- [func trashItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./trashitem%28withidentifier,completionhandler%29.md)
  Moves an item into the trash.
- [func untrashItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemIdentifier: NSFileProviderItemIdentifier?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./untrashitem%28withidentifier,toparentitemidentifier,completionhandler%29.md)
  Moves an item out of the trash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/createdirectory(withname:inparentitemidentifier:completionhandler:))*