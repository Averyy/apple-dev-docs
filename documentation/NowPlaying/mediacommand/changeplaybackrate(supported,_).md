# changePlaybackRate(supported:_:)

**Framework**: Now Playing  
**Kind**: method  
**Role**: Type Method

Creates a command that changes the playback rate of the media.

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
static func changePlaybackRate(supported: [Float], _ action: @escaping (Float) async throws -> Void) -> MediaCommand
```

## Parameters

- `supported`: An array of playback rates your app can play at.
- `action`: The closure the system calls to change the playback rate.

## See Also

### Changing playback modes
- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](./changerepeatmode%28current,supported,_%29.md)
  Creates a command that changes the repeat mode for media playback.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](./changeshufflemode%28current,supported,_%29.md)
  Creates a command that changes the shuffle mode for media playback.
- [MediaCommand.RepeatMode](./repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](./shufflemode.md)
  The shuffle mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/changeplaybackrate(supported:_:))*