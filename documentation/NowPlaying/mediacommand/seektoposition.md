# seekToPosition(_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that seeks to a specific position in the media.

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
static func seekToPosition(_ action: @escaping (TimeInterval) async throws -> Void) -> MediaCommand
```

## Parameters

- `action`: The closure the system calls to seek to a position. Receives the target position in seconds.

## See Also

- [static func seekForward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](mediacommand/seekforward(beginaction:endaction:).md)
  Creates a command that fast-forwards through the media.
- [static func seekBackward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](mediacommand/seekbackward(beginaction:endaction:).md)
  Creates a command that rewinds through the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/seektoposition(_:))*