# suggestedBatchSize

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The batch size that the system recommends.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var suggestedBatchSize: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger suggestedBatchSize;
```

## Discussion

The system suggests the batch size to optimize performance based on the context of the pending changes. The system can request the enumeration of a container for various reasons, such as if the user has the directory open in Finder, or the file open in an application. Each case has its own performance profile.

If the enumerator has more pending changes than the suggested batch size, it should split the changes into batches that are equal to or smaller than the batch size. If the enumerator has fewer changes than the suggested batch size, return all the changes immediately and finish the enumeration. You don’t need to wait for more incoming changes.

While using the suggested batch size helps ensure the best user experience, the system enforces a maximum of 100 times the suggested size.

## See Also

### Observing Changes
- [func didDeleteItems(withIdentifiers: [NSFileProviderItemIdentifier])](./diddeleteitems%28withidentifiers%29.md)
  Tells the observer that the specified items have been deleted.
- [func didUpdate([any NSFileProviderItemProtocol])](./didupdate%28_%29.md)
  Tells the observer that the specified items have been updated.
- [func finishEnumeratingChanges(upTo: NSFileProviderSyncAnchor, moreComing: Bool)](./finishenumeratingchanges%28upto,morecoming%29.md)
  Tells the observer that all of the changes have been enumerated up to the specified sync anchor.
- [func finishEnumeratingWithError(any Error)](./finishenumeratingwitherror%28_%29.md)
  Tells the observer that an error occurred during change notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderchangeobserver/suggestedbatchsize)*