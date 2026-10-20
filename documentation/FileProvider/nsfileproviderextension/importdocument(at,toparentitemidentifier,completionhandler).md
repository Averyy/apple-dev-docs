# importDocument(at:toParentItemIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Imports a file or package into the given parent directory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
func importDocument(at fileURL: URL, toParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping @Sendable (NSFileProviderItem?, (any Error)?) -> Void)
```

```swift
func importDocument(at fileURL: URL, toParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
```

```objc
- (void) importDocumentAtURL:(NSURL *) fileURL toParentItemIdentifier:(NSFileProviderItemIdentifier) parentItemIdentifier completionHandler:(void (^)(NSFileProviderItem importedDocumentItem, NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func importDocument(at fileURL: URL, toParentItemIdentifier parentItemIdentifier: NSFileProviderItemIdentifier) async throws -> NSFileProviderItem
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method is called when the user imports a document or directory. Override this method to move the file at the provided security-scoped URL to the file provider’s storage. Your implementation should return immediately. Call the completion handler before performing any network activity or other long-running tasks. Defer these tasks to the background.

The `importedDocumentItem` instance that you pass to the completion handler must define the following properties:

- **[`itemIdentifier`](../nsfileprovideritemprotocol/itemidentifier.md)**: This identifier may be temporary. If you later receive a permanent identifier from your server, delete the temporary item and add the permanent one.
- **[`parentItemIdentifier`](../nsfileprovideritemprotocol/parentitemidentifier.md)**: Set to the value passed to the `parentItemIdentifier` parameter.
- **[`filename`](../nsfileprovideritemprotocol/filename.md)**: Set to the `fileURL` parameter’s  [`nameKey`](../../Foundation/urlresourcekey/namekey.md) resource value.
- **[`creationDate`](../nsfileprovideritemprotocol/creationdate.md)**: Set to the `fileURL` parameter’s  [`creationDateKey`](../../Foundation/urlresourcekey/creationdatekey.md) resource value.
- **[`contentModificationDate`](../nsfileprovideritemprotocol/contentmodificationdate.md)**: Set to the `fileURL` parameter’s  [`contentModificationDateKey`](../../Foundation/urlresourcekey/contentmodificationdatekey.md) resource value.
- **[`typeIdentifier`](../nsfileprovideritemprotocol/typeidentifier.md)**: Set to the `fileURL` parameter’s  [`typeIdentifierKey`](../../Foundation/urlresourcekey/typeidentifierkey.md) resource value.
- **[`documentSize`](../nsfileprovideritemprotocol/documentsize.md)**: For a flat file, set to the `fileURL` parameter’s [`totalFileSizeKey`](../../Foundation/urlresourcekey/totalfilesizekey.md) resource value. For a package, set to the sum of the contents’ file sizes.
- **[`capabilities`](../nsfileprovideritemprotocol/capabilities.md)**: Set to define the actions that the user can perform on the directory (for example, [`allowsReading`](../nsfileprovideritemcapabilities/allowsreading.md) and [`allowsWriting`](../nsfileprovideritemcapabilities/allowswriting.md)).

The user’s ability to import an item into a directory is controlled by the parent directory’s [`allowsAddingSubItems`](../nsfileprovideritemcapabilities/allowsaddingsubitems.md) capability.

## Parameters

- `fileURL`: A security-scoped URL for the file to import. Call [`startAccessingSecurityScopedResource()`](../../Foundation/url/startaccessingsecurityscopedresource%28%29.md) on the URL before accessing it and  [`stopAccessingSecurityScopedResource()`](../../Foundation/url/stopaccessingsecurityscopedresource%28%29.md) when finished.
- `parentItemIdentifier`: The persistent identifier for the directory where the item will be imported.
- `completionHandler`: A block that takes the following parameters:

  - **`importedDocumentItem`**: A provider item that describes the newly imported item, or `nil` if an error occurred.
  - **`error`**: An error object. If an error occurs, pass in an object that describes the error; otherwise, set it to `nil`.

## See Also

### Handling actions
- [Providing support for user-driven actions](../providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
- [func createDirectory(withName: String, inParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./createdirectory%28withname,inparentitemidentifier,completionhandler%29.md)
  Creates a directory with the given name inside the given parent directory.
- [func deleteItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./deleteitem%28withidentifier,completionhandler%29.md)
  Permanently deletes an item from the trash.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/importdocument(at:toparentitemidentifier:completionhandler:))*