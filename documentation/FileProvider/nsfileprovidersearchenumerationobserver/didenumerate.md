# didEnumerate(_:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Delivers an array of search results to the observer.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func didEnumerate(_ searchResults: [any NSFileProviderSearchResult])
```

#### Discussion

For files stored on your server, consult search indexes on the server and use them to create an array of [`NSFileProviderSearchResult`](nsfileprovidersearchresult.md) instances that you provide to this method.

You can call this method multiple times prior to calling [`finishEnumerating(upTo:)`](nsfileprovidersearchenumerationobserver/finishenumerating(upto:).md) or [`finishEnumeratingWithError(_:)`](nsfileprovidersearchenumerationobserver/finishenumeratingwitherror(_:).md), as long as the total number of results doesn’t exceed [`maxNumberOfResults`](nsfileprovidersearchenumerationobserver/maxnumberofresults.md).

## See Also

- [protocol NSFileProviderSearchResult](nsfileprovidersearchresult.md)
  A protocol that defines properties of a search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/didenumerate(_:))*