# NSFileProviderReplicatedExtension

**Framework**: File Provider  
**Kind**: protocol

A File Provider extension in which the system replicates the contents on disk.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderReplicatedExtension : NSFileProviderEnumerating
```

## Mentions

- [Using push notifications to signal changes](using-push-notifications-to-signal-changes.md)

## Topics

### Creating and Removing File Providers
- [init(domain: NSFileProviderDomain)](nsfileproviderreplicatedextension/init(domain:).md)
  Creates an instance of the file provider for the specified domain.
- [func invalidate()](nsfileproviderreplicatedextension/invalidate.md)
  Tells the file provider to perform any necessary cleanup so that the system can deallocate it.
### Accessing Remote Content
- [func item(for: NSFileProviderItemIdentifier, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/item(for:request:completionhandler:).md)
  Asks the file provider for the metadata of the provided item.
- [func fetchContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion?, request: NSFileProviderRequest, completionHandler: (URL?, NSFileProviderItem?, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/fetchcontents(for:version:request:completionhandler:).md)
  Tells the file provider to download the requested item from remote storage.
### Managing Items
- [func createItem(basedOn: NSFileProviderItem, fields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderCreateItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md)
  Tells the file provider to create or import an item based on a template.
- [struct NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md)
  Tells the file provider that an item’s content or metadata changed.
- [struct NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions.md)
  Options for modifying items.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:).md)
  Tells the file provider to delete an item forever.
- [struct NSFileProviderDeleteItemOptions](nsfileproviderdeleteitemoptions.md)
  Options for deleting items.
### Tracking Materialized Items
- [func materializedItemsDidChange(completionHandler: () -> Void)](nsfileproviderreplicatedextension/materializeditemsdidchange(completionhandler:).md)
  Tells the file provider that the set of materialized items changed.
### Tracking Pending Items
- [func pendingItemsDidChange(completionHandler: () -> Void)](nsfileproviderreplicatedextension/pendingitemsdidchange(completionhandler:).md)
  Tells the file provider extension that the set of pending items has changed.
### Importing Domains
- [func importDidFinish(completionHandler: () -> Void)](nsfileproviderreplicatedextension/importdidfinish(completionhandler:).md)
  Tells the File Provider extension that the system finished importing items.

## Relationships

### Inherits From
- [NSFileProviderEnumerating](nsfileproviderenumerating.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFileProviderEnumerating](nsfileproviderenumerating.md)
  Support for enumerating the file provider’s contents.
- [protocol NSFileProviderIncrementalContentFetching](nsfileproviderincrementalcontentfetching.md)
  Support for fetching changes to the item’s content.
- [protocol NSFileProviderPartialContentFetching](nsfileproviderpartialcontentfetching.md)
  Support for fetching part of a file’s content.
- [protocol NSFileProviderServicing](nsfileproviderservicing.md)
  Support for providing a custom service source.
- [protocol NSFileProviderCustomAction](nsfileprovidercustomaction.md)
  Support for custom actions.
- [struct NSFileProviderExtensionActionIdentifier](nsfileproviderextensionactionidentifier.md)
  An identifier for custom actions.
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension)*