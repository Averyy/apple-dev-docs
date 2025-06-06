# NSFileProviderEnumerationObserver

**Framework**: File Provider  
**Kind**: protocol

An observer that receives batches of items during enumeration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderEnumerationObserver : NSObjectProtocol
```

## Mentions

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)

## Topics

### Observing Item Enumeration
- [func didEnumerate([any NSFileProviderItemProtocol])](nsfileproviderenumerationobserver/didenumerate(_:).md)
  Provides a batch of enumerated items.
- [func finishEnumerating(upTo: NSFileProviderPage?)](nsfileproviderenumerationobserver/finishenumerating(upto:).md)
  Tells the observer that all of the items have been enumerated up to the specified page.
- [func finishEnumeratingWithError(any Error)](nsfileproviderenumerationobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during item enumeration.
- [var suggestedPageSize: Int](nsfileproviderenumerationobserver/suggestedpagesize.md)
  The page size that the system recommends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)
  Create enumerators to specify your file provider’s content.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver)*