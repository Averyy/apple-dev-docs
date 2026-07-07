# NSFileProviderExtension

**Framework**: File Provider  
**Kind**: class

The principal class for the nonreplicated File Provider extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderExtension
```

#### Overview

To create a nonreplicated File Provider extension, start by creating a subclass of the [`NSFileProviderExtension`](nsfileproviderextension.md) class. When implementing your [`NSFileProviderExtension`](nsfileproviderextension.md) subclass, remember:

- Override all of the extension’s methods (except the deprecated methods), even if your implementation is only an empty method.
- Use your method implementations to provide access to the documents and folders managed by your file provider.
- Don’t call `super` in your method implementations.

Don’t use the [`NSFileProviderExtension`](nsfileproviderextension.md) class in macOS. Instead, create an [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) subclass that adopts the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) and [`NSFileProviderEnumerating`](nsfileproviderenumerating.md) protocols. For more information, see [`Replicated File Provider extension`](replicated-file-provider-extension.md).

## Topics

### Working with items and persistent identifiers
- [func persistentIdentifierForItem(at: URL) -> NSFileProviderItemIdentifier?](nsfileproviderextension/persistentidentifierforitem(at:).md)
  Returns a unique identifier for the given URL.
- [func urlForItem(withPersistentIdentifier: NSFileProviderItemIdentifier) -> URL?](nsfileproviderextension/urlforitem(withpersistentidentifier:).md)
  Returns the URL for a given persistent identifier.
- [func item(for: NSFileProviderItemIdentifier) throws -> NSFileProviderItem](nsfileproviderextension/item(for:).md)
  Returns a description of the item associated with the persistent identifier.
- [func enumerator(for: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator](nsfileproviderextension/enumerator(for:).md)
  Returns an enumerator for the specified item.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
### Managing shared files
- [func itemChanged(at: URL)](nsfileproviderextension/itemchanged(at:).md)
  Tells the File Provider extension that a document has changed.
- [func providePlaceholder(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/provideplaceholder(at:completionhandler:).md)
  Triggers the creation of a placeholder for the given URL.
- [func startProvidingItem(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/startprovidingitem(at:completionhandler:).md)
  Provides an actual file on disk for a placeholder.
- [func stopProvidingItem(at: URL)](nsfileproviderextension/stopprovidingitem(at:).md)
  Tells the File Provider extension that a given document is no longer being accessed.
### Handling actions
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
### Managing domains
- [var domain: NSFileProviderDomain?](nsfileproviderextension/domain.md)
  The domain managed by this file provider object.
### Accessing thumbnails
- [func fetchThumbnails(for: [NSFileProviderItemIdentifier], requestedSize: CGSize, perThumbnailCompletionHandler: (NSFileProviderItemIdentifier, Data?, (any Error)?) -> Void, completionHandler: ((any Error)?) -> Void) -> Progress](nsfileproviderextension/fetchthumbnails(for:requestedsize:perthumbnailcompletionhandler:completionhandler:).md)
  Fetches the thumbnails for items that have been enumerated by the file provider.
### Working with services
- [func supportedServiceSources(for: NSFileProviderItemIdentifier) throws -> [any NSFileProviderServiceSource]](nsfileproviderextension/supportedservicesources(for:).md)
  Return an array of service sources that let the host app perform actions associated with the specified item.
- [protocol NSFileProviderServiceSource](nsfileproviderservicesource.md)
  A service that provides a custom communication channel between the host app and the File Provider extension.
### Managing placeholders
- [class func placeholderURL(for: URL) -> URL](nsfileproviderextension/placeholderurl(for:).md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: [URLResourceKey : Any]) throws](nsfileproviderextension/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.
### Accessing the document storage
- [var documentStorageURL: URL](nsfileproviderextension/documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](nsfileproviderextension/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Content and Change Tracking](content-and-change-tracking.md)
  Create enumerators to specify your file provider’s content, and track changes to that content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension)*