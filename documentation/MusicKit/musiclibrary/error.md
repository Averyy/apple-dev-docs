# MusicLibrary.Error

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

An error that the music library can throw upon accessing, manipulating, or requesting data from the user’s music library.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [MusicLibrary.Error.addToPlaylistFailed](./error/addtoplaylistfailed.md)
  An error that indicates a failure in the process of adding an item to a playlist.
- [MusicLibrary.Error.createPlaylistFailed](./error/createplaylistfailed.md)
  An error that indicates a failure in the process of creating a playlist.
- [MusicLibrary.Error.editPlaylistFailed](./error/editplaylistfailed.md)
  An error that indicates a failure in the process of editing a playlist.
- [MusicLibrary.Error.itemAlreadyAdded](./error/itemalreadyadded.md)
  An error indicating that the item attempting to be added to the user’s music library is already in the library.
- [MusicLibrary.Error.permissionDenied](./error/permissiondenied.md)
  An error that occurs when the user doesn’t consent for the current app to access their Apple Music library.
- [MusicLibrary.Error.playlistNotInLibrary](./error/playlistnotinlibrary.md)
  An error indicating that the playlist attempting to be added to is not in the user’s library.
- [MusicLibrary.Error.unableToAddItem](./error/unabletoadditem.md)
  An error indicating that the item attempting to be added to the user’s music library cannot be added.
- [MusicLibrary.Error.unknown](./error/unknown.md)
  An error indicating the ocurrence of an unknown or unexpected error.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/error)*