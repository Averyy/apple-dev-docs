# NSFileProviderSearching

**Framework**: File Provider  
**Kind**: protocol

A protocol you implement to support searching in your file provider.

**Availability**:
- macOS 26.0+

## Declaration

```swift
protocol NSFileProviderSearching : NSObjectProtocol
```

#### Overview

Implement this protocol in your provider’s principal class to support searching files in cloud storage. To make search available to the person using the device, also set the property [`supportsStringSearchRequest`](nsfileproviderdomain/supportsstringsearchrequest.md) to `true`.

> 💡 **Tip**: You don’t need to implement this protocol if you only want to expose the contents of the working set to system search.

When the person using the device performs a search, the system calls the `NSFileProviderSearching` implementation for all the accounts they’ve chosen to search. Your implementation returns a [`NSFileProviderSearchEnumerator`](nsfileprovidersearchenumerator.md), which receives repeated callbacks to [`enumerateSearchResults(for:startingAt:)`](nsfileprovidersearchenumerator/enumeratesearchresults(for:startingat:).md) until one of the following occurs:

- The system has received enough results.
- The system has received all results.
- The person enters another character into the query string, thereby canceling this search and starting another.
- The person explicitly cancels the search.

## Topics

### Implementing search
- [func searchEnumerator(for: NSFileProviderStringSearchRequest) -> any NSFileProviderSearchEnumerator](nsfileprovidersearching/searchenumerator(for:).md)
  Provides an object that enumerates over search results, in response to a call from the system.
- [class NSFileProviderStringSearchRequest](nsfileproviderstringsearchrequest.md)
  A type that contains details of a string-based search request.
- [protocol NSFileProviderSearchEnumerator](nsfileprovidersearchenumerator.md)
  A protocol that defines methods for providing search results and canceling searches.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearching)*