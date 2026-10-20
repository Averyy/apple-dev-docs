# NSFileProviderSearchEnumerator

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines methods for providing search results and canceling searches.

**Availability**:
- macOS 26.0+

## Declaration

```swift
protocol NSFileProviderSearchEnumerator : NSObjectProtocol
```

```objc
@protocol NSFileProviderSearchEnumerator <NSObject>
```

#### Overview

Implement this protocol by implementing the [`enumerateSearchResults(for:startingAt:)`](./nsfileprovidersearchenumerator/enumeratesearchresults%28for,startingat%29.md) method to perform your search and deliver pages of results to the [`NSFileProviderSearchEnumerationObserver`](./nsfileprovidersearchenumerationobserver.md) that you receive as the first parameter.

## Topics

### Providing search results
- [func enumerateSearchResults(for: any NSFileProviderSearchEnumerationObserver, startingAt: NSFileProviderPage?)](./nsfileprovidersearchenumerator/enumeratesearchresults%28for,startingat%29.md)
  Enumerates search results starting from the specified page, in response to a call from the framework.
- [protocol NSFileProviderSearchEnumerationObserver](./nsfileprovidersearchenumerationobserver.md)
  A protocol that defines a type that receives enumerations of search results from your extension.
- [struct NSFileProviderPage](./nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.
### Canceling a search
- [func invalidate()](./nsfileprovidersearchenumerator/invalidate%28%29.md)
  Cancels a currently-running enumeration, in respone to a call from the framework.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Implementing search
- [func searchEnumerator(for: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator](./nsfileprovidersearching/searchenumerator%28for%29.md)
  Provides an object that enumerates over search results, in response to a call from the system.
- [class NSFileProviderStringSearchRequest](./nsfileproviderstringsearchrequest.md)
  A type that contains details of a string-based search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerator)*