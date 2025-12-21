# NSFileProviderSearchEnumerationObserver

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines a type that receives enumerations of search results from your extension.

**Availability**:
- macOS 26.0+

## Declaration

```swift
protocol NSFileProviderSearchEnumerationObserver : NSObjectProtocol
```

## Topics

### Providing search results
- [func didEnumerate([any NSFileProviderSearchResult])](nsfileprovidersearchenumerationobserver/didenumerate(_:).md)
  Delivers an array of search results to the observer.
- [protocol NSFileProviderSearchResult](nsfileprovidersearchresult.md)
  A protocol that defines properties of a search result.
### Ending enumeration
- [func finishEnumerating(upTo: NSFileProviderPage?)](nsfileprovidersearchenumerationobserver/finishenumerating(upto:).md)
  Finish enumerating a page of results, and optionally provide a location within the results to continue the enumeration.
- [func finishEnumeratingWithError(any Error)](nsfileprovidersearchenumerationobserver/finishenumeratingwitherror(_:).md)
  Finishes a search enumeration by sending an error to the framework.
### Instance Properties
- [var maximumNumberOfResultsPerPage: Int](nsfileprovidersearchenumerationobserver/maximumnumberofresultsperpage.md)
  The maximum number of results to return in a single page enumeration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func enumerateSearchResults(for: any NSFileProviderSearchEnumerationObserver, startingAt: NSFileProviderPage?)](nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:).md)
  Enumerates search results starting from the specified page, in response to a call from the framework.
- [struct NSFileProviderPage](nsfileproviderpage.md)
  A synchronization point that represents the next batch of items to be returned by an enumerator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver)*