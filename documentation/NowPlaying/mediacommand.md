# MediaCommand

**Framework**: Now Playing  
**Kind**: struct

A command that describes a media control action for a Now Playing session.

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
struct MediaCommand
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use static factory methods to create commands for your session:

```swift
var commands: [MediaCommand] {[
    .play { await self.play() },
    .pause { await self.pause() },
    .next { await self.nextTrack() }.enabled(self.hasNextTrack),
]}
```

## Topics

### Instance Methods
- [func enabled(Bool) -> MediaCommand](mediacommand/enabled(_:).md)
  Sets the enabled state for this command.
### Type Methods
- [static func changePlaybackRate(supported: [Float], (Float) async throws -> Void) -> MediaCommand](mediacommand/changeplaybackrate(supported:_:).md)
  Creates a command that changes the playback rate of the media.
- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](mediacommand/changerepeatmode(current:supported:_:).md)
  Creates a command that changes the repeat mode for media playback.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](mediacommand/changeshufflemode(current:supported:_:).md)
  Creates a command that changes the shuffle mode for media playback.
- [static func feedback(title: String?, shortTitle: String?, status: MediaCommand.FeedbackStatus, (MediaCommand.FeedbackStatus) async throws -> Void) -> MediaCommand](mediacommand/feedback(title:shorttitle:status:_:).md)
  Creates a command that handles user feedback (positive, neutral, or negative) for the current content.
- [static func next(() async throws -> Void) -> MediaCommand](mediacommand/next(_:).md)
  Creates a command that advances to the next track in the playback queue.
- [static func pause(() async throws -> Void) -> MediaCommand](mediacommand/pause(_:).md)
  Creates a command that pauses media playback.
- [static func play(() async throws -> Void) -> MediaCommand](mediacommand/play(_:).md)
  Creates a command that starts media playback.
- [static func previous(() async throws -> Void) -> MediaCommand](mediacommand/previous(_:).md)
  Creates a command that returns to the previous track in the playback queue.
- [static func seekBackward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](mediacommand/seekbackward(beginaction:endaction:).md)
  Creates a command that rewinds through the media.
- [static func seekForward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](mediacommand/seekforward(beginaction:endaction:).md)
  Creates a command that fast-forwards through the media.
- [static func seekToPosition((TimeInterval) async throws -> Void) -> MediaCommand](mediacommand/seektoposition(_:).md)
  Creates a command that seeks to a specific position in the media.
- [static func skipBackward(preferredIntervals: [TimeInterval], (TimeInterval) async throws -> Void) -> MediaCommand](mediacommand/skipbackward(preferredintervals:_:).md)
  Creates a command that skips backward in the media by a specified time interval.
- [static func skipForward(preferredIntervals: [TimeInterval], (TimeInterval) async throws -> Void) -> MediaCommand](mediacommand/skipforward(preferredintervals:_:).md)
  Creates a command that skips forward in the media by a specified time interval.
- [static func stop(() async throws -> Void) -> MediaCommand](mediacommand/stop(_:).md)
  Creates a command that stops media playback.
- [static func togglePlayPause(() async throws -> Void) -> MediaCommand](mediacommand/toggleplaypause(_:).md)
  Creates a command that toggles between play and pause states.
### Enumerations
- [MediaCommand.FeedbackStatus](mediacommand/feedbackstatus.md)
  The feedback status for a media item.
- [MediaCommand.RepeatMode](mediacommand/repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](mediacommand/shufflemode.md)
  The shuffle mode for media playback.

## See Also

- [func enabled(Bool) -> MediaCommand](mediacommand/enabled(_:).md)
  Sets the enabled state for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacommand)*