# MediaSessionRepresentable

**Framework**: Now Playing  
**Kind**: protocol

A protocol that provides content metadata, playback state, and commands for a Now Playing session.

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
protocol MediaSessionRepresentable : Identifiable
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Conform to this protocol to provide the media content description, playback state, and commands like [`play(_:)`](mediacommand/play(_:).md), [`pause(_:)`](mediacommand/pause(_:).md), [`next(_:)`](mediacommand/next(_:).md), [`previous(_:)`](mediacommand/previous(_:).md), and more.

The framework observes your `@Observable` model and automatically updates the system’s Now Playing interface when your properties change.

For more information, see [`Publishing media sessions`](publishing-media-sessions.md)

The following example shows a basic session representable:

```swift
@Observable
class PlayerModel: MediaSessionRepresentable {
    let id = "com.example.music"
    var currentTrack: Track?
    var isPlaying = false
    var currentTime: TimeInterval = 0

    var content: (any MediaContentRepresentable)? {
        guard let track = currentTrack else { return nil }
        return MusicContent(
            id: track.id,
            songTitle: track.title,
            artistName: track.artist,
            albumName: track.album,
            type: .audio,
            duration: .finite(track.duration),
            isExplicit: track.isExplicit,
            artwork: Artwork(id: track.artworkID) { size in
                let data = await self.loadArtworkData(with: size)
                return try ArtworkRepresentation(data: data)
            }
        )
    }

    var playbackSnapshot: MediaPlaybackSnapshot? {
        if isPlaying {
            return MediaPlaybackSnapshot(state: .playing(rate: 1.0), elapsedTime: currentTime, timestamp: .now)
        } else {
            return MediaPlaybackSnapshot(state: .paused, elapsedTime: currentTime, timestamp: .now)
        }
    }

    var commands: [MediaCommand] {[
        .play { await self.play() },
        .pause { await self.pause() },
        .next { await self.nextTrack() },
        .previous { await self.previousTrack() },
    ]}
}
```

## Topics

### Instance Properties
- [var commands: [MediaCommand]](mediasessionrepresentable/commands.md)
  The commands supported by this session.
- [var content: (any MediaContentRepresentable)?](mediasessionrepresentable/content.md)
  The content being played in this session.
- [var id: String](mediasessionrepresentable/id.md)
  The unique identifier for this session.
- [var playbackSnapshot: MediaPlaybackSnapshot?](mediasessionrepresentable/playbacksnapshot.md)
  The current playback state of this session.

## Relationships

### Inherits From
- [Identifiable](../swift/identifiable.md)

## See Also

- [Publishing media sessions](publishing-media-sessions.md)
  Show your app’s media on the Lock Screen and Control Center.
- [class MediaSession](mediasession.md)
  A local Now Playing session that publishes metadata and commands to the system.
- [enum MediaSessionError](mediasessionerror.md)
  Errors that can occur during local session operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasessionrepresentable)*