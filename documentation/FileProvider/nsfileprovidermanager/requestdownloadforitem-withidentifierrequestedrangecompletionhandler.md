# requestDownloadForItem(withIdentifier:requestedRange:completionHandler:)

**Framework**: File Provider  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func requestDownloadForItem(withIdentifier itemIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange? = nil, completionHandler: @escaping ((any Error)?) -> Void)
```

## See Also

- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/reimportitems(below:completionhandler:).md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/evictitem(identifier:completionhandler:).md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:).md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:).md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](nsfileprovidermanager/enumeratorformaterializeditems.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](nsfileprovidermanager/enumeratorforpendingitems.md)
  Returns an enumerator for the set of pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/requestdownloadforitem(withidentifier:requestedrange:completionhandler:))*