# requestModification(of:forItemWithIdentifier:options:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func requestModification(of fields: NSFileProviderItemFields, forItemWithIdentifier itemIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions = [], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func requestModification(of fields: NSFileProviderItemFields, forItemWithIdentifier itemIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions = []) async throws
```

```objc
- (void) requestModificationOfFields:(NSFileProviderItemFields) fields forItemWithIdentifier:(NSFileProviderItemIdentifier) itemIdentifier options:(NSFileProviderModifyItemOptions) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestModification(of fields: NSFileProviderItemFields, forItemWithIdentifier itemIdentifier: NSFileProviderItemIdentifier, options: NSFileProviderModifyItemOptions = []) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Working with items
- [func reimportItems(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./reimportitems%28below,completionhandler%29.md)
  Tells the system to reimport the item and its content recursively.
- [func evictItem(identifier: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./evictitem%28identifier,completionhandler%29.md)
  Asks the system to remove an item from its cache.
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?) async throws](./requestdownloadforitem%28withidentifier,requestedrange%29.md)
- [func requestDownloadForItem(withIdentifier: NSFileProviderItemIdentifier, requestedRange: NSRange?, completionHandler: ((any Error)?) -> Void)](./requestdownloadforitem%28withidentifier,requestedrange,completionhandler%29.md)
- [func enumeratorForMaterializedItems() -> any NSFileProviderEnumerator](./enumeratorformaterializeditems%28%29.md)
  Returns an enumerator for all the items the system currently stores on disk.
- [func enumeratorForPendingItems() -> any NSFileProviderPendingSetEnumerator](./enumeratorforpendingitems%28%29.md)
  Returns an enumerator for the set of pending items.
- [- requestDownloadForItemWithIdentifier:requestedRange:completionHandler:](./requestdownloadforitemwithidentifier_requestedrange_completionhandler_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/requestmodification(of:foritemwithidentifier:options:completionhandler:))*