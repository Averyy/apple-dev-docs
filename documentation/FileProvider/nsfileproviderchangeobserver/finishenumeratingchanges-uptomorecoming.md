# finishEnumeratingChanges(upTo:moreComing:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the observer that all of the changes have been enumerated up to the specified sync anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumeratingChanges(upTo anchor: NSFileProviderSyncAnchor, moreComing: Bool)
```

## Parameters

- `anchor`: An object used to identify the end of the current batch of changes.
- `moreComing`: A Boolean value that indicates the file provider still has one or more batches of pending changes.

## See Also

- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](nsfileproviderchangeobserver/diddeleteitems(withidentifiers:).md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](nsfileproviderchangeobserver/didupdate(_:).md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingWithError(any Error)](nsfileproviderchangeobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during change notification.
- [var suggestedBatchSize: Int](nsfileproviderchangeobserver/suggestedbatchsize.md)
  The batch size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/finishenumeratingchanges(upto:morecoming:))*