# AVSystemRoute

**Framework**: AVSystemRouting  
**Kind**: class

An active media route to a remote device that manages connection and communication for media playback and data exchange.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class AVSystemRoute
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)

#### Overview

Use this object to control playback sessions, communicate with remote applications through data channels, and manage the lifecycle of remote connections.

The system route provides a high-level abstraction for routing media content to external devices such as TVs, speakers, or other compatible endpoints. You can create multiple sessions on a single route to manage different playback contexts or communication channels.

#### Manage Sessions

Create an [`AVSystemRouteSession`](avsystemroutesession-gp78.md) to initiate playback or communication with the remote device.

#### Access the Protocol Identifier

The [`protocolType`](avsystemroute-5s2um/protocoltype.md) property identifies the communication protocol used by the active route.

#### Send and Receive Data

Use the [`routeDataChannel`](avsystemroute-5s2um/routedatachannel.md) property to send and receive custom data with the extension outside of any media session. This enables control messages, state synchronization, and other bidirectional communication needs.

## Topics

### Classes
- [AVSystemRoute.DataChannel](avsystemroute-5s2um/datachannel.md)
  An object that manages bidirectional data communication with a remote application.
### Instance Properties
- [var protocolType: UTType](avsystemroute-5s2um/protocoltype.md)
  The communication protocol the active route uses.
- [var routeDataChannel: AVSystemRoute.DataChannel](avsystemroute-5s2um/routedatachannel.md)
  A data channel for communicating with the extension outside of any media session.
- [var routeDisplayName: String](avsystemroute-5s2um/routedisplayname.md)
  The user-facing display name of the remote device or route.
- [var routeSymbolName: String](avsystemroute-5s2um/routesymbolname.md)
  The SF Symbol name representing the remote device or route.
### Instance Methods
- [func addSession(AVSystemRouteSession) -> Bool](avsystemroute-5s2um/addsession(_:).md)
  Adds a session to the active route.
- [func removeSession(AVSystemRouteSession)](avsystemroute-5s2um/removesession(_:).md)
  Removes a session from the active route.
### Enumerations
- [AVSystemRoute.LaunchMode](avsystemroute-5s2um/launchmode.md)
  The mode that determines how media playback launches on a remote device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVSystemRouteSession](avsystemroutesession-gp78.md)
  An object that manages a single media playback session on a remote device.
- [AVSystemRoute.LaunchMode](avsystemroute-5s2um/launchmode.md)
  The mode that determines how media playback launches on a remote device.
- [enum AVSystemRouteLaunchMode](avsystemroutelaunchmode.md)
  The mode that determines how media playback launches on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um)*