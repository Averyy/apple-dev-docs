# PaginatedResourceCollectionResponse

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A response object composed of paginated resource objects for the request.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object PaginatedResourceCollectionResponse
```

## Properties

- `next` (string): A relative cursor to fetch the next paginated collection of resources for the request if more exist.
- `data` ([Resource]) *(required)*: A paginated collection of resources for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/paginatedresourcecollectionresponse)*