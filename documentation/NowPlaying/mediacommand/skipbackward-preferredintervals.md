# skipBackward(preferredIntervals:_:)

**Framework**: Now Playing  
**Kind**: method

Creates a command that skips backward in the media by a specified time interval.

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
static func skipBackward(preferredIntervals: [TimeInterval] = [10], _ action: @escaping (TimeInterval) async throws -> Void) -> MediaCommand
```

## Parameters

- `preferredIntervals`: An array of preferred time intervals, in seconds. Defaults to 10 seconds.
- `action`: The closure the system calls to skip backward. Receives the selected interval.

## See Also

- [static func next(() async throws -> Void) -> MediaCommand](mediacommand/next(_:).md)
  Creates a command that advances to the next track in the playback queue.
- [static func previous(() async throws -> Void) -> MediaCommand](mediacommand/previous(_:).md)
  Creates a command that returns to the previous track in the playback queue.
- [static func skipForward(preferredIntervals: [TimeInterval], (TimeInterval) async throws -> Void) -> MediaCommand](mediacommand/skipforward(preferredintervals:_:).md)
  Creates a command that skips forward in the media by a specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand/skipbackward(preferredintervals:_:))*