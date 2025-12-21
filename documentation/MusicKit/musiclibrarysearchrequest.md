# MusicLibrarySearchRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch items from user’s library using a search term.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MusicLibrarySearchRequest
```

## Topics

### Initializers
- [init(term: String, types: [any MusicLibrarySearchable.Type])](musiclibrarysearchrequest/init(term:types:).md)
  Creates a library search request for a specified search term and list of library searchable types.
### Instance Properties
- [var includeTopResults: Bool](musiclibrarysearchrequest/includetopresults.md)
  A Boolean value that indicates whether to request top search results.
- [var limit: Int](musiclibrarysearchrequest/limit.md)
  A limit for the number of items to return in the library search response.
- [let term: String](musiclibrarysearchrequest/term.md)
  The search term for the request.
- [var types: [any MusicLibrarySearchable.Type]](musiclibrarysearchrequest/types.md)
  The list of requested library searchable types.
### Instance Methods
- [func response() async throws -> MusicLibrarySearchResponse](musiclibrarysearchrequest/response.md)
  Fetches items of the requested library searchable types that match the search term of the request.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest)*