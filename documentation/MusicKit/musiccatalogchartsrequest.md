# MusicCatalogChartsRequest

**Framework**: MusicKit  
**Kind**: struct

A request that your app uses to fetch the most popular items in the Apple Music catalog.

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
struct MusicCatalogChartsRequest
```

## Topics

### Initializers
- [init(genre: Genre?, kinds: [MusicCatalogChartKind], types: [any MusicCatalogChartRequestable.Type])](musiccatalogchartsrequest/init(genre:kinds:types:).md)
  Creates a catalog charts request for a specified genre and list of types to include in the catalog charts response.
### Instance Properties
- [var genre: Genre?](musiccatalogchartsrequest/genre.md)
  The genre for the request.
- [var kinds: [MusicCatalogChartKind]](musiccatalogchartsrequest/kinds.md)
  The kinds of requested catalog charts.
- [var limit: Int?](musiccatalogchartsrequest/limit.md)
  A limit for the number of items to return in the catalog search response.
- [var offset: Int?](musiccatalogchartsrequest/offset.md)
  An offet for the request.
- [var types: [any MusicCatalogChartRequestable.Type]](musiccatalogchartsrequest/types.md)
  The list of requested types for the catalog charts response.
### Instance Methods
- [func response() async throws -> MusicCatalogChartsResponse](musiccatalogchartsrequest/response.md)
  Fetches the most popular items of the requested types that match the genre and kinds for the request.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest)*