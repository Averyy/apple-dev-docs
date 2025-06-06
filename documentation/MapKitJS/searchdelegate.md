# SearchDelegate

**Framework**: MapKit JS  
**Kind**: class

An object or callback function the framework calls when performing a search or an autocomplete request.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface SearchDelegate
```

#### Overview

You can also pass an object to the [`search`](mapkit.search/search.md) and [`autocomplete`](mapkit.search/autocomplete.md) methods instead of a search delegate callback function. A delegate object can include the following methods:

- [`searchDidComplete`](searchdelegate/searchdidcomplete.md). Upon successful completion of a search request, this method returns a data object that’s the same as the one that passes to the search callback function.
- [`searchDidError`](searchdelegate/searchdiderror.md). The system calls this when the search request fails.
- [`autocompleteDidComplete`](searchdelegate/autocompletedidcomplete.md). When an autocomplete request successfully completes, this method returns a `data` array that’s the same as the one that passes to the autocomplete callback function.
- [`autocompleteDidError`](searchdelegate/autocompletediderror.md). The system invokes this when an autocomplete request fails.

## Topics

### Responding to state changes and errors
- [autocompleteDidComplete](searchdelegate/autocompletedidcomplete.md)
  Tells the delegate when the autocomplete request completes.
- [autocompleteDidError](searchdelegate/autocompletediderror.md)
  Tells the delegate when the autocomplete request fails due to an error.
- [searchDidComplete](searchdelegate/searchdidcomplete.md)
  Tells the delegate when the search completes.
- [searchDidError](searchdelegate/searchdiderror.md)
  Tells the delegate when the search fails due to an error.

## See Also

- [search](mapkit.search/search.md)
  Retrieves the results of a search query.
- [SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.
- [SearchResponse](searchresponse.md)
  The result of a search, including the original search query, the bounding region, and a list of places that match the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchdelegate)*