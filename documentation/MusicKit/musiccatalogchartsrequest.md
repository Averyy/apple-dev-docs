# MusicCatalogChartsRequest

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

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
- [init(genre: Genre?, kinds: [MusicCatalogChartKind], types: [any MusicCatalogChartRequestable.Type])](./musiccatalogchartsrequest/init%28genre,kinds,types%29.md)
  Creates a catalog charts request for a specified genre and list of types to include in the catalog charts response.
### Instance Properties
- [var genre: Genre?](./musiccatalogchartsrequest/genre.md)
  The genre for the request.
- [var kinds: [MusicCatalogChartKind]](./musiccatalogchartsrequest/kinds.md)
  The kinds of requested catalog charts.
- [var limit: Int?](./musiccatalogchartsrequest/limit.md)
  A limit for the number of items to return in the catalog search response.
- [var offset: Int?](./musiccatalogchartsrequest/offset.md)
  An offset for the request.
- [var types: [any MusicCatalogChartRequestable.Type]](./musiccatalogchartsrequest/types.md)
  The list of requested types for the catalog charts response.
### Instance Methods
- [func response() async throws -> MusicCatalogChartsResponse](./musiccatalogchartsrequest/response%28%29.md)
  Fetches the most popular items of the requested types that match the genre and kinds for the request.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest)*