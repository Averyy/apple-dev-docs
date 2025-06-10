# NetworkListener

**Framework**: Network  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final class NetworkListener<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Topics

### Initializers
- [convenience init(for: any ListenerProvider, using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(for:using:)-64s14.md)
- [convenience init(for: any ListenerProvider, using: () -> ApplicationProtocol) throws](networklistener/init(for:using:)-6n089.md)
- [convenience init(on: NWEndpoint.Port, for: any ListenerProvider, using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(on:for:using:)-7l1be.md)
- [convenience init(on: NWEndpoint.Port, for: any ListenerProvider, using: () -> ApplicationProtocol) throws](networklistener/init(on:for:using:)-8cbpt.md)
- [init(on: NWEndpoint.Port, using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(on:using:)-4873s.md)
- [convenience init(on: NWEndpoint.Port, using: () -> ApplicationProtocol) throws](networklistener/init(on:using:)-7pzf2.md)
- [init(port: NWEndpoint.Port, provider: any ListenerProvider, builder: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(port:provider:builder:).md)
- [init(provider: any ListenerProvider, using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(provider:using:).md)
- [init(using: NWParametersBuilder<ApplicationProtocol>) throws](networklistener/init(using:)-4brg.md)
- [convenience init(using: () -> ApplicationProtocol) throws](networklistener/init(using:)-7lq05.md)
### Instance Properties
- [var newConnectionLimit: Int](networklistener/newconnectionlimit.md)
- [var port: NWEndpoint.Port?](networklistener/port.md)
- [var service: NWListener.Service?](networklistener/service.md)
### Instance Methods
- [func newConnectionLimit(Int) -> Self](networklistener/newconnectionlimit(_:).md)
- [func onServiceRegistrationUpdate(NetworkListener<ApplicationProtocol>.ServiceRegistrationUpdateHandler?) -> Self](networklistener/onserviceregistrationupdate(_:).md)
- [func onStateUpdate(NetworkListener<ApplicationProtocol>.StateUpdateHandler?) -> Self](networklistener/onstateupdate(_:).md)
- [func run((NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](networklistener/run(_:).md)
### Type Aliases
- [NetworkListener.ServiceRegistrationUpdateHandler](networklistener/serviceregistrationupdatehandler.md)
- [NetworkListener.State](networklistener/state.md)
- [NetworkListener.StateUpdateHandler](networklistener/stateupdatehandler.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener)*