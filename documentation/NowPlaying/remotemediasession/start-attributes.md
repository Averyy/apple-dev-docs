# start(attributes:)

**Framework**: Now Playing  
**Kind**: method

Starts a new remote session with the specified attributes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func start(attributes: Attributes) async throws -> RemoteMediaSession<Attributes>
```

#### Return Value

A remote session instance.

#### Discussion

This method registers a session. The attributes are encoded and sent to your app extension, which creates the actual session using your [`RemoteMediaSessionExtension`](remotemediasessionextension.md) conformance.

> **Note**: [`RemoteMediaSessionError.internalFailure`](remotemediasessionerror/internalfailure.md) if the system couldn’t register the session. Also throws an encoding error if `attributes` isn’t encodable.

## Parameters

- `attributes`: The attributes that configure the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/start(attributes:))*