# changePlaybackRate(supported:_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that changes the playback rate of the media.

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
static func changePlaybackRate(supported: [Float], _ action: @escaping (Float) async throws -> Void) -> MediaCommand
```

## Parameters

- `supported`: An array of playback rates your app can play at.
- `action`: The closure the system calls to change the playback rate.

## See Also

- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](mediacommand/changerepeatmode(current:supported:_:).md)
  Creates a command that changes the repeat mode for media playback.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](mediacommand/changeshufflemode(current:supported:_:).md)
  Creates a command that changes the shuffle mode for media playback.
- [MediaCommand.RepeatMode](mediacommand/repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](mediacommand/shufflemode.md)
  The shuffle mode for media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/changeplaybackrate(supported:_:))*