# add(_:to:)

**Framework**: MusicKit  
**Kind**: method

Adds an item to the end of an existing playlist.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func add<MusicItemType>(_ item: MusicItemType, to playlist: Playlist) async throws -> Playlist where MusicItemType : MusicPlaylistAddable
```

#### Return Value

The updated playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/add(_:to:))*