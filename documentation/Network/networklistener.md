# NetworkListener

**Framework**: Network  
**Kind**: class

Listen for incoming network connections.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final class NetworkListener<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

#### Overview

A listener receives incoming connections by binding to a local endpoint. It accepts connections based on the protocols defined in its protocol stack. Accepted connections will represent new local and remote address and port tuples.

## Topics

### Initializers
- [convenience init(for: (any ListenerProvider)?, using: () -> ApplicationProtocol) throws](networklistener/init(for:using:)-2hkg.md)
  Create a listener that advertises a service with a protocol stack to use for listening.
- [convenience init(for: (any ListenerProvider)?, using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(for:using:)-2vh87.md)
  Create a listener that advertises a service with a protocol stack and parameters to use for listening.
### Instance Properties
- [var newConnectionLimit: Int](networklistener/newconnectionlimit.md)
  Configure the listener’s new connection limit.
- [var port: NWEndpoint.Port?](networklistener/port.md)
  The port that the listener is listening on.
- [var service: NWListener.Service?](networklistener/service.md)
  An optional service to advertise with the listener.
### Instance Methods
- [func newConnectionLimit(Int) -> Self](networklistener/newconnectionlimit(_:).md)
  Configure the listener’s new connection limit.
- [func onServiceRegistrationUpdate((NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.ServiceRegistrationChange) -> Void) -> Self](networklistener/onserviceregistrationupdate(_:).md)
  Set a closure to be called when the listener has added or removed a registered service.
- [func onStateUpdate((NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.State) -> Void) -> Self](networklistener/onstateupdate(_:).md)
  Set a closure to be called when the listener’s state changes.
- [func run((NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](networklistener/run(_:)-42k25.md)
  Run the listener and receive incoming multiplexed connections.
- [func run((NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](networklistener/run(_:)-4iov3.md)
  Run the listener and receive incoming connections.
### Type Aliases
- [NetworkListener.ServiceRegistrationUpdateHandler](networklistener/serviceregistrationupdatehandler.md)
- [NetworkListener.StateUpdateHandler](networklistener/stateupdatehandler.md)
### Enumerations
- [NetworkListener.ServiceRegistrationChange](networklistener/serviceregistrationchange.md)
- [NetworkListener.State](networklistener/state.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener)*