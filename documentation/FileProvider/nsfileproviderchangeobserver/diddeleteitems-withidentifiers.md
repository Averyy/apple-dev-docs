# didDeleteItems(withIdentifiers:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the observer that the specified items have been deleted.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func didDeleteItems(withIdentifiers deletedItemIdentifiers: [NSFileProviderItemIdentifier])
```

## Parameters

- `deletedItemIdentifiers`: An array of identifiers for the deleted items.

## See Also

- [func didUpdate([any NSFileProviderItemProtocol])](nsfileproviderchangeobserver/didupdate(_:).md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingChanges(upTo: NSFileProviderSyncAnchor, moreComing: Bool)](nsfileproviderchangeobserver/finishenumeratingchanges(upto:morecoming:).md)
  Tells the observer that all of the changes have been enumerated up to the specified sync anchor.
- [func finishEnumeratingWithError(any Error)](nsfileproviderchangeobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during change notification.
- [var suggestedBatchSize: Int](nsfileproviderchangeobserver/suggestedbatchsize.md)
  The batch size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/diddeleteitems(withidentifiers:))*