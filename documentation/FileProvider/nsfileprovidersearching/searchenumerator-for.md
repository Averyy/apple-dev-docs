# searchEnumerator(for:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Provides an object that enumerates over search results, in response to a call from the system.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func searchEnumerator(for request: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator
```

#### Return Value

An [`NSFileProviderSearchEnumerator`](nsfileprovidersearchenumerator.md) that you implement to provide search results to the system.

## Parameters

- `request`: An   that contains the search query.

## See Also

- [class NSFileProviderStringSearchRequest](nsfileproviderstringsearchrequest.md)
  A type that contains details of a string-based search request.
- [protocol NSFileProviderSearchEnumerator](nsfileprovidersearchenumerator.md)
  A protocol that defines methods for providing search results and canceling searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearching/searchenumerator(for:))*