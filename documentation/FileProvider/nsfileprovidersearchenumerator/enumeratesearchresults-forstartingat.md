# enumerateSearchResults(for:startingAt:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Enumerates search results starting from the specified page, in response to a call from the framework.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func enumerateSearchResults(for observer: any NSFileProviderSearchEnumerationObserver, startingAt page: NSFileProviderPage?)
```

#### Discussion

Implement this method to perform your search and deliver pages of results to `observer`.

## Parameters

- `observer`: An  , to which your extension provides search results.
- `page`: An indication of a location within the search results to resume enumeration. This parameter is non-  if you previously provided a   parameter to the observer’s   method. Make sure the page contains whatever information you need to resume the enumeration.

## See Also

- [protocol NSFileProviderSearchEnumerationObserver](nsfileprovidersearchenumerationobserver.md)
  A protocol that defines a type that receives enumerations of search results from your extension.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:))*