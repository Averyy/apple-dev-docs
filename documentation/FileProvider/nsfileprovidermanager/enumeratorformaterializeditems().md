# enumeratorForMaterializedItems()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns an enumerator for all the items the system currently stores on disk.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator
```

```objc
- (id<NSFileProviderEnumerator>) enumeratorForMaterializedItems;
```

## Mentions

- [Synchronizing the File Provider Extension](../synchronizing-the-file-provider-extension.md)

## Discussion

In most cases, the system requests an enumerator from the File Provider. The file provider creates the enumerator, and uses it to pass information back to the system. In this case, however, the roles are reversed. The File Provider extension calls this method to request an enumerator from the system. The system then creates the enumerator and uses it to pass the list of items currently stored on disk back to the File Provider extension.

## See Also

### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./evictitem%28identifier,completionhandler%29.md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](./requestdownloadforitem%28withidentifier,requestedrange%29.md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](./requestdownloadforitem%28withidentifier,requestedrange,completionhandler%29.md)
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](./requestmodification%28of,foritemwithidentifier,options,completionhandler%29.md)
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](./enumeratorforpendingitems%28%29.md)
  Returns an enumerator for the set of pending items.
- [- requestDownloadForItemWithIdentifier:requestedRange:completionHandler:](./requestdownloadforitemwithidentifier_requestedrange_completionhandler_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/enumeratorformaterializeditems())*