# commands

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

The commands supported by this session.

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
@MainActor
var commands: [MediaCommand] { get }
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Discussion

Compose commands using [`MediaCommand`](mediacommand.md) static factory methods like [`play(_:)`](mediacommand/play(_:).md), [`pause(_:)`](mediacommand/pause(_:).md), [`next(_:)`](mediacommand/next(_:).md), [`previous(_:)`](mediacommand/previous(_:).md), [`seekToPosition(_:)`](mediacommand/seektoposition(_:).md) and other playback and content commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasessionrepresentable/commands)*