# requestDownloadForItemWithIdentifier:requestedRange:completionHandler:

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 13.0+

## Declaration

```objc
- (void) requestDownloadForItemWithIdentifier:(NSFileProviderItemIdentifier) itemIdentifier requestedRange:(NSRange) rangeToMaterialize completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./evictitem%28identifier,completionhandler%29.md)
  Asks the system to remove an item from its cache.
- [func requestModification(of: NSFileProviderItemFields, forItemWithIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions, completionHandler: ((any Error)?) -> Void)](./requestmodification%28of,foritemwithidentifier,options,completionhandler%29.md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](./enumeratorformaterializeditems%28%29.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](./enumeratorforpendingitems%28%29.md)
  Returns an enumerator for the set of pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/requestdownloadforitemwithidentifier:requestedrange:completionhandler:)*