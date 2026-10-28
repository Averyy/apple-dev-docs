# MediaCommand.ShuffleMode

**Framework**: Now Playing  
**Kind**: enum  
**Role**: Enumeration

The shuffle mode for media playback.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum ShuffleMode
```

## Overview

Use this enumeration to specify how the player shuffles content during playback.

## Topics

### Enumeration Cases
- [MediaCommand.ShuffleMode.collections](./shufflemode/collections.md)
  The player shuffles collections during playback (for example, albums).
- [MediaCommand.ShuffleMode.items](./shufflemode/items.md)
  The player shuffles individual items during playback (for example, songs).
- [MediaCommand.ShuffleMode.off](./shufflemode/off.md)
  The player does not shuffle content during playback.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Changing playback modes
- [static func changePlaybackRate(supported: [Float], (Float) async throws -> Void) -> MediaCommand](./changeplaybackrate%28supported,_%29.md)
  Creates a command that changes the playback rate of the media.
- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](./changerepeatmode%28current,supported,_%29.md)
  Creates a command that changes the repeat mode for media playback.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](./changeshufflemode%28current,supported,_%29.md)
  Creates a command that changes the shuffle mode for media playback.
- [MediaCommand.RepeatMode](./repeatmode.md)
  The repeat mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/shufflemode)*