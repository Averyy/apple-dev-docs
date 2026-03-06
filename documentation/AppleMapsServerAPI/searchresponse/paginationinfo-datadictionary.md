# SearchResponse.PaginationInfo

**Framework**: Apple Maps Server API  
**Kind**: dictionary

An object that returns a page of search responses.

**Availability**:
- Apple Maps Server API 1.2+

## Declaration

```swift
object SearchResponse.PaginationInfo
```

## Properties

- `nextPageToken` (string): An opaque string that the server uses to fetch the next page of search responses.
- `prevPageToken` (string): An opaque string that the server uses to fetch the previous page of search responses.
- `totalPageCount` (number): The total number of pages for the request.
- `totalResults` (number): The total number of results for the request.

## See Also

- [object SearchResponse.Place](searchresponse/place.md)
  A structure returned by a search that describes a place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/searchresponse/paginationinfo-data.dictionary)*