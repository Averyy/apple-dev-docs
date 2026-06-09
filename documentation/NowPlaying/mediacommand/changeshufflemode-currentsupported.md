# changeShuffleMode(current:supported:_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that changes the shuffle mode for media playback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]? = nil, _ action: @escaping (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand
```

## Parameters

- `current`: The current shuffle mode.
- `supported`: The supported shuffle modes. Pass `nil` to support all modes.
- `action`: The closure the system calls to change the shuffle mode.

## See Also

- [static func changePlaybackRate(supported: [Float], (Float) async throws -> Void) -> MediaCommand](mediacommand/changeplaybackrate(supported:_:).md)
  Creates a command that changes the playback rate of the media.
- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](mediacommand/changerepeatmode(current:supported:_:).md)
  Creates a command that changes the repeat mode for media playback.
- [MediaCommand.RepeatMode](mediacommand/repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](mediacommand/shufflemode.md)
  The shuffle mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/changeshufflemode(current:supported:_:))*