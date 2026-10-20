# MediaCommand.RepeatMode

**Framework**: Now Playing  
**Kind**: enum  
**Role**: Enumeration

The repeat mode for media playback.

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
enum RepeatMode
```

#### Overview

Use this enumeration to specify how the player repeats content during playback.

## Topics

### Enumeration Cases
- [MediaCommand.RepeatMode.all](./repeatmode/all.md)
  The player repeats the current container or playlist indefinitely.
- [MediaCommand.RepeatMode.off](./repeatmode/off.md)
  The player does not repeat content during playback.
- [MediaCommand.RepeatMode.one](./repeatmode/one.md)
  The player repeats a single item indefinitely.

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
- [MediaCommand.ShuffleMode](./shufflemode.md)
  The shuffle mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/repeatmode)*