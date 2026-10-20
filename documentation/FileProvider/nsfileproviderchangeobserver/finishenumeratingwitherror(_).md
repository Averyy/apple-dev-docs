# finishEnumeratingWithError(_:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that an error occurred during change notification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumeratingWithError(_ error: any Error)
```

```objc
- (void) finishEnumeratingWithError:(NSError *) error;
```

## Parameters

- `error`: An object that contains information about the error.

## See Also

### Observing Changes
- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](./diddeleteitems%28withidentifiers%29.md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](./didupdate%28_%29.md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingChanges(upTo: NSFileProviderSyncAnchor, moreComing: Bool)](./finishenumeratingchanges%28upto,morecoming%29.md)
  Tells the observer that all of the changes have been enumerated up to the specified sync anchor.
- [var suggestedBatchSize: Int](./suggestedbatchsize.md)
  The batch size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/finishenumeratingwitherror(_:))*