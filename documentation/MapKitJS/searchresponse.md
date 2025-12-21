# SearchResponse

**Framework**: MapKit JS  
**Kind**: struct

The result of a search, including the original search query, the bounding region, and a list of places that match the query.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface SearchResponse
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

The search callback function provides the search response in its data parameter. An object parsed from server-returned JSON, `data` contains a [`query`](searchresponse/query.md) and a [`boundingRegion`](searchresponse/boundingregion.md).

## Topics

### Search response
- [places](searchresponse/places.md)
  A list of places that match the search query.
- [query](searchresponse/query.md)
  The query string for performing the search.
- [boundingRegion](searchresponse/boundingregion.md)
  The region that encloses the places from the search results.

## See Also

- [search(query, callback, options)](search/search.md)
  Retrieves the results of a search query.
- [type SearchDelegate](searchdelegate.md)
  An object or callback function the framework calls when performing a search or an autocomplete request.
- [interface SearchOptions](searchoptions.md)
  An object that contains options to adjust a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchresponse)*