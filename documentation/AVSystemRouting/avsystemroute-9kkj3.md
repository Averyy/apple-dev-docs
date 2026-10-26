# AVSystemRoute

**Framework**: AVSystemRouting  
**Kind**: class  
**Role**: Class

An active media route to a remote device that manages connection and communication for media playback and data exchange.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVSystemRoute : NSObject
```

#### Overview

Use this object to control playback sessions, communicate with remote applications through data channels, and manage the lifecycle of remote connections.

The system route provides a high-level abstraction for routing media content to external devices such as TVs, speakers, or other compatible endpoints. You can create multiple sessions on a single route to manage different playback contexts or communication channels.

#### Manage sessions

Create an [`AVSystemRouteSession`](./avsystemroutesession-5i6j6.md) to initiate playback or communication with the remote device.

#### Access the protocol identifier

The [`protocolType`](./avsystemroute-9kkj3/protocoltype.md) property identifies the communication protocol used by the active route.

#### Send and receive data

Use the [`routeDataChannel`](./avsystemroute-9kkj3/routedatachannel.md) property to send and receive custom data with the extension outside of any media session. This enables control messages, state synchronization, and other bidirectional communication needs.

## Topics

### Instance Properties
- [protocolType](./avsystemroute-9kkj3/protocoltype.md)
  The communication protocol the active route uses.
- [routeDataChannel](./avsystemroute-9kkj3/routedatachannel.md)
  A data channel for communicating with the extension outside of any media session.
- [routeDisplayName](./avsystemroute-9kkj3/routedisplayname.md)
  The user-facing display name of the remote device or route.
- [routeSymbolName](./avsystemroute-9kkj3/routesymbolname.md)
  The SF Symbol name representing the remote device or route.
### Instance Methods
- [- addSession:](./avsystemroute-9kkj3/addsession_.md)
  Adds a session to the active route.
- [- removeSession:](./avsystemroute-9kkj3/removesession_.md)
  Removes a session from the active route.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Routes and sessions
- [AVSystemRouteSession](./avsystemroutesession-5i6j6.md)
  An object that manages a single media playback session on a remote device.
- [AVSystemRouteLaunchMode](./avsystemroutelaunchmode.md)
  The mode that determines how media playback launches on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-9kkj3)*