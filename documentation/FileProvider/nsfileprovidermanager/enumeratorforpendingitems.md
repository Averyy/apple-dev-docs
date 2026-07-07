# enumeratorForPendingItems()

**Framework**: File Provider  
**Kind**: method

Returns an enumerator for the set of pending items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator
```

#### Discussion

When the set of pending items changes, the system calls [`pendingItemsDidChange(completionHandler:)`](nsfileproviderreplicatedextension/pendingitemsdidchange(completionhandler:).md).

## See Also

- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/reimportitems(below:completionhandler:).md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/evictitem(identifier:completionhandler:).md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:).md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:completionhandler:).md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:).md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](nsfileprovidermanager/enumeratorformaterializeditems.md)
  Returns an enumerator for all the items the system currently stores on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/enumeratorforpendingitems())*