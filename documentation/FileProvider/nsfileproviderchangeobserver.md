# NSFileProviderChangeObserver

**Framework**: File Provider  
**Kind**: protocol

An observer that receives changes and deletions during enumeration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderChangeObserver : NSObjectProtocol
```

## Topics

### Observing Changes
- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](nsfileproviderchangeobserver/diddeleteitems(withidentifiers:).md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](nsfileproviderchangeobserver/didupdate(_:).md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingChanges(upTo: NSFileProviderSyncAnchor, moreComing: Bool)](nsfileproviderchangeobserver/finishenumeratingchanges(upto:morecoming:).md)
  Tells the observer that all of the changes have been enumerated up to the specified sync anchor.
- [func finishEnumeratingWithError(any Error)](nsfileproviderchangeobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during change notification.
- [var suggestedBatchSize: Int](nsfileproviderchangeobserver/suggestedbatchsize.md)
  The batch size that the system recommends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Tracking Your File Provider’s Changes](tracking-your-file-provider-s-changes.md)
  Create an enumerator to track changes to your file provider’s content.
- [struct NSFileProviderSyncAnchor](nsfileprovidersyncanchor.md)
  A synchronization point that represents the last batch of changes returned by the enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver)*