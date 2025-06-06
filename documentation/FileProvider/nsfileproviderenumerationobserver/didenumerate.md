# didEnumerate(_:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Provides a batch of enumerated items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func didEnumerate(_ updatedItems: [any NSFileProviderItemProtocol])
```

## Mentions

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)

## See Also

- [func finishEnumerating(upTo: NSFileProviderPage?)](nsfileproviderenumerationobserver/finishenumerating(upto:).md)
  Tells the observer that all of the items have been enumerated up to the specified page.
- [func finishEnumeratingWithError(any Error)](nsfileproviderenumerationobserver/finishenumeratingwitherror(_:).md)
  Tells the observer that an error occurred during item enumeration.
- [var suggestedPageSize: Int](nsfileproviderenumerationobserver/suggestedpagesize.md)
  The page size that the system recommends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerationobserver/didenumerate(_:))*