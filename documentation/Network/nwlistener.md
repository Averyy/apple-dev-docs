# NWListener

**Framework**: Network  
**Kind**: class

An object you use to listen for incoming network connections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final class NWListener
```

## Mentions

- [Creating an Identity for Local Network TLS](creating-an-identity-for-local-network-tls.md)

## Topics

### Creating Listeners
- [init(using: NWParameters, on: NWEndpoint.Port) throws](nwlistener/init(using:on:).md)
  Initializes a network listener, with an optional local port.
- [func start(queue: DispatchQueue)](nwlistener/start(queue:).md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [var stateUpdateHandler: ((NWListener.State) -> Void)?](nwlistener/stateupdatehandler.md)
  A handler that receives listener state updates.
- [NWListener.State](nwlistener/state-swift.enum.md)
  States indicating whether a listener is able to accept incoming connections.
- [var port: NWEndpoint.Port?](nwlistener/port.md)
  The port on which the listener can accept connections.
- [func cancel()](nwlistener/cancel.md)
  Stops listening for inbound connections.
### Receiving Connections
- [var newConnectionHandler: ((NWConnection) -> Void)?](nwlistener/newconnectionhandler.md)
  A handler that receives inbound connections.
- [var newConnectionLimit: Int](nwlistener/newconnectionlimit.md)
  The remaining number of inbound connections to deliver before rejecting connections.
- [static let InfiniteConnectionLimit: Int](nwlistener/infiniteconnectionlimit.md)
  A static value to indicate that inbound connections should not be limited.
### Advertising Bonjour Services
- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells the user why the app is requesting access to the local network.
- [var service: NWListener.Service?](nwlistener/service-swift.property.md)
  A Bonjour service that advertises the listener on the local network.
- [NWListener.Service](nwlistener/service-swift.struct.md)
  A description used to advertise the Bonjour service that a listener provides.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](nwlistener/serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.
- [NWListener.ServiceRegistrationChange](nwlistener/serviceregistrationchange.md)
  Changes to how a network listener’s service is advertised.
### Inspecting Listeners
- [let parameters: NWParameters](nwlistener/parameters.md)
  The parameters used to initialize the listener.
- [var queue: DispatchQueue?](nwlistener/queue.md)
  The queue on which listener events are delivered.
### Initializers
- [convenience init(applicationService: String, using: NWParameters) throws](nwlistener/init(applicationservice:using:).md)
- [convenience init?(launchd: String, using: NWParameters)](nwlistener/init(launchd:using:).md)
- [convenience init(launchdSocketKey: String, parameters: NWParameters)](nwlistener/init(launchdsocketkey:parameters:).md)
- [convenience init(service: NWListener.Service, using: NWParameters) throws](nwlistener/init(service:using:).md)
### Instance Properties
- [var newConnectionGroupHandler: ((NWConnectionGroup) -> Void)?](nwlistener/newconnectiongrouphandler.md)
- [var state: NWListener.State](nwlistener/state-swift.property.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NWConnection](nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWBrowser](nwbrowser.md)
  An object you use to browse for available network services.
- [class NWConnectionGroup](nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [class NWEthernetChannel](nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener)*