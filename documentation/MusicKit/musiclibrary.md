# MusicLibrary

**Framework**: MusicKit  
**Kind**: class

An object your app uses to access the user’s music library.

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
class MusicLibrary
```

## Topics

### Instance Methods
- [func add<MusicItemType>(MusicItemType) async throws](musiclibrary/add(_:).md)
  Adds an item to the user’s music library.
- [func add<MusicItemType>(MusicItemType, to: Playlist) async throws -> Playlist](musiclibrary/add(_:to:).md)
  Adds an item to the end of an existing playlist.
- [func createPlaylist(name: String, description: String?, authorDisplayName: String?) async throws -> Playlist](musiclibrary/createplaylist(name:description:authordisplayname:).md)
  Creates a playlist in the user’s music library.
- [func createPlaylist<S, MusicPlaylistAddableType>(name: String, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist](musiclibrary/createplaylist(name:description:authordisplayname:items:).md)
  Creates a playlist in the user’s music library.
- [func edit(Playlist, name: String?, description: String?, authorDisplayName: String?) async throws -> Playlist](musiclibrary/edit(_:name:description:authordisplayname:).md)
  Edits a playlist that your app has created.
- [func edit<S, MusicPlaylistAddableType>(Playlist, name: String?, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist](musiclibrary/edit(_:name:description:authordisplayname:items:).md)
  Edits a playlist that your app has created including items to rebuild the list of entries.
### Type Properties
- [static let shared: MusicLibrary](musiclibrary/shared.md)
  A shared object that allows your app to modify the user’s music library.
### Enumerations
- [MusicLibrary.Error](musiclibrary/error.md)
  An error that the music library can throw upon accessing, manipulating, or requesting data from the user’s music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary)*