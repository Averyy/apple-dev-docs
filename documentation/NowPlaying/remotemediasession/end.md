# end()

**Framework**: Now Playing  
**Kind**: method

Ends the session and removes it from the Now Playing interface.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
func end() async throws
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

> **Note**: [`RemoteMediaSessionError.internalFailure`](remotemediasessionerror/internalfailure.md) if the session couldn’t be removed from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/end())*