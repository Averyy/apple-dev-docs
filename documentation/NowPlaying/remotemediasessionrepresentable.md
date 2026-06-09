# RemoteMediaSessionRepresentable

**Framework**: Now Playing  
**Kind**: protocol

A session that plays remotely, potentially across multiple devices.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol RemoteMediaSessionRepresentable : Identifiable
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Conform to this protocol to represent playback happening outside of the current device. This object is expected to interact with a remote device, and thus may require some form of remote connection that you set up on initialization.

Your session provides metadata and supported commands, as well as the list of devices playing in this session. It also handles volume changes and commands targeting the remote session.

> ❗ **Important**: The system may request updates about this session via [`update(_:)`](remotemediasessionrepresentable/update(_:).md), where an instance of a `Codable` type your app defines passes into the function. Your implementation uses the passed [`Attributes`](remotemediasessionrepresentable/attributes.md) instance to update the model objects from your session, which informs the system of any metadata or command changes.

Your app donates remote sessions to the system in two ways: from the main app, or through push notifications.

See [`RemoteMediaSession`](remotemediasession.md) for the in-app API to donate a remote session.

The following example shows a basic implementation:

```swift
// A struct representing the current playback information from a remote device.
struct PlayerSnapshot: Codable {
  let trackId: String
  let title: String
  let artist: String
  let album: String
  let duration: Double
  let elapsedTime: Double
  let timestamp: Date
  let isPlaying: Bool
  let playingDevices: [PlayingDevice]
}

struct PlayingDevice: Codable {
  let id: String
  let name: String
  let volume: Float
}

@Observable
class RemotePlayerModel {
    var server: ServerConnection
    var snapshot: PlayerSnapshot
}

class MySession: RemoteMediaSessionRepresentable {
    struct Attributes: RemoteMediaSessionAttributes {
        let id: String
        var snapshot: PlayerSnapshot
    }

    let id: String
    var remotePlayer: RemotePlayerModel

    var devices: [MediaDevice] {
        remotePlayer.snapshot.playingDevices.map { device in
            MediaDevice(
                id: device.id,
                name: device.name,
                type: .speaker,
                capabilities: [
                    .absoluteVolume(device.volume) { newLevel in
                        // Communicate with an external server to issue the volume change
                        try await remotePlayer.server.setVolume(newLevel, forDevice: device.id)
                    }
                ]
            )
        }
    }

    var content: (any MediaContentRepresentable)? {
        let snapshot = remotePlayer.snapshot
        return MusicContent(
            id: snapshot.trackId,
            songTitle: snapshot.title,
            artistName: snapshot.artist,
            albumName: snapshot.album,
            type: .audio,
            duration: .finite(snapshot.duration),
            artwork: Artwork(id: snapshot.trackId) { size in
                let data = await remotePlayer.server.loadArtworkData(for: snapshot.trackId, size: size)
                return try ArtworkRepresentation(data: data)
            }
        )
    }

    var playbackSnapshot: MediaPlaybackSnapshot {
        let snapshot = remotePlayer.snapshot
        if snapshot.isPlaying {
            return MediaPlaybackSnapshot(
                state: .playing(rate: 1.0),
                elapsedTime: snapshot.elapsedTime,
                timestamp: snapshot.timestamp
            )
        } else {
            return MediaPlaybackSnapshot(
                state: .paused,
                elapsedTime: snapshot.elapsedTime,
                timestamp: snapshot.timestamp
            )
        }
    }

    var commands: [MediaCommand] {[
        .play {
          // Communicate with an external server to issue the command
          try await remotePlayer.server.play()
        },
        .pause {
          try await remotePlayer.server.pause()
        },
        // … more supported commands …
    ]}

    func update(_ attributes: Attributes) {
      // Incorporate the incoming attributes into your existing model
      remotePlayer.update(with: attributes)
    }
    // …
}
```

## Topics

### Associated Types
- [associatedtype Attributes : RemoteMediaSessionAttributes](remotemediasessionrepresentable/attributes.md)
  A `Codable` type you define to identify this session and carry its remote state.
### Instance Properties
- [var commands: [MediaCommand]](remotemediasessionrepresentable/commands.md)
  The commands supported by this session.
- [var content: (any MediaContentRepresentable)?](remotemediasessionrepresentable/content.md)
  The content being played in this session.
- [var devices: [MediaDevice]](remotemediasessionrepresentable/devices.md)
  The devices currently playing as part of this session.
- [var id: String](remotemediasessionrepresentable/id.md)
  The unique identifier for this session.
- [var playbackSnapshot: MediaPlaybackSnapshot?](remotemediasessionrepresentable/playbacksnapshot.md)
  The current playback state of this session.
- [var pushToken: Data?](remotemediasessionrepresentable/pushtoken.md)
  The token you use to send push notifications to update this remote session.
- [var pushTokenUpdates: AsyncStream<Data>](remotemediasessionrepresentable/pushtokenupdates.md)
  An asynchronous sequence you use to observe changes to the push token of this remote session.
### Instance Methods
- [func update(Self.Attributes)](remotemediasessionrepresentable/update(_:).md)
  Updates the session state from new attributes.

## Relationships

### Inherits From
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [class RemoteMediaSession](remotemediasession.md)
  A session that manages remote media playback across devices.
- [protocol RemoteMediaSessionExtension](remotemediasessionextension.md)
  An app extension that provides remote media sessions.
- [class RemoteMediaSessionExtensionConfiguration](remotemediasessionextensionconfiguration.md)
  The configuration object for a remote playback extension.
- [protocol RemoteMediaSessionAttributes](remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.
- [struct MediaDevice](mediadevice.md)
  A device that plays media in a remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable)*