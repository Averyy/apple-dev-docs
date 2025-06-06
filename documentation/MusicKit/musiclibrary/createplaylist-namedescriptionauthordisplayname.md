# createPlaylist(name:description:authorDisplayName:)

**Framework**: MusicKit  
**Kind**: method

Creates a playlist in the user’s music library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func createPlaylist(name: String, description: String? = nil, authorDisplayName: String? = nil) async throws -> Playlist
```

#### Return Value

The newly created playlist.

## Parameters

- `name`: The name of the playlist.
- `description`: An optional description of the playlist.
- `authorDisplayName`: The display name of the author for the playlist.   A   value will result in the framework using   your app’s name instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:))*