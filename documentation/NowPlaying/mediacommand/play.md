# play(_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that starts media playback.

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
static func play(_ action: @escaping () async throws -> Void) -> MediaCommand
```

## Parameters

- `action`: The closure the system calls to start playback.

## See Also

- [static func pause(() async throws -> Void) -> MediaCommand](mediacommand/pause(_:).md)
  Creates a command that pauses media playback.
- [static func stop(() async throws -> Void) -> MediaCommand](mediacommand/stop(_:).md)
  Creates a command that stops media playback.
- [static func togglePlayPause(() async throws -> Void) -> MediaCommand](mediacommand/toggleplaypause(_:).md)
  Creates a command that toggles between play and pause states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/play(_:))*