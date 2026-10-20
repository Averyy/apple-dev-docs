# Playback commands

**Framework**: Now Playing  
**Role**: API Collection

Declare the playback controls your app supports.

#### Overview

Use [`MediaCommand`](./mediacommand.md) to define the controls available for your Now Playing session. The system displays these controls on the Lock Screen, Control Center, and connected accessories. Each command takes an action closure that the system invokes when someone interacts with a control.

Return an array of commands from your [`commands`](./mediasessionrepresentable/commands.md) property. Create each command with a static factory method on [`MediaCommand`](./mediacommand.md):

```swift
var commands: [MediaCommand] {
    [
        .play { self.play() },
        .pause { self.pause() },
        .next { self.next() }.enabled(hasNextTrack),
        .previous { self.previous() }.enabled(hasPreviousTrack),
        .seekToPosition { time in
            self.seek(to: time)
        },
    ]
}
```

Use [`enabled(_:)`](./mediacommand/enabled%28_%29.md) to make a command available or unavailable based on your app’s state. Unavailable commands still appear in the interface, but the system doesn’t invoke their handler.

## Topics

### Creating commands
- [struct MediaCommand](./mediacommand.md)
  A command that describes a media control action for a Now Playing session.
- [func enabled(Bool) -> MediaCommand](./mediacommand/enabled%28_%29.md)
  Sets the enabled state for this command.
### Controlling playback
- [static func play(() async throws -> Void) -> MediaCommand](./mediacommand/play%28_%29.md)
  Creates a command that starts media playback.
- [static func pause(() async throws -> Void) -> MediaCommand](./mediacommand/pause%28_%29.md)
  Creates a command that pauses media playback.
- [static func stop(() async throws -> Void) -> MediaCommand](./mediacommand/stop%28_%29.md)
  Creates a command that stops media playback.
- [static func togglePlayPause(() async throws -> Void) -> MediaCommand](./mediacommand/toggleplaypause%28_%29.md)
  Creates a command that toggles between play and pause states.
### Navigating commands
- [static func next(() async throws -> Void) -> MediaCommand](./mediacommand/next%28_%29.md)
  Creates a command that advances to the next track in the playback queue.
- [static func previous(() async throws -> Void) -> MediaCommand](./mediacommand/previous%28_%29.md)
  Creates a command that returns to the previous track in the playback queue.
- [static func skipForward(preferredIntervals: [TimeInterval], (TimeInterval) async throws -> Void) -> MediaCommand](./mediacommand/skipforward%28preferredintervals,_%29.md)
  Creates a command that skips forward in the media by a specified time interval.
- [static func skipBackward(preferredIntervals: [TimeInterval], (TimeInterval) async throws -> Void) -> MediaCommand](./mediacommand/skipbackward%28preferredintervals,_%29.md)
  Creates a command that skips backward in the media by a specified time interval.
### Seeking
- [static func seekToPosition((TimeInterval) async throws -> Void) -> MediaCommand](./mediacommand/seektoposition%28_%29.md)
  Creates a command that seeks to a specific position in the media.
- [static func seekForward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](./mediacommand/seekforward%28beginaction,endaction%29.md)
  Creates a command that fast-forwards through the media.
- [static func seekBackward(beginAction: () async throws -> Void, endAction: () async throws -> Void) -> MediaCommand](./mediacommand/seekbackward%28beginaction,endaction%29.md)
  Creates a command that rewinds through the media.
### Changing playback modes
- [static func changePlaybackRate(supported: [Float], (Float) async throws -> Void) -> MediaCommand](./mediacommand/changeplaybackrate%28supported,_%29.md)
  Creates a command that changes the playback rate of the media.
- [static func changeRepeatMode(current: MediaCommand.RepeatMode, supported: [MediaCommand.RepeatMode]?, (MediaCommand.RepeatMode) async throws -> Void) -> MediaCommand](./mediacommand/changerepeatmode%28current,supported,_%29.md)
  Creates a command that changes the repeat mode for media playback.
- [static func changeShuffleMode(current: MediaCommand.ShuffleMode, supported: [MediaCommand.ShuffleMode]?, (MediaCommand.ShuffleMode) async throws -> Void) -> MediaCommand](./mediacommand/changeshufflemode%28current,supported,_%29.md)
  Creates a command that changes the shuffle mode for media playback.
- [MediaCommand.RepeatMode](./mediacommand/repeatmode.md)
  The repeat mode for media playback.
- [MediaCommand.ShuffleMode](./mediacommand/shufflemode.md)
  The shuffle mode for media playback.
### Providing feedback
- [static func feedback(title: String?, shortTitle: String?, status: MediaCommand.FeedbackStatus, (MediaCommand.FeedbackStatus) async throws -> Void) -> MediaCommand](./mediacommand/feedback%28title,shorttitle,status,_%29.md)
  Creates a command that handles user feedback (positive, neutral, or negative) for the current content.
- [MediaCommand.FeedbackStatus](./mediacommand/feedbackstatus.md)
  The feedback status for a media item.

## See Also

### Playback
- [struct MediaPlaybackSnapshot](./mediaplaybacksnapshot.md)
  A snapshot of playback state and timing for a Now Playing session.
- [Content types and metadata](./content-types-and-metadata.md)
  Describe the media your app is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/playback-commands)*