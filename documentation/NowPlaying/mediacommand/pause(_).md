# pause(_:)

**Framework**: Now Playing  
**Kind**: method  
**Role**: Type Method

Creates a command that pauses media playback.

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
static func pause(_ action: @escaping () async throws -> Void) -> MediaCommand
```

## Parameters

- `action`: The closure the system calls to pause playback.

## See Also

### Controlling playback
- [static func play(() async throws -> Void) -> MediaCommand](./play%28_%29.md)
  Creates a command that starts media playback.
- [static func stop(() async throws -> Void) -> MediaCommand](./stop%28_%29.md)
  Creates a command that stops media playback.
- [static func togglePlayPause(() async throws -> Void) -> MediaCommand](./toggleplaypause%28_%29.md)
  Creates a command that toggles between play and pause states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/pause(_:))*