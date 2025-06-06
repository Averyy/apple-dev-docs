# enumeratorForMaterializedItems()

**Framework**: File Provider  
**Kind**: method

Returns an enumerator for all the items the system currently stores on disk.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

#### Discussion

In most cases, the system requests an enumerator from the File Provider. The file provider creates the enumerator, and uses it to pass information back to the system. In this case, however, the roles are reversed. The File Provider extension calls this method to request an enumerator from the system. The system then creates the enumerator and uses it to pass the list of items currently stored on disk back to the File Provider extension.

## See Also

- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/reimportitems(below:completionhandler:).md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/evictitem(identifier:completionhandler:).md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:).md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:completionhandler:).md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:).md)
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](nsfileprovidermanager/enumeratorforpendingitems.md)
  Returns an enumerator for the set of pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/enumeratorformaterializeditems())*