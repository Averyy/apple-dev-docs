# reimportItems(below:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Tells the system to reimport the item and its content recursively.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func reimportItems(below itemIdentifier: NSFileProviderItemIdentifier) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func reimportItems(below itemIdentifier: NSFileProviderItemIdentifier) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method tells the system that the specified item identifiers are no longer valid. Your file provider extension should call this method if it has lost track of its synchronization state and can’t guarantee the stability of the item identifiers anymore.

The system calls [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) and passes the [`mayAlreadyExist`](nsfileprovidercreateitemoptions/mayalreadyexist.md) option for each affected identifier in its working set. Your File Provider extension can then specify a new identifier for each item.

The system then calls [`importDidFinish(completionHandler:)`](nsfileproviderreplicatedextension/importdidfinish(completionhandler:).md) when the import is complete. If successful, the system always reimports the specified subtree, but it may reimport other items as well. If the item specified by the `itemIdentifier` parameter has no on-disk representation, the method fails with an [`NSFileProviderError.Code.noSuchItem`](nsfileprovidererror/code/nosuchitem.md) error.

If your file provider loses synchronization but is still able to guarantee the stability of the identifiers, you don’t need to reimport the items. Instead, if the system queries the working set with an anchor that predates the synchronization loss, your File Provider extension can fail with an [`NSFileProviderError.Code.syncAnchorExpired`](nsfileprovidererror/code/syncanchorexpired.md) error.

If your file provider loses synchronization, but you aren’t interested in preserving the local data, you can resolve the issue by removing and then adding the domain back.

## Parameters

- `itemIdentifier`: The identifier of the item to reimport. The system reimports the item and all of its children.
- `completionHandler`: A block called by the system immediately after receiving the request. The completion handler takes the following parameters:

## See Also

- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/evictitem(identifier:completionhandler:).md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:).md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:completionhandler:).md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:).md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](nsfileprovidermanager/enumeratorformaterializeditems.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](nsfileprovidermanager/enumeratorforpendingitems.md)
  Returns an enumerator for the set of pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/reimportitems(below:completionhandler:))*