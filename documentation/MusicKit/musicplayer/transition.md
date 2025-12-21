# MusicPlayer.Transition

**Framework**: MusicKit  
**Kind**: enum

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
- [MusicPlayer.Transition.CrossfadeOptions](musicplayer/transition/crossfadeoptions.md)
  The options for the crossfade transition.
### Enumeration Cases
- [case crossfade(options: MusicPlayer.Transition.CrossfadeOptions)](musicplayer/transition/crossfade(options:).md)
  A smooth overlap between the currently playing item and the next item.
- [MusicPlayer.Transition.none](musicplayer/transition/none.md)
  No transition.
### Type Properties
- [static let crossfade: MusicPlayer.Transition](musicplayer/transition/crossfade.md)
  A smooth overlap between the currently playing item and the next item with default options.
### Type Methods
- [static func crossfade(duration: TimeInterval?) -> MusicPlayer.Transition](musicplayer/transition/crossfade(duration:).md)
  A smooth overlap between the currently playing item and the next item with a specified duration.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/transition)*