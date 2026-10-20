# seekToPosition(_:)

**Framework**: Now Playing  
**Kind**: method  
**Role**: Type Method

Creates a command that seeks to a specific position in the media.

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
static func seekToPosition(_ action: @escaping (TimeInterval) async throws -> Void) -> MediaCommand
```

## Parameters

- `action`: The closure the system calls to seek to a position. Receives the target position in seconds.

## See Also

### Seeking
- [static func seekForward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](./seekforward%28beginaction,endaction%29.md)
  Creates a command that fast-forwards through the media.
- [static func seekBackward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](./seekbackward%28beginaction,endaction%29.md)
  Creates a command that rewinds through the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/seektoposition(_:))*