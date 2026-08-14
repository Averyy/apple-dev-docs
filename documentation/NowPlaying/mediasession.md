# MediaSession

**Framework**: Now Playing  
**Kind**: class

A local Now Playing session that publishes metadata and commands to the system.

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
class MediaSession<Representable> where Representable : MediaSessionRepresentable
```

## Mentions

- [Publishing media sessions](publishing-media-sessions.md)

#### Overview

Use a session to represent media playback happening on the current device. The session automatically observes your [`MediaSessionRepresentable`](mediasessionrepresentable.md) model and syncs changes to the system’s Now Playing interface.

For more information, see [`Publishing media sessions`](publishing-media-sessions.md)

Create a session by providing a session representable:

```swift
let session = MediaSession(myModel)
```

Call [`requestToBecomeApplicationPrimary()`](mediasession/requesttobecomeapplicationprimary().md) to make this your app’s primary Now Playing session when you want to display playback controls:

```swift
try await session.requestToBecomeApplicationPrimary()
```

## Topics

### Initializers
- [init(Representable)](mediasession/init(_:).md)
  Creates a new local Now Playing session.
### Instance Properties
- [var canBecomeApplicationPrimary: Bool](mediasession/canbecomeapplicationprimary.md)
  A Boolean value that indicates whether this session can become the app’s primary session.
- [let id: String](mediasession/id.md)
  The unique identifier for this session.
- [var isApplicationPrimary: Bool](mediasession/isapplicationprimary.md)
  A Boolean value that indicates whether this is currently the primary application session.
- [var isSystemPrimary: Bool](mediasession/issystemprimary.md)
  A Boolean value that indicates whether this is currently the primary system session.
### Instance Methods
- [func requestToBecomeApplicationPrimary() async throws](mediasession/requesttobecomeapplicationprimary.md)
  Attempts to make this session your app’s primary media session.
- [func requestToBecomeSystemPrimary() async throws](mediasession/requesttobecomesystemprimary.md)
  Requests to make this session the primary system media session.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Publishing media sessions](publishing-media-sessions.md)
  Show your app’s media on the Lock Screen and Control Center.
- [protocol MediaSessionRepresentable](mediasessionrepresentable.md)
  A protocol that provides content metadata, playback state, and commands for a Now Playing session.
- [enum MediaSessionError](mediasessionerror.md)
  Errors that can occur during local session operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasession)*