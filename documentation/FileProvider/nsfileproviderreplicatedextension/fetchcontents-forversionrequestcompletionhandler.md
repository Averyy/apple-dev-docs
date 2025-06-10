# fetchContents(for:version:request:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the file provider to download the requested item from remote storage.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func fetchContents(for itemIdentifier: NSFileProviderItemIdentifier, version requestedVersion: NSFileProviderItemVersion?, request: NSFileProviderRequest, completionHandler: @escaping (URL?, NSFileProviderItem?, (any Error)?) -> Void) -> Progress
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

#### Return Value

An item that tracks your extension’s progress. The system automatically calls [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel())  on the progress object when an error occurs, or when the system or user cancels the download.

#### Discussion

The system initially learns about available items through enumerations; however, the enumeration only provides the item’s metadata. When the user accesses the item, the system needs to download the full contents from your remote store. After you call the completion handler, the system takes complete control over the local copy.

> **Note**:  The URL you pass to the completion handler must be on the same volume as the URL returned by the file provider manager’s  [`temporaryDirectoryURL()`](nsfileprovidermanager/temporarydirectoryurl().md) method, so that the system can clone it to provide the content for the dataless item.

If the `requestedVersion` parameter is not `nil`, you must return the specified version of the item, or return an error. If the parameter is `nil`, return a version that is the same or newer than the most recent version enumerated to the system. In either case, the [`contentVersion`](nsfileprovideritemversion/contentversion.md) of the [`NSFileProviderItem`](nsfileprovideritem-swift.typealias.md)  passed to the completion handler must match the version you return.

If your extension doesn’t recognize the item, pass [`NSFileProviderError.Code.noSuchItem`](nsfileprovidererror/code/nosuchitem.md) to the handler. The system assumes the item is no longer in the domain, and attempts to delete the local copy. If the delete attempt fails because the item has local changes, the system reimports the item by calling [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md).

If you pass [`NSFileProviderError.Code.notAuthenticated`](nsfileprovidererror/code/notauthenticated.md) or [`NSFileProviderError.Code.serverUnreachable`](nsfileprovidererror/code/serverunreachable.md) to the handler, the system presents an appropriate alert to the user, but doesn’t try to access the metadata until triggered again by the user.

If the user deletes the item before the download completes, the system calls the progress object’s [`cancel()`](https://developer.apple.com/documentation/Foundation/Progress/cancel()) method. Your file provider should stop fetching the item, and pass [`NSUserCancelledError`](https://developer.apple.com/documentation/Foundation/NSUserCancelledError-swift.var) to the handler.

The system considers any other errors to be transient, and automatically retries the method call.

## Parameters

- `itemIdentifier`: The item to fetch.
- `requestedVersion`: The version of the item. If this is  , download the latest version.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `completionHandler`: A block that you call after downloading the item from your remote storage. You pass the following parameters:

## See Also

- [func item(for: NSFileProviderItemIdentifier, request: NSFileProviderRequest, completionHandler: (NSFileProviderItem?, (any Error)?) -> Void) -> Progress](nsfileproviderreplicatedextension/item(for:request:completionhandler:).md)
  Asks the file provider for the metadata of the provided item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/fetchcontents(for:version:request:completionhandler:))*