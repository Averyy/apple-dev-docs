# commands

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

The commands supported by this session.

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
@MainActor
var commands: [MediaCommand] { get }
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Discussion

Compose commands using [`MediaCommand`](mediacommand.md) static factory methods like [`play(_:)`](mediacommand/play(_:).md), [`pause(_:)`](mediacommand/pause(_:).md), [`next(_:)`](mediacommand/next(_:).md), [`previous(_:)`](mediacommand/previous(_:).md), [`seekToPosition(_:)`](mediacommand/seektoposition(_:).md) and other playback and content commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasessionrepresentable/commands)*