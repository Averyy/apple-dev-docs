# PlayParameters

**Framework**: MusicKit  
**Kind**: struct

An opaque object that represents parameters to initiate playback of a playable music item using a music player.

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
struct PlayParameters
```

## Topics

### Operators
- [static func == (PlayParameters, PlayParameters) -> Bool](playparameters/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](playparameters/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](playparameters/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Decodable Implementations](playparameters/decodable-implementations.md)
- [Encodable Implementations](playparameters/encodable-implementations.md)
- [Equatable Implementations](playparameters/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ApplicationMusicPlayer](applicationmusicplayer.md)
  An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [class SystemMusicPlayer](systemmusicplayer.md)
  An object your app uses to play music by controlling the Music app’s state.
- [class MusicPlayer](musicplayer.md)
  An object your app uses to play music.
- [protocol PlayableMusicItem](playablemusicitem.md)
  A set of properties that a music player uses to initiate playback for a music item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/playparameters)*