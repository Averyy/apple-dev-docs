# commands

**Framework**: Now Playing  
**Kind**: property  
**Role**: Instance Property  
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

- [Publishing remote media sessions](../publishing-remote-media-sessions.md)

## Discussion

Compose commands using [`MediaCommand`](../mediacommand.md) static factory methods like [`play(_:)`](../mediacommand/play%28_%29.md), [`pause(_:)`](../mediacommand/pause%28_%29.md), [`next(_:)`](../mediacommand/next%28_%29.md), [`previous(_:)`](../mediacommand/previous%28_%29.md), [`seekToPosition(_:)`](../mediacommand/seektoposition%28_%29.md) and other playback and content commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable/commands)*