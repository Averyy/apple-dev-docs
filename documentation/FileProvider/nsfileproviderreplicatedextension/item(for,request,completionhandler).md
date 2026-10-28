# item(for:request:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the file provider for the metadata of the provided item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func item(for identifier: NSFileProviderItemIdentifier, request: NSFileProviderRequest, completionHandler: @escaping (NSFileProviderItem?, (any Error)?) -> Void) -> Progress
```

```objc
- (NSProgress *) itemForIdentifier:(NSFileProviderItemIdentifier) identifier request:(NSFileProviderRequest *) request completionHandler:(void (^)(NSFileProviderItem , NSError *)) completionHandler;
```

## Return Value

An item that tracks your extension’s progress. The system automatically calls [`cancel()`](../../Foundation/progress/cancel%28%29.md)  on the progress object when an error occurs.

## Discussion

If your extension doesn’t recognize the item, pass [`NSFileProviderError.Code.noSuchItem`](../nsfileprovidererror/code/nosuchitem.md) to the handler. The system assumes the item is no longer in the domain, and attempts to delete the local copy. If the delete attempt fails because the item has local changes, the system reimports the item by calling [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](./createitem%28basedon,fields,contents,options,request,completionhandler%29.md).

If you pass [`NSFileProviderError.Code.notAuthenticated`](../nsfileprovidererror/code/notauthenticated.md) or [`NSFileProviderError.Code.serverUnreachable`](../nsfileprovidererror/code/serverunreachable.md) to the handler, the system presents an appropriate alert to the user, but doesn’t try to access the metadata until triggered again by the user.

The system considers any other errors to be transient, and automatically retries the method call.

## Parameters

- `identifier`: The item’s identifier.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `completionHandler`: A block that you call after downloading the item’s metadata. The block takes the following parameters:

  - **`item`**: A new file provider item, containing all the item’s metadata.
  - **`error`**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.

## See Also

### Accessing Remote Content
- [func fetchContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion?, request: NSFileProviderRequest, completionHandler: (URL?, NSFileProviderItem?, (any Error)?) -> Void) -> Progress](./fetchcontents%28for,version,request,completionhandler%29.md)
  Tells the file provider to download the requested item from remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/item(for:request:completionhandler:))*