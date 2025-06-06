# MusicLibrary.Error

**Framework**: MusicKit  
**Kind**: enum

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
- [MusicLibrary.Error.addToPlaylistFailed](musiclibrary/error/addtoplaylistfailed.md)
  An error that indicates a failure in the process of adding an item to a playlist.
- [MusicLibrary.Error.createPlaylistFailed](musiclibrary/error/createplaylistfailed.md)
  An error that indicates a failure in the process of creating a playlist.
- [MusicLibrary.Error.editPlaylistFailed](musiclibrary/error/editplaylistfailed.md)
  An error that indicates a failure in the process of editing a playlist.
- [MusicLibrary.Error.itemAlreadyAdded](musiclibrary/error/itemalreadyadded.md)
  An error indicating that the item attempting to be added to the user’s music library is already in the library.
- [MusicLibrary.Error.permissionDenied](musiclibrary/error/permissiondenied.md)
  An error that occurs when the user doesn’t consent for the current app to access their Apple Music library.
- [MusicLibrary.Error.playlistNotInLibrary](musiclibrary/error/playlistnotinlibrary.md)
  An error indicating that the playlist attempting to be added to is not in the user’s library.
- [MusicLibrary.Error.unableToAddItem](musiclibrary/error/unabletoadditem.md)
  An error indicating that the item attempting to be added to the user’s music library cannot be added.
- [MusicLibrary.Error.unknown](musiclibrary/error/unknown.md)
  An error indicating the ocurrence of an unknown or unexpected error.
### Initializers
- [init?(rawValue: String)](musiclibrary/error/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var description: String](musiclibrary/error/description.md)
  A textual representation of this instance.
- [var errorDescription: String?](musiclibrary/error/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](musiclibrary/error/failurereason.md)
  A localized message describing the reason for the failure.
- [var helpAnchor: String?](musiclibrary/error/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var rawValue: String](musiclibrary/error/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [var recoverySuggestion: String?](musiclibrary/error/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
### Type Aliases
- [MusicLibrary.Error.RawValue](musiclibrary/error/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](musiclibrary/error/equatable-implementations.md)
- [Error Implementations](musiclibrary/error/error-implementations.md)
- [RawRepresentable Implementations](musiclibrary/error/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/error)*