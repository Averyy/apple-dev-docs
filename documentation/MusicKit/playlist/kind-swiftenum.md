# Playlist.Kind

**Framework**: MusicKit  
**Kind**: enum

The available kinds of playlists.

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
enum Kind
```

## Topics

### Operators
- [static func == (Playlist.Kind, Playlist.Kind) -> Bool](playlist/kind-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Playlist.Kind.editorial](playlist/kind-swift.enum/editorial.md)
  Indicates that the playlist was created by an Apple Music curator.
- [Playlist.Kind.external](playlist/kind-swift.enum/external.md)
  Indicates that the playlist was created by an external curator.
- [Playlist.Kind.personalMix](playlist/kind-swift.enum/personalmix.md)
  Indicates that the playlist is a personalized playlist for an Apple Music user.
- [Playlist.Kind.replay](playlist/kind-swift.enum/replay.md)
  Indicates that the playlist is a personalized Replay playlist for an Apple Music user.
- [Playlist.Kind.userShared](playlist/kind-swift.enum/usershared.md)
  Indicates that the playlist was created and shared by an Apple Music user.
### Initializers
- [init(from: any Decoder) throws](playlist/kind-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](playlist/kind-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](playlist/kind-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](playlist/kind-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](playlist/kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playlist/kind-swift.enum)*