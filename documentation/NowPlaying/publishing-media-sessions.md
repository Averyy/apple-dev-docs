# Publishing media sessions

**Framework**: Now Playing

Show your app’s media on the Lock Screen and Control Center.

#### Overview

A local session publishes media that’s playing on the current device. When you create one, the system shows your content’s metadata and playback controls across the Lock Screen, Control Center, and connected accessories, including CarPlay and AirPlay-capable devices.

To publish a local session, create a type that conforms to [`MediaSessionRepresentable`](mediasessionrepresentable.md), then register it with the system using [`MediaSession`](mediasession.md). The framework observes your model with [`Observable`](https://developer.apple.com/documentation/observation/observable) and syncs updates to the system automatically.

#### Create a Session Representable

To publish your media to the system, conform to [`MediaSessionRepresentable`](mediasessionrepresentable.md) and mark your type with the [`Observable`](https://developer.apple.com/documentation/observation/observable) macro. The framework reads four properties from your type: [`id`](mediasessionrepresentable/id.md) to uniquely identify the session, [`content`](mediasessionrepresentable/content.md) to describe what’s playing, [`playbackSnapshot`](mediasessionrepresentable/playbacksnapshot.md) to capture playback state, and [`commands`](mediasessionrepresentable/commands.md) to declare the controls your app supports.

```swift
import NowPlaying

@Observable
@MainActor
final class AudioPlayer: MediaSessionRepresentable {
    let id: String = UUID().uuidString

    var currentTrack: Track?
    var isPlaying: Bool = false
    var elapsedTime: TimeInterval = 0
    var timestamp: Date = .now

    var content: (any MediaContentRepresentable)? {
        guard let track = currentTrack else { return nil }
        return MusicContent(
            id: track.id,
            songTitle: track.title,
            artistName: track.artist,
            albumName: track.album,
            type: .audio,
            duration: .finite(track.duration),
            artwork: nil
        )
    }

    var playbackSnapshot: MediaPlaybackSnapshot? {
        MediaPlaybackSnapshot(
            state: isPlaying ? .playing() : .paused,
            elapsedTime: elapsedTime,
            timestamp: timestamp
        )
    }

    var commands: [MediaCommand] {
        [
            .play { self.play() },
            .pause { self.pause() },
        ]
    }

    func play() { /* ... */ }
    func pause() { /* ... */ }
}
```

The [`content`](mediasessionrepresentable/content.md) property returns a content type that matches your media. The framework provides [`MusicContent`](musiccontent.md), [`PodcastContent`](podcastcontent.md), [`MovieContent`](moviecontent.md), [`TVShowContent`](tvshowcontent.md), [`BookContent`](bookcontent.md), [`RadioContent`](radiocontent.md), [`HomeMediaContent`](homemediacontent.md), and [`GenericContent`](genericcontent.md).

The [`playbackSnapshot`](mediasessionrepresentable/playbacksnapshot.md) property returns a [`MediaPlaybackSnapshot`](mediaplaybacksnapshot.md) that captures the current playback state and progress. Provide the elapsed time and a timestamp so the system extrapolates the playback position between updates.

#### Add Artwork

Provide artwork by adding an [`Artwork`](artwork.md) structure for your content. The framework requests artwork from your process asynchronously at the size the system requires.

```swift
var content: (any MediaContentRepresentable)? {
    guard let track = currentTrack else { return nil }
    return MusicContent(
        id: track.id,
        songTitle: track.title,
        artistName: track.artist,
        albumName: track.album,
        type: .audio,
        duration: .finite(track.duration),
        artwork: Artwork(id: track.artworkID) { size in
            let (data, _) = try await URLSession.shared.data(from: track.artworkURL)
            return try ArtworkRepresentation(data: data)
        }
    )
}
```

#### Manage the Session Life Cycle

Create a [`MediaSession`](mediasession.md) from your representable and call [`requestToBecomeApplicationPrimary()`](mediasession/requesttobecomeapplicationprimary().md) to begin publishing. When playback ends, set your session reference to `nil` to remove it from the system.

```swift
@Observable
@MainActor
final class AudioPlayer: MediaSessionRepresentable {
    var session: MediaSession<AudioPlayer>?

    func activate() async throws {
        let session = MediaSession(self)
        self.session = session
        try await session.requestToBecomeApplicationPrimary()
    }

    func deactivate() {
        session = nil
    }

    // ...
}
```

If your app plays audio (such as music, a podcast, or an audiobook), configure the audio session before calling [`requestToBecomeApplicationPrimary()`](mediasession/requesttobecomeapplicationprimary().md):

```swift
let audioSession = AVAudioSession.sharedInstance()
try audioSession.setCategory(.playback, mode: .default)
try audioSession.setActive(true)
```

When you’re done with playback, call `setActive(false)` and pass `notifyOthersOnDeactivation` in the options so other apps can resume:

```swift
try audioSession.setActive(false, options: .notifyOthersOnDeactivation)
```

#### Coordinate Multiple Sessions

Apps can have more than one local session. For example, your app can be both a music player and a podcast player. Each session observes its own representable independently. Use [`requestToBecomeApplicationPrimary()`](mediasession/requesttobecomeapplicationprimary().md) to switch which session represents your app to the system.

To display a session on the Lock Screen and Control Center, call [`requestToBecomeSystemPrimary()`](mediasession/requesttobecomesystemprimary().md). This makes the session both your app’s primary session and the system’s active session.

```swift
try await session.requestToBecomeSystemPrimary()
```

> **Note**: Your app must be in the foreground when you call [`requestToBecomeSystemPrimary()`](mediasession/requesttobecomesystemprimary().md). If your app is in the background, the request has no effect.

Observe [`isApplicationPrimary`](mediasession/isapplicationprimary.md) and [`isSystemPrimary`](mediasession/issystemprimary.md) to reflect the current state in your UI.

#### Respond to Commands

Declare the commands your app supports in the [`commands`](mediasessionrepresentable/commands.md) property. Each entry is a [`MediaCommand`](mediacommand.md) created with a static factory method that takes an action closure. The system calls the closure when someone interacts with the corresponding control.

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
        .feedback(status: currentFeedback) { newStatus in
            self.setFeedback(newStatus)
        },
    ]
}
```

Use [`enabled(_:)`](mediacommand/enabled(_:).md) to conditionally make a command available or unavailable. For example, make [`next(_:)`](mediacommand/next(_:).md) unavailable when there are no more tracks in the queue.

For the full set of commands you can offer, including seek, skip, playback rate, repeat, shuffle, and feedback, see [`Playback commands`](playback-commands.md).

## See Also

- [protocol MediaSessionRepresentable](mediasessionrepresentable.md)
  A protocol that provides content metadata, playback state, and commands for a Now Playing session.
- [class MediaSession](mediasession.md)
  A local Now Playing session that publishes metadata and commands to the system.
- [enum MediaSessionError](mediasessionerror.md)
  Errors that can occur during local session operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/publishing-media-sessions)*