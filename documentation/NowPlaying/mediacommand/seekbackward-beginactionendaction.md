# seekBackward(beginAction:endAction:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that rewinds through the media.

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
static func seekBackward(beginAction: @escaping () async throws -> Void, endAction: @escaping () async throws -> Void) -> MediaCommand
```

#### Discussion

The system calls `beginAction` when the user starts rewinding (for example, by pressing and holding a rewind button), and calls `endAction` when the user stops. Use these paired actions to start and stop any rate change or scrubbing behavior.

## Parameters

- `beginAction`: The closure the system calls to begin rewinding.
- `endAction`: The closure the system calls to end rewinding.

## See Also

- [static func seekToPosition((TimeInterval) async throws -> Void) -> MediaCommand](mediacommand/seektoposition(_:).md)
  Creates a command that seeks to a specific position in the media.
- [static func seekForward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](mediacommand/seekforward(beginaction:endaction:).md)
  Creates a command that fast-forwards through the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/seekbackward(beginaction:endaction:))*