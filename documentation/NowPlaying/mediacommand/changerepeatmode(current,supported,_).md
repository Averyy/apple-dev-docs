# changeRepeatMode(current:supported:_:)

**Framework**: Now Playing  
**Kind**: method  
**Role**: Type Method

Creates a command that changes the repeat mode for media playback.

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
static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]? = nil, _ action: @escaping (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand
```

## Parameters

- `current`: The current repeat mode.
- `supported`: The supported repeat modes. Pass `nil` to support all modes.
- `action`: The closure the system calls to change the repeat mode.

## See Also

### Changing playback modes
- [static func changePlaybackRate(supported: [Float], (Float) async throws -> Void) -> MediaCommand](./changeplaybackrate%28supported,_%29.md)
  Creates a command that changes the playback rate of the media.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](./changeshufflemode%28current,supported,_%29.md)
  Creates a command that changes the shuffle mode for media playback.
- [MediaCommand.RepeatMode](./repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](./shufflemode.md)
  The shuffle mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/changerepeatmode(current:supported:_:))*