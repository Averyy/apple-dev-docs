# NSFileProviderError.Code.localVersionConflictingWithServer

**Framework**: File Provider  
**Kind**: case

Returned by createItemBasedOnTemplate or modifyItem if the provider does not wish to sync the item.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case localVersionConflictingWithServer
```

#### Discussion

When a provider returns this error, it causes the item to be excluded from sync. The system will ensure that the item (and any descendents, in case of a directory), are downloaded, and then issue a deleteItem call to the provider for the item.

The system will call createItemBasedOnTemplate for the item, whenever the item’s metadata changes on disk. This ensures that the provider’s rules for excluding from sync are re-evaluated whenever the item’s properties change.

#### Re Evaluating Items

If the provider wishes for previously excluded items to be re-sent as createItemBasedOnTemplate calls, the provider may call -[NSFileProviderManager signalErrorResolved:completionHandler:] with this error code.

If the provider wishes to exclude items which had previously been synced, the provider may call -[NSFileProviderManager requestModificationOfFields:forItemWithIdentifier:options:completionHandler:]. This will cause the system to send a new modifyItem call to the provider. At that time, the provider can choose to return this error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/code/localversionconflictingwithserver)*