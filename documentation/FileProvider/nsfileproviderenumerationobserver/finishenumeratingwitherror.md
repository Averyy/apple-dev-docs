# finishEnumeratingWithError(_:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the observer that an error occurred during item enumeration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func finishEnumeratingWithError(_ error: any Error)
```

## Mentions

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)

## See Also

- [func didEnumerate([any NSFileProviderItemProtocol])](nsfileproviderenumerationobserver/didenumerate(_:).md)
  Provides a batch of enumerated items.
- [func finishEnumerating(upTo: NSFileProviderPage?)](nsfileproviderenumerationobserver/finishenumerating(upto:).md)
  Tells the observer that all of the items have been enumerated up to the specified page.
- [var suggestedPageSize: Int](nsfileproviderenumerationobserver/suggestedpagesize.md)
  The page size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver/finishenumeratingwitherror(_:))*