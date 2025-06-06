# MusicCatalogSearchRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items from the Apple Music catalog using a search term.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct MusicCatalogSearchRequest
```

## Topics

### Initializers
- [init(term: String, types: [any MusicCatalogSearchable.Type])](musiccatalogsearchrequest/init(term:types:).md)
  Creates a catalog search request for a specified search term and list of catalog searchable types.
### Instance Properties
- [var includeTopResults: Bool](musiccatalogsearchrequest/includetopresults.md)
  A Boolean value that indicates whether to request top search results.
- [var limit: Int?](musiccatalogsearchrequest/limit.md)
  A limit for the number of items to return in the catalog search response.
- [var offset: Int?](musiccatalogsearchrequest/offset.md)
  An offet for the request.
- [let term: String](musiccatalogsearchrequest/term.md)
  The search term for the request.
- [var types: [any MusicCatalogSearchable.Type]](musiccatalogsearchrequest/types.md)
  The list of requested catalog searchable types.
### Instance Methods
- [func response() async throws -> MusicCatalogSearchResponse](musiccatalogsearchrequest/response.md)
  Fetches items of the requested catalog searchable types that match the search term of the request.

## See Also

- [struct MusicCatalogSearchResponse](musiccatalogsearchresponse.md)
  An object that contains results for a catalog search request.
- [protocol MusicCatalogSearchable](musiccatalogsearchable.md)
  A protocol for music items that your app can fetch by using a catalog search request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchrequest)*