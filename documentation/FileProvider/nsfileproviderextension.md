# NSFileProviderExtension

**Framework**: File Provider  
**Kind**: class  
**Role**: Class

The principal class for the nonreplicated File Provider extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderExtension
```

```objc
@interface NSFileProviderExtension : NSObject
```

## Overview

To create a nonreplicated File Provider extension, start by creating a subclass of the [`NSFileProviderExtension`](./nsfileproviderextension.md) class. When implementing your [`NSFileProviderExtension`](./nsfileproviderextension.md) subclass, remember:

- Override all of the extension’s methods (except the deprecated methods), even if your implementation is only an empty method.
- Use your method implementations to provide access to the documents and folders managed by your file provider.
- Don’t call `super` in your method implementations.

Don’t use the [`NSFileProviderExtension`](./nsfileproviderextension.md) class in macOS. Instead, create an [`NSObject`](../ObjectiveC/nsobject-swift.class.md) subclass that adopts the [`NSFileProviderReplicatedExtension`](./nsfileproviderreplicatedextension.md) and [`NSFileProviderEnumerating`](./nsfileproviderenumerating.md) protocols. For more information, see [Replicated File Provider extension](./replicated-file-provider-extension.md).

## Topics

### Working with items and persistent identifiers
- [func persistentIdentifierForItem(at: URL) -> NSFileProviderItemIdentifier?](./nsfileproviderextension/persistentidentifierforitem%28at%29.md)
  Returns a unique identifier for the given URL.
- [func urlForItem(withPersistentIdentifier: NSFileProviderItemIdentifier) -> URL?](./nsfileproviderextension/urlforitem%28withpersistentidentifier%29.md)
  Returns the URL for a given persistent identifier.
- [func item(for: NSFileProviderItemIdentifier) throws -> NSFileProviderItem](./nsfileproviderextension/item%28for%29.md)
  Returns a description of the item associated with the persistent identifier.
- [func enumerator(for: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator](./nsfileproviderextension/enumerator%28for%29.md)
  Returns an enumerator for the specified item.
- [struct NSFileProviderItemIdentifier](./nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
### Managing shared files
- [func itemChanged(at: URL)](./nsfileproviderextension/itemchanged%28at%29.md)
  Tells the File Provider extension that a document has changed.
- [func providePlaceholder(at: URL, completionHandler: ((any Error)?) -> Void)](./nsfileproviderextension/provideplaceholder%28at,completionhandler%29.md)
  Triggers the creation of a placeholder for the given URL.
- [func startProvidingItem(at: URL, completionHandler: ((any Error)?) -> Void)](./nsfileproviderextension/startprovidingitem%28at,completionhandler%29.md)
  Provides an actual file on disk for a placeholder.
- [func stopProvidingItem(at: URL)](./nsfileproviderextension/stopprovidingitem%28at%29.md)
  Tells the File Provider extension that a given document is no longer being accessed.
### Handling actions
- [Providing support for user-driven actions](./providing-support-for-user-driven-actions.md)
  Override methods to handle user-initiated actions.
- [func createDirectory(withName: String, inParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/createdirectory%28withname,inparentitemidentifier,completionhandler%29.md)
  Creates a directory with the given name inside the given parent directory.
- [func deleteItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./nsfileproviderextension/deleteitem%28withidentifier,completionhandler%29.md)
  Permanently deletes an item from the trash.
- [func importDocument(at: URL, toParentItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/importdocument%28at,toparentitemidentifier,completionhandler%29.md)
  Imports a file or package into the given parent directory.
- [func renameItem(withIdentifier: NSFileProviderItemIdentifier, toName: String, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/renameitem%28withidentifier,toname,completionhandler%29.md)
  Renames a document or directory.
- [func reparentItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemWithIdentifier: NSFileProviderItemIdentifier, newName: String?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/reparentitem%28withidentifier,toparentitemwithidentifier,newname,completionhandler%29.md)
  Moves the specified item into the given parent directory.
- [func setFavoriteRank(NSNumber?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/setfavoriterank%28_,foritemidentifier,completionhandler%29.md)
  Marks a directory as a favorite and sets its relative order in the Favorites list.
- [func setLastUsedDate(Date?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/setlastuseddate%28_,foritemidentifier,completionhandler%29.md)
  Marks an item as recently used and sets its relative order in the Recents list.
- [func setTagData(Data?, forItemIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/settagdata%28_,foritemidentifier,completionhandler%29.md)
  Tags an item.
- [func trashItem(withIdentifier: NSFileProviderItemIdentifier, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/trashitem%28withidentifier,completionhandler%29.md)
  Moves an item into the trash.
- [func untrashItem(withIdentifier: NSFileProviderItemIdentifier, toParentItemIdentifier: NSFileProviderItemIdentifier?, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void)](./nsfileproviderextension/untrashitem%28withidentifier,toparentitemidentifier,completionhandler%29.md)
  Moves an item out of the trash.
### Managing domains
- [var domain: NSFileProviderDomain?](./nsfileproviderextension/domain.md)
  The domain managed by this file provider object.
### Accessing thumbnails
- [func fetchThumbnails(for: [NSFileProviderItemIdentifier], requestedSize: CGSize, perThumbnailCompletionHandler: (NSFileProviderItemIdentifier, Data?, (any Error)?) -> Void, completionHandler: ((any Error)?) -> Void) -> Progress](./nsfileproviderextension/fetchthumbnails%28for,requestedsize,perthumbnailcompletionhandler,completionhandler%29.md)
  Fetches the thumbnails for items that have been enumerated by the file provider.
### Working with services
- [func supportedServiceSources(for: NSFileProviderItemIdentifier) throws -> [any NSFileProviderServiceSource]](./nsfileproviderextension/supportedservicesources%28for%29.md)
  Return an array of service sources that let the host app perform actions associated with the specified item.
- [protocol NSFileProviderServiceSource](./nsfileproviderservicesource.md)
  A service that provides a custom communication channel between the host app and the File Provider extension.
### Managing placeholders
- [class func placeholderURL(for: URL) -> URL](./nsfileproviderextension/placeholderurl%28for%29.md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: [URLResourceKey : Any]) throws](./nsfileproviderextension/writeplaceholder%28at,withmetadata%29.md)
  Writes a document placeholder with the provided metadata.
### Accessing the document storage
- [var documentStorageURL: URL](./nsfileproviderextension/documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](./nsfileproviderextension/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Nonreplicated extension
- [Content and Change Tracking](./content-and-change-tracking.md)
  Create enumerators to specify your file provider’s content, and track changes to that content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension)*