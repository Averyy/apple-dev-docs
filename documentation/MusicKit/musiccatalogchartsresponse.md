# MusicCatalogChartsResponse

**Framework**: MusicKit  
**Kind**: struct

An object that contains results for a catalog charts request.

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
struct MusicCatalogChartsResponse
```

## Topics

### Operators
- [static func == (MusicCatalogChartsResponse, MusicCatalogChartsResponse) -> Bool](musiccatalogchartsresponse/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let albumCharts: [MusicCatalogChart<Album>]](musiccatalogchartsresponse/albumcharts.md)
  A collection of charts that contain albums.
- [var hashValue: Int](musiccatalogchartsresponse/hashvalue.md)
  The hash value.
- [let musicVideoCharts: [MusicCatalogChart<MusicVideo>]](musiccatalogchartsresponse/musicvideocharts.md)
  A collection of charts that contain music videos.
- [let playlistCharts: [MusicCatalogChart<Playlist>]](musiccatalogchartsresponse/playlistcharts.md)
  A collection of charts that contain playlists.
- [let songCharts: [MusicCatalogChart<Song>]](musiccatalogchartsresponse/songcharts.md)
  A collection of charts that contain songs.
### Instance Methods
- [func hash(into: inout Hasher)](musiccatalogchartsresponse/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiccatalogchartsresponse/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiccatalogchartsresponse/customstringconvertible-implementations.md)
- [Decodable Implementations](musiccatalogchartsresponse/decodable-implementations.md)
- [Encodable Implementations](musiccatalogchartsresponse/encodable-implementations.md)
- [Equatable Implementations](musiccatalogchartsresponse/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchartsresponse)*