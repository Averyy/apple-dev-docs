# commands

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

The commands supported by this session.

**Availability**:
- iOS 27.0+
- iOS App Extension 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
var commands: [MediaCommand] { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Compose commands using [`MediaCommand`](mediacommand.md) static factory methods like [`play(_:)`](mediacommand/play(_:).md), [`pause(_:)`](mediacommand/pause(_:).md), [`next(_:)`](mediacommand/next(_:).md), [`previous(_:)`](mediacommand/previous(_:).md), [`seekToPosition(_:)`](mediacommand/seektoposition(_:).md) and other playback and content commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable/commands)*