# enumeratorForPendingItems()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns an enumerator for the set of pending items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator
```

```objc
- (id<NSFileProviderPendingSetEnumerator>) enumeratorForPendingItems;
```

#### Discussion

When the set of pending items changes, the system calls [`pendingItemsDidChange(completionHandler:)`](../nsfileproviderreplicatedextension/pendingitemsdidchange%28completionhandler%29.md).

## See Also

### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./evictitem%28identifier,completionhandler%29.md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](./requestdownloadforitem%28withidentifier,requestedrange%29.md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](./requestdownloadforitem%28withidentifier,requestedrange,completionhandler%29.md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](./requestmodification%28of,foritemwithidentifier,options,completionhandler%29.md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](./enumeratorformaterializeditems%28%29.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [- requestDownloadForItemWithIdentifier:requestedRange:completionHandler:](./requestdownloadforitemwithidentifier_requestedrange_completionhandler_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/enumeratorforpendingitems())*