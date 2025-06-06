# finishEnumeratingWithError(_:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the observer that an error occurred during change notification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumeratingWithError(_ error: any Error)
```

## Parameters

- `error`: An object that contains information about the error.

## See Also

- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](nsfileproviderchangeobserver/diddeleteitems(withidentifiers:).md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](nsfileproviderchangeobserver/didupdate(_:).md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingChanges(upTo: NSFileProviderSyncAnchor, moreComing: Bool)](nsfileproviderchangeobserver/finishenumeratingchanges(upto:morecoming:).md)
  Tells the observer that all of the changes have been enumerated up to the specified sync anchor.
- [var suggestedBatchSize: Int](nsfileproviderchangeobserver/suggestedbatchsize.md)
  The batch size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/finishenumeratingwitherror(_:))*