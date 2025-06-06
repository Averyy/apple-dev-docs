# modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the file provider that an item’s content or metadata changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func modifyItem(_ item: NSFileProviderItem, baseVersion version: NSFileProviderItemVersion, changedFields: NSFileProviderItemFields, contents newContents: URL?, options: NSFileProviderModifyItemOptions = [], request: NSFileProviderRequest, completionHandler: @escaping (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress
```

#### Return Value

An item that tracks your extension’s progress.

#### Discussion

The system calls this method when the user modifies an item—for example, moving it, renaming it, or updating its content. The `changedFields` parameter may contain multiple items, indicating that multiple changes have occurred. Update the version of the item in your remote storage to match, and then call the callback handler.

## Parameters

- `item`: The item to modify.
- `version`: The item’s version.
- `changedFields`: The fields that have changed.
- `newContents`: A URL for the local copy of the item’s new contents.
- `options`: The modification options.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `completionHandler`: A block that you call after uploading the changes to your remote storage. You pass the following parameters:

## See Also

- [func createItem(basedOn: NSFileProviderItem, fields: NSFileProviderItemFields, contents: URL?, options: NSFileProviderCreateItemOptions, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md)
  Tells the file provider to create or import an item based on a template.
- [struct NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions.md)
  Options for creating items.
- [struct NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions.md)
  Options for modifying items.
- [func deleteItem(identifier: NSFileProviderItemIdentifier, baseVersion: NSFileProviderItemVersion, options: NSFileProviderDeleteItemOptions, request: NSFileProviderRequest, completionHandler: ((any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:).md)
  Tells the file provider to delete an item forever.
- [struct NSFileProviderDeleteItemOptions](nsfileproviderdeleteitemoptions.md)
  Options for deleting items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:))*