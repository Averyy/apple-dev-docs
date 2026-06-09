# RemoteMediaSession

**Framework**: Now Playing  
**Kind**: class

A session that manages remote media playback across devices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
class RemoteMediaSession<Attributes> where Attributes : RemoteMediaSessionAttributes
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Use a remote session to represent media playback sessions happening outside of this device, but that your app wants to donate to the system so they may appear in the system’s Now Playing interface.

Use this API when your app has information about the remote session and wants to signal to the system that playback has started (using [`start(attributes:)`](remotemediasession/start(attributes:).md)) or something about the session has changed (using [`update(_:)`](remotemediasession/update(_:).md)).

You can also donate remote sessions to the system through push notifications, for example when playback starts while your app isn’t running.

In that case, use APNs to send a push notification to the user’s device that informs the system of a `start`, `update`, or `end` event.

The following example shows how to start a session:

```swift
struct MySessionAttributes: RemoteMediaSessionAttributes {
    let id: String
    let trackID: String
}

let attributes = MySessionAttributes(id: "session-123", trackID: "track-123")
let session = try await RemoteMediaSession.start(attributes: attributes)
```

After starting a session, update its attributes or end it:

```swift
// Update the session attributes
try await session.update(newAttributes)

// End the session when playback completes
try await session.end()
```

## Topics

### Instance Properties
- [let id: String](remotemediasession/id.md)
  The unique identifier for this session.
- [var isSystemPrimary: Bool](remotemediasession/issystemprimary.md)
  A Boolean value that indicates whether this is currently the primary system session.
### Instance Methods
- [func end() async throws](remotemediasession/end.md)
  Ends the session and removes it from the Now Playing interface.
- [func requestToBecomeSystemPrimary() async throws](remotemediasession/requesttobecomesystemprimary.md)
  Requests to make this session the system primary media session.
- [func update(Attributes) async throws](remotemediasession/update(_:).md)
  Updates the session with new attributes.
### Type Properties
- [static var pushToStartToken: Data?](remotemediasession/pushtostarttoken.md)
  The token you use to start a [`RemoteMediaSession`](remotemediasession.md) through a push notification.
- [static var pushToStartTokenUpdates: AsyncStream<Data>](remotemediasession/pushtostarttokenupdates.md)
  An asynchronous sequence that delivers updated tokens for starting a [`RemoteMediaSession`](remotemediasession.md) through a push notification.
### Type Methods
- [static func sessions() async throws -> [RemoteMediaSession<Attributes>]](remotemediasession/sessions.md)
  Returns all registered remote sessions.
- [static func start(attributes: Attributes) async throws -> RemoteMediaSession<Attributes>](remotemediasession/start(attributes:).md)
  Starts a new remote session with the specified attributes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
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

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession)*