# pause(_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that pauses media playback.

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
static func pause(_ action: @escaping () async throws -> Void) -> MediaCommand
```

## Parameters

- `action`: The closure the system calls to pause playback.

## See Also

- [static func play(() async throws -> Void) -> MediaCommand](mediacommand/play(_:).md)
  Creates a command that starts media playback.
- [static func stop(() async throws -> Void) -> MediaCommand](mediacommand/stop(_:).md)
  Creates a command that stops media playback.
- [static func togglePlayPause(() async throws -> Void) -> MediaCommand](mediacommand/toggleplaypause(_:).md)
  Creates a command that toggles between play and pause states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/pause(_:))*