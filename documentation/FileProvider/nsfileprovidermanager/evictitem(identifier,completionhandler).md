# evictItem(identifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Asks the system to remove an item from its cache.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func evictItem(identifier itemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func evictItem(identifier itemIdentifier: NSFileProviderItemIdentifier) async throws
```

```objc
- (void) evictItemWithIdentifier:(NSFileProviderItemIdentifier) itemIdentifier completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func evictItem(identifier itemIdentifier: NSFileProviderItemIdentifier) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Calling this method turns a materialized item into a dataless item to free up disk space. For more information on materialized and dataless items, see [Synchronizing the File Provider Extension](../synchronizing-the-file-provider-extension.md).

If the item is a document without local changes, this method deletes the local copy of the item’s content. If the item has local changes, it fails with an [`NSFileWriteNoPermissionError`](../../Foundation/nsfilewritenopermissionerror-swift.var.md) error.

When called on a directory, the system recursively evicts the directory’s content. It deletes the content of any materialized files, and recursively evicts any subdirectories. After it has successfully evicted all the content, it deletes its list of the directory’s content, making the directory dataless. The next time the system accesses the directory, it requests a list of the contents using the [`NSFileProviderEnumerating`](../nsfileproviderenumerating.md) protocol.

If the system encounters a nonevictable child, eviction stops immediately, and the system calls the completion handler with a [`NSFileProviderError.Code.nonEvictableChildren`](../nsfileprovidererror/code/nonevictablechildren.md) error. The error includes information about the nonevictable child in its [`underlyingErrors`](../../Foundation/nserror/underlyingerrors.md) property. The system may have evicted other materialized items, based on the traversal order.

The system calls the completion handler after it successfully evicts all items, or immediately when an error occurs. Eviction might fail with the following errors:

- [`NSFileProviderError.Code.unsyncedEdits`](../nsfileprovidererror/code/unsyncededits.md) if the item had nonuploaded changes.
- [`NSFileProviderError.Code.nonEvictable`](../nsfileprovidererror/code/nonevictable.md) if the user has marked the item as nonevictable.
- `EBUSY` if the item has open file descriptors on it.
- `EMLINK` if the item has too many hardlinks.
- Other [`NSPOSIXErrorDomain`](../../Foundation/nsposixerrordomain.md) error codes if the system can’t access or manipulate the corresponding file.

## Parameters

- `itemIdentifier`: The item’s identifier.
- `completionHandler`: A block that the system calls after removing the item from disk. The system passes the following parameter:

  - **`error`**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.

## See Also

### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](./requestdownloadforitem%28withidentifier,requestedrange%29.md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](./requestdownloadforitem%28withidentifier,requestedrange,completionhandler%29.md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](./requestmodification%28of,foritemwithidentifier,options,completionhandler%29.md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](./enumeratorformaterializeditems%28%29.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](./enumeratorforpendingitems%28%29.md)
  Returns an enumerator for the set of pending items.
- [- requestDownloadForItemWithIdentifier:requestedRange:completionHandler:](./requestdownloadforitemwithidentifier_requestedrange_completionhandler_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/evictitem(identifier:completionhandler:))*