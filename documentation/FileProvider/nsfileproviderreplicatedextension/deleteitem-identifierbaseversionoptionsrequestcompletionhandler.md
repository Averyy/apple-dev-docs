# deleteItem(identifier:baseVersion:options:request:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the file provider to delete an item forever.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion version: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions = [], request: NSFileProviderRequest, completionHandler: @escaping ((any Error)?) -> Void) -> Progress
```

#### Return Value

An item that tracks your extension’s progress.

#### Discussion

The system calls this method when the user deletes an item that was already in the trash. Users can only delete items that have the [`allowsDeleting`](nsfileprovideritemcapabilities/allowsdeleting.md) capability.

Remove the item from the trash and delete it from your remote storage. If the item is in the working set, notify the system about the change by calling [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) and passing [`workingSet`](nsfileprovideritemidentifier/workingset.md) for the `containerItemIdentifier` parameter. If the deletion is recursive, be sure to check all the deleted items, and notify the system to any changes in the working set.

If your extension doesn’t recognize the item, you can just report success. The system then removes the local copy of the item.

## Parameters

- `identifier`: The identifier of the object to delete.
- `version`: The version of the item to delete.
- `options`: The options for deleting the item.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `completionHandler`: A block that you call after deleting the item from your remote storage. You pass the following parameter:

## See Also

- [func createItem(basedOn: NSFileProviderItem, fields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderCreateItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md)
  Tells the file provider to create or import an item based on a template.
- [struct NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [func modifyItem(NSFileProviderItem, baseVersion: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderModifyItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md)
  Tells the file provider that an item’s content or metadata changed.
- [struct NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions.md)
  Options for modifying items.
- [struct NSFileProviderDeleteItemOptions](nsfileproviderdeleteitemoptions.md)
  Options for deleting items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:))*