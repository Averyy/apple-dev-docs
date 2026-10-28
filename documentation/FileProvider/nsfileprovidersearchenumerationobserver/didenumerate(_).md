# didEnumerate(_:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Delivers an array of search results to the observer.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func didEnumerate(_ searchResults: [any NSFileProviderSearchResult])
```

```objc
- (void) didEnumerateSearchResults:(NSArray<id<NSFileProviderSearchResult>> *) searchResults;
```

## Discussion

For files stored on your server, consult search indexes on the server and use them to create an array of [`NSFileProviderSearchResult`](../nsfileprovidersearchresult.md) instances that you provide to this method.

You can call this method multiple times prior to calling [`finishEnumerating(upTo:)`](./finishenumerating%28upto%29.md) or [`finishEnumeratingWithError(_:)`](./finishenumeratingwitherror%28_%29.md), as long as the total number of results doesn’t exceed `NSFileProviderSearchEnumerationObserver/maxNumberOfResults`.

## See Also

### Providing search results
- [protocol NSFileProviderSearchResult](../nsfileprovidersearchresult.md)
  A protocol that defines properties of a search result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/didenumerate(_:))*