# NSFileProviderSearchEnumerator

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines methods for providing search results and canceling searches.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
protocol NSFileProviderSearchEnumerator : NSObjectProtocol
```

#### Overview

Implement this protocol by implementing the [`enumerateSearchResults(for:startingAt:)`](nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:).md) method to perform your search and deliver pages of results to the [`NSFileProviderSearchEnumerationObserver`](nsfileprovidersearchenumerationobserver.md) that you receive as the first parameter.

## Topics

### Providing search results
- [func enumerateSearchResults(for: any NSFileProviderSearchEnumerationObserver, startingAt: NSFileProviderPage?)](nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:).md)
  Enumerates search results starting from the specified page, in response to a call from the framework.
- [protocol NSFileProviderSearchEnumerationObserver](nsfileprovidersearchenumerationobserver.md)
  A protocol that defines a type that receives enumerations of search results from your extension.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.
### Canceling a search
- [func invalidate()](nsfileprovidersearchenumerator/invalidate.md)
  Cancels a currently-running enumeration, in respone to a call from the framework.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func searchEnumerator(for: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator](nsfileprovidersearching/searchenumerator(for:).md)
  Provides an object that enumerates over search results, in response to a call from the system.
- [class NSFileProviderStringSearchRequest](nsfileproviderstringsearchrequest.md)
  A type that contains details of a string-based search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerator)*