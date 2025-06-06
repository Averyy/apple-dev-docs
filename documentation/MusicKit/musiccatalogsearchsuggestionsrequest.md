# MusicCatalogSearchSuggestionsRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MusicCatalogSearchSuggestionsRequest
```

## Topics

### Initializers
- [init(term: String, includingTopResultsOfTypes: [any MusicCatalogSearchable.Type])](musiccatalogsearchsuggestionsrequest/init(term:includingtopresultsoftypes:).md)
  Creates a catalog search suggestions request for a specified search term along with a list of types to include when fetching top results.
### Instance Properties
- [var limit: Int?](musiccatalogsearchsuggestionsrequest/limit.md)
  A limit for the number of items to return in the catalog search suggestions response.
- [let term: String](musiccatalogsearchsuggestionsrequest/term.md)
  The search term for the request.
- [var typesForTopResults: [any MusicCatalogSearchable.Type]](musiccatalogsearchsuggestionsrequest/typesfortopresults.md)
  The list of requested types for top results.
### Instance Methods
- [func response() async throws -> MusicCatalogSearchSuggestionsResponse](musiccatalogsearchsuggestionsrequest/response.md)
  Fetches suggestions of the requested catalog searchable types that match the search term of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsrequest)*