# MusicPlayer.Transition

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

The transition applied between playing items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Transition
```

## Topics

### Structures
- [MusicPlayer.Transition.CrossfadeOptions](./transition/crossfadeoptions.md)
  The options for the crossfade transition.
### Enumeration Cases
- [case crossfade(options: MusicPlayer.Transition.CrossfadeOptions)](./transition/crossfade%28options%29.md)
  A smooth overlap between the currently playing item and the next item.
- [MusicPlayer.Transition.none](./transition/none.md)
  No transition.
### Type Properties
- [static let crossfade: MusicPlayer.Transition](./transition/crossfade.md)
  A smooth overlap between the currently playing item and the next item with default options.
### Type Methods
- [static func crossfade(duration: TimeInterval?) -> MusicPlayer.Transition](./transition/crossfade%28duration%29.md)
  A smooth overlap between the currently playing item and the next item with a specified duration.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/transition)*