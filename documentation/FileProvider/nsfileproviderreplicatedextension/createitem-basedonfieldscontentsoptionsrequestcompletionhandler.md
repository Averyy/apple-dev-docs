# createItem(basedOn:fields:contents:options:request:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the file provider to create or import an item based on a template.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func createItem(basedOn itemTemplate: NSFileProviderItem, fields: NSFileProviderItemFields, contents url: URL?, options: NSFileProviderCreateItemOptions = [], request: NSFileProviderRequest, completionHandler: @escaping (NSFileProviderItem?, NSFileProviderItemFields, Bool, (any Error)?) -> Void) -> Progress
```

#### Return Value

A progress that tracks creating the item in your remote storage and uploading its content. The system automatically calls [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel())  on the progress object when an error occurs.

#### Discussion

The system calls this method when the user creates a new item or imports an item into the file provider. The system manages the local copy of the item. You’re responsible for syncing and saving the item to your remote storage.

Implement this method to create an item in your remote storage that matches the template, and then call the callback handler.

The `itemTemplate` parameter describes the item’s intended state, including:

The system sets the template’s [`itemIdentifier`](nsfileprovideritemprotocol/itemidentifier.md) to a unique value and guarantees that it remains the same for the specified item. For example, the system can reuse the identifier to replay this method after a crash.

In general, set the properties in your `createdItem` to match the `itemTemplate`. One exception is the [`itemIdentifier`](nsfileprovideritemprotocol/itemidentifier.md) property; always provide your own identifier for the item. If you reuse an existing identifier, the system replaces the local copy of the old item with the new one.

If the item is a document, fetch its contents from the `url` parameter. Otherwise, the `url` is `nil`. For symlinks, you can access the content using the template’s [`symlinkTargetPath`](nsfileprovideritemprotocol/symlinktargetpath.md) parameter. For both symlinks and aliases, make sure to return the correct UTI for the item,  because the UTI can’t be inferred from the item’s filename.

If you are reimporting an item and the system finds a local copy without any content, it sets the [`mayAlreadyExist`](nsfileprovidercreateitemoptions/mayalreadyexist.md) option, and sets the `url` to nil. In this case, if you can’t match the item with an existing item from remote storage, pass `nil` as the completion handler’s `createdItem` parameter. The system then deletes the local copy of the item.

If the attempt to create an item fails because the parent directory doesn’t exist, pass [`NSFileProviderError.Code.noSuchItem`](nsfileprovidererror/code/nosuchitem.md) to the handler. The system attempts to create the parent directory, and then tries to create the item again.

## Parameters

- `itemTemplate`: An object that defines the state of the new or imported item.
- `fields`: The fields that you should apply to the new or imported item.
- `url`: If the item is a file with the   field set, this is the URL to the item’s content. Otherwise, it’s  .
- `options`: The item creation options.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `completionHandler`: A block that you call after uploading the item to your remote storage. You pass the following parameters:

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:))*