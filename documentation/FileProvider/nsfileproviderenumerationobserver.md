# NSFileProviderEnumerationObserver

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

An observer that receives batches of items during enumeration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderEnumerationObserver : NSObjectProtocol
```

```objc
@protocol NSFileProviderEnumerationObserver <NSObject>
```

## Mentions

- [Defining Your File Provider’s Content](./defining-your-file-provider-s-content.md)

## Topics

### Observing Item Enumeration
- [func didEnumerate([any NSFileProviderItemProtocol])](./nsfileproviderenumerationobserver/didenumerate%28_%29.md)
  Provides a batch of enumerated items.
- [func finishEnumerating(upTo: NSFileProviderPage?)](./nsfileproviderenumerationobserver/finishenumerating%28upto%29.md)
  Tells the observer that all of the items have been enumerated up to the specified page.
- [func finishEnumeratingWithError(any Error)](./nsfileproviderenumerationobserver/finishenumeratingwitherror%28_%29.md)
  Tells the observer that an error occurred during item enumeration.
- [var suggestedPageSize: Int](./nsfileproviderenumerationobserver/suggestedpagesize.md)
  The page size that the system recommends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Content
- [Defining Your File Provider’s Content](./defining-your-file-provider-s-content.md)
  Create enumerators to specify your file provider’s content.
- [struct NSFileProviderPage](./nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver)*