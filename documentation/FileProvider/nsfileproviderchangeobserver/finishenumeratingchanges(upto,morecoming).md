# finishEnumeratingChanges(upTo:moreComing:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that all of the changes have been enumerated up to the specified sync anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumeratingChanges(upTo anchor: NSFileProviderSyncAnchor, moreComing: Bool)
```

```objc
- (void) finishEnumeratingChangesUpToSyncAnchor:(NSFileProviderSyncAnchor) anchor moreComing:(BOOL) moreComing;
```

## Parameters

- `anchor`: An object used to identify the end of the current batch of changes.
- `moreComing`: A Boolean value that indicates the file provider still has one or more batches of pending changes.

## See Also

### Observing Changes
- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](./diddeleteitems%28withidentifiers%29.md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](./didupdate%28_%29.md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingWithError(any Error)](./finishenumeratingwitherror%28_%29.md)
  Tells the observer that an error occurred during change notification.
- [var suggestedBatchSize: Int](./suggestedbatchsize.md)
  The batch size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/finishenumeratingchanges(upto:morecoming:))*