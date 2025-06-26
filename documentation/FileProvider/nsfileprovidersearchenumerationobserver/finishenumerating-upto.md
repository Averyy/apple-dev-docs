# finishEnumerating(upTo:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Finish enumerating a page of results, and optionally provide a location within the results to continue the enumeration.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func finishEnumerating(upTo nextPage: NSFileProviderPage?)
```

#### Discussion

Call this method after you make one or more calls to [`didEnumerate(_:)`](nsfileprovidersearchenumerationobserver/didenumerate(_:).md) to provide results to the observer. The collective results you provide in these calls constitues a “page” of results.

Finish your page before sending `NSFileProviderSearchEnumerationObserver/maxNumberOfResults`. If you have more results to provide, use the `nextPage` parameter to indicate where to continue in your result set. The system sends the `nextPage` parameter the next time it calls your [`enumerateSearchResults(for:startingAt:)`](nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:).md) method.

> **Note**: The [`NSFileProviderPage`](nsfileproviderpage.md) data payload is limited to 500 bytes. Sending a `nextPage` larger than this interrupts the enumeration.

## See Also

- [func finishEnumeratingWithError(any Error)](nsfileprovidersearchenumerationobserver/finishenumeratingwitherror(_:).md)
  Finishes a search enumeration by sending an error to the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/finishenumerating(upto:))*