# finishEnumerating(upTo:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that all of the items have been enumerated up to the specified page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumerating(upTo nextPage: NSFileProviderPage?)
```

```objc
- (void) finishEnumeratingUpToPage:(NSFileProviderPage) nextPage;
```

## Mentions

- [Defining Your File Provider’s Content](../defining-your-file-provider-s-content.md)

## See Also

### Observing Item Enumeration
- [func didEnumerate([any NSFileProviderItemProtocol])](./didenumerate%28_%29.md)
  Provides a batch of enumerated items.
- [func finishEnumeratingWithError(any Error)](./finishenumeratingwitherror%28_%29.md)
  Tells the observer that an error occurred during item enumeration.
- [var suggestedPageSize: Int](./suggestedpagesize.md)
  The page size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver/finishenumerating(upto:))*