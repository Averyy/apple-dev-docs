# Publishing remote media sessions

**Framework**: Now Playing

Show media from an external device on the Lock Screen and Control Center.

#### Overview

A remote session represents media playback happening on an external device such as a speaker, streaming stick, or smart TV. When you publish a remote session, the framework makes the external device’s playback available for display on the Lock Screen and Control Center. Your app extension handles any commands the system routes back to the device.

Remote sessions use an app extension architecture. An app extension conforming to [`RemoteMediaSessionExtension`](remotemediasessionextension.md) provides the session content and handles commands.

Send push notifications from your server to start and update remote sessions, so the framework makes remote playback available for display even when your app isn’t running. In your main app, use [`RemoteMediaSession`](remotemediasession.md) to start, fetch, and update sessions.

#### Define Session Attributes

Create a [`Codable`](https://developer.apple.com/documentation/Swift/Codable) type that captures the playback state of the external device. Your app and extension share this type to communicate session state. Conform to [`RemoteMediaSessionAttributes`](remotemediasessionattributes.md) and include only the fields your app needs to represent the external device’s playback.

```swift
struct MySessionAttributes: RemoteMediaSessionAttributes {
    var id: String
    var isPlaying: Bool
    var elapsedTime: TimeInterval
    var timestamp: Date
    var currentTrack: TrackInfo?
    var devices: [DeviceInfo]
    var queueCount: Int
    var currentTrackIndex: Int
}
```

#### Declare the Extension

Add an app extension target to your project. In the extension’s Info pane in Xcode, add an `EXAppExtensionAttributes` dictionary with an `EXExtensionPointIdentifier` of `com.apple.nowplaying.remote-media`. Xcode writes the following entries to the extension’s `Info.plist` file:

```xml
<key>EXAppExtensionAttributes</key>
<dict>
    <key>EXExtensionPointIdentifier</key>
    <string>com.apple.nowplaying.remote-media</string>
</dict>
```

#### Create the App Extension

Define a type that conforms to [`RemoteMediaSessionExtension`](remotemediasessionextension.md) and annotate it with `@main`. The system calls [`session(_:)`](remotemediasessionextension/session(_:).md) when it needs your extension to produce a session for a given set of attributes. From the [`configuration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension/configuration-swift.property) property, return a [`RemoteMediaSessionExtensionConfiguration`](remotemediasessionextensionconfiguration.md) initialized with your extension instance.

```swift
import ExtensionFoundation
import NowPlaying

@main
struct MyRemotePlaybackExtension: RemoteMediaSessionExtension {
    var configuration: RemoteMediaSessionExtensionConfiguration<Self> {
        RemoteMediaSessionExtensionConfiguration(extension: self)
    }

    func session(_ attributes: MySessionAttributes) async throws -> MyRemoteSession {
        MyRemoteSession(attributes: attributes)
    }
}
```

The framework caches the sessions your extension returns and routes subsequent updates and commands to the same instance. If your extension connects to a backend or device, establish that connection once and reuse it across `session(_:)` calls.

#### Implement the Remote Session Representable

Create a type that conforms to [`RemoteMediaSessionRepresentable`](remotemediasessionrepresentable.md) to provide content, playback state, commands, and device information. Mark it with [`Observable`](https://developer.apple.com/documentation/Observation/Observable) to detect changes automatically.

```swift
import NowPlaying

@Observable
final class MyRemoteSession: @MainActor RemoteMediaSessionRepresentable {
    let id: String
    var attributes: MySessionAttributes
    let apiClient: MyAPIClient

    init(attributes: MySessionAttributes) {
        self.id = attributes.id
        self.attributes = attributes
        self.apiClient = MyAPIClient()
    }

    func update(_ attributes: MySessionAttributes) {
        self.attributes = attributes
    }

    var playbackSnapshot: MediaPlaybackSnapshot? {
        MediaPlaybackSnapshot(
            state: attributes.isPlaying ? .playing() : .paused,
            elapsedTime: attributes.elapsedTime,
            timestamp: attributes.timestamp
        )
    }
}
```

The system delivers incoming attribute changes to [`update(_:)`](remotemediasessionrepresentable/update(_:).md). Save them to your stored attributes so the Now Playing interface reflects the external device’s current state.

#### Provide Content and Commands

Implement [`content`](remotemediasessionrepresentable/content.md) and [`commands`](remotemediasessionrepresentable/commands.md) on your type to describe what’s playing and which commands the remote session supports. Forward each command to the external device.

```swift
extension MyRemoteSession {
    var content: (any MediaContentRepresentable)? {
        guard let track = attributes.currentTrack else { return nil }
        var content = MusicContent(
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
        content.isExplicit = track.isExplicit
        return content
    }

    var commands: [MediaCommand] {
        [
            .play { try await self.apiClient.sendCommand(.play) },
            .pause { try await self.apiClient.sendCommand(.pause) },
            .next { try await self.apiClient.sendCommand(.next) }
                .enabled(attributes.currentTrackIndex < attributes.queueCount - 1),
            .previous { try await self.apiClient.sendCommand(.previous) }
                .enabled(attributes.currentTrackIndex > 0),
            .seekToPosition { time in
                try await self.apiClient.sendCommand(.seek(to: time))
            },
        ]
    }
}
```

#### Provide Devices and Control Capabilities

Return the devices playing as part of the session from the [`devices`](remotemediasessionrepresentable/devices.md) property. Each [`MediaDevice`](mediadevice.md) declares the operations the system can perform on it through an array of [`MediaDevice.Capability`](mediadevice/capability.md) values.

```swift
extension MyRemoteSession {
    var devices: [MediaDevice] {
        attributes.devices.map { device in
            MediaDevice(
                id: device.id,
                name: device.name,
                type: .speaker,
                capabilities: [
                    .absoluteVolume(device.volume) { newLevel in
                        try await self.apiClient.setVolume(newLevel, forDevice: device.id)
                    }
                ]
            )
        }
    }
}
```

Use [`absoluteVolume(_:onChange:)`](mediadevice/capability/absolutevolume(_:onchange:).md) when the device exposes a volume level in the range `0.0` to `1.0`. The system calls the closure with the requested level when someone adjusts the volume slider.

For devices that only support stepwise volume changes, use [`relativeVolume(onIncrement:onDecrement:)`](mediadevice/capability/relativevolume(onincrement:ondecrement:).md) instead.

#### Start and Update Sessions From Your App

In your main app, use [`RemoteMediaSession`](remotemediasession.md) to start a session and send updates when the external device’s state changes:

```swift
let remoteSession = try await RemoteMediaSession.start(attributes: attributes)
```

When the external device’s state changes, update the session with new attributes. The `id` on the attributes must match the `id` used to start the session:

```swift
try await remoteSession.update(updatedAttributes)
```

To have the system show this session on the Lock Screen and Control Center, call [`requestToBecomeSystemPrimary()`](remotemediasession/requesttobecomesystemprimary().md):

```swift
try await remoteSession.requestToBecomeSystemPrimary()
```

> **Note**: Your app must be in the foreground when you call [`requestToBecomeSystemPrimary()`](remotemediasession/requesttobecomesystemprimary().md). If your app is in the background, the request has no effect.

When playback ends, call [`end()`](remotemediasession/end().md) to remove the session:

```swift
try await remoteSession.end()
```

#### Start and Update Sessions From Push Notifications

Remote sessions support push notifications. Your server can start, update, or end sessions when your app isn’t running. Use this approach when playback starts from a remote device without someone opening your app.

##### Observe the Push to Start Token

The push-to-start token lets your server start new remote sessions with a push notification. Observe [`pushToStartTokenUpdates`](remotemediasession/pushtostarttokenupdates.md) to receive the token whenever it changes, and read [`pushToStartToken`](remotemediasession/pushtostarttoken.md) to get the current value at any time. Send the latest token to your server so it can send push notifications to the right device.

```swift
// Observe token updates.
Task {
    for await token in RemoteMediaSession<MySessionAttributes>.pushToStartTokenUpdates {
        let tokenString = token.map { String(format: "%02x", $0) }.joined()
        try await apiClient.registerStartToken(tokenString)
    }
}

// Read the current token.
if let token = RemoteMediaSession<MySessionAttributes>.pushToStartToken {
    let tokenString = token.map { String(format: "%02x", $0) }.joined()
    try await apiClient.registerStartToken(tokenString)
}
```

##### Observe Session Update Tokens

Each active session has its own push token for receiving updates and end events. Observe [`pushTokenUpdates`](remotemediasessionrepresentable/pushtokenupdates.md) from inside your extension’s session, and query the latest token using [`pushToken`](remotemediasessionrepresentable/pushtoken.md):

```swift
extension MyRemoteSession {
    func startObservingPushToken() {
        if let token = pushToken {
            let tokenString = token.map { String(format: "%02x", $0) }.joined()
            Task { try? await apiClient.registerUpdateToken(tokenString, forSessionID: id) }
        }

        Task { [weak self] in
            guard let self else { return }
            for await token in pushTokenUpdates {
                let tokenString = token.map { String(format: "%02x", $0) }.joined()
                try? await apiClient.registerUpdateToken(tokenString, forSessionID: id)
            }
        }
    }
}
```

#### Send Push Notifications From Your Server

Your server sends APNs push notifications to start, update, or end remote sessions. Use the `nowplaying` push type for each push and target the topic `<your-bundle-id>.push-type.nowplaying`.

Set the following headers on your APNs request:

```None
apns-topic: com.example.myapp.push-type.nowplaying
apns-push-type: nowplaying
```

##### Start a Session

To start a new remote session, send a push to the push-to-start token. The `event` field must be `"start"`, and the `attributes` field must contain a JSON-encoded representation of your [`RemoteMediaSessionAttributes`](remotemediasessionattributes.md):

```json
{
    "aps": {
        "event": "start",
        "timestamp": 1773907200,
        "attributes": {
            "id": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
            "devices": [
                {
                    "id": "living-room-speaker",
                    "name": "Living Room Speaker",
                    "type": "speaker",
                    "volume": 0.65
                }
            ],
            "isPlaying": true,
            "currentTrackIndex": 0,
            "queueCount": 5,
            "elapsedTime": 0,
            "timestamp": "2026-03-16T12:00:00Z",
            "currentTrack": {
                "id": "track-1",
                "title": "Song Title",
                "artist": "Name of Artist",
                "album": "Title of the Album",
                "duration": 237.0,
                "artworkURL": "https://example.com/artwork/track-1"
            }
        }
    }
}
```

When the system receives this push, it wakes your app extension and calls [`session(_:)`](remotemediasessionextension/session(_:).md) with the decoded attributes. Return a [`RemoteMediaSessionRepresentable`](remotemediasessionrepresentable.md) object from this method.

##### Update a Session

To update an existing session, like when someone skips to the next track on the remote device, send a push notification to the session’s update token with the `event` field set to `"update"`:

```json
{
    "aps": {
        "event": "update",
        "timestamp": 1773907444,
        "attributes": {
            "id": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
            "devices": [
                {
                    "id": "living-room-speaker",
                    "name": "Living Room Speaker",
                    "type": "speaker",
                    "volume": 0.65
                }
            ],
            "isPlaying": true,
            "currentTrackIndex": 1,
            "queueCount": 5,
            "elapsedTime": 0,
            "timestamp": "2026-06-08T12:00:00Z",
            "currentTrack": {
                "id": "track-2",
                "title": "Song Title",
                "artist": "Name of Artist",
                "album": "Title of the Album",
                "duration": 312.0,
                "artworkURL": "https://example.com/artwork/track-2"
            }
        }
    }
}
```

The system delivers the updated attributes to your extension’s [`update(_:)`](remotemediasessionrepresentable/update(_:).md) method, and the Now Playing interface updates to reflect the new content.

##### End a Session

To end a session when playback stops on the remote device, send a push to the session’s update token with the `event` field set to `"end"`. Only the session `id` is required in the attributes:

```json
{
    "aps": {
        "event": "end",
        "timestamp": 1773907847,
        "attributes": {
            "id": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890"
        }
    }
}
```

## See Also

- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
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

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/publishing-remote-media-sessions)*