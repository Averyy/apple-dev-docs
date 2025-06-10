# NWParameters

**Framework**: Network  
**Kind**: class

An object that stores the protocols to use for connections, options for sending data, and network path constraints.

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
final class NWParameters
```

## Mentions

- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)

## Topics

### Creating Parameters
- [class var tls: NWParameters](nwparameters/tls.md)
  A set of default parameters for connections and listeners that use TLS and TCP.
- [class var tcp: NWParameters](nwparameters/tcp.md)
  A set of default parameters for connections and listeners that use TCP.
- [class var dtls: NWParameters](nwparameters/dtls.md)
  A set of default parameters for connections and listeners that use DTLS and UDP.
- [class var udp: NWParameters](nwparameters/udp.md)
  A set of default parameters for connections and listeners that use UDP.
- [class func quic(alpn: [String]) -> NWParameters](nwparameters/quic(alpn:).md)
  Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [class func quicDatagram(alpn: [String]) -> NWParameters](nwparameters/quicdatagram(alpn:).md)
  Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [convenience init(tls: NWProtocolTLS.Options?, tcp: NWProtocolTCP.Options)](nwparameters/init(tls:tcp:).md)
  Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [convenience init(dtls: NWProtocolTLS.Options?, udp: NWProtocolUDP.Options)](nwparameters/init(dtls:udp:).md)
  Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [convenience init(quic: NWProtocolQUIC.Options)](nwparameters/init(quic:).md)
  Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](nwparameters/init.md)
  Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber: UInt8)](nwparameters/init(customipprotocolnumber:).md)
  Initializes parameters for connections and listeners using a custom IP protocol.
- [func copy() -> NWParameters](nwparameters/copy.md)
  Performs a deep copy of a parameters object.
### Modifying Protocol Stacks
- [var defaultProtocolStack: NWParameters.ProtocolStack](nwparameters/defaultprotocolstack.md)
  The protocol stack used by connections and listeners.
- [NWParameters.ProtocolStack](nwparameters/protocolstack.md)
  An ordered set of protocol options that define the protocols that connections and listeners use.
- [class NWProtocol](nwprotocol.md)
  The abstract superclass used by Network framework protocols and by custom network protocols that you define.
### Selecting Paths
- [var requiredInterfaceType: NWInterface.InterfaceType](nwparameters/requiredinterfacetype.md)
  An interface type to require on connections and listeners.
- [var requiredInterface: NWInterface?](nwparameters/requiredinterface.md)
  A specific interface to require on connections, listeners, and browsers.
- [var requiredLocalEndpoint: NWEndpoint?](nwparameters/requiredlocalendpoint.md)
  A specific local IP address and port to use for connections and listeners.
- [var prohibitConstrainedPaths: Bool](nwparameters/prohibitconstrainedpaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [var prohibitExpensivePaths: Bool](nwparameters/prohibitexpensivepaths.md)
  A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [var prohibitedInterfaceTypes: [NWInterface.InterfaceType]?](nwparameters/prohibitedinterfacetypes.md)
  A list of interface types that connections, listeners, and browsers will not use.
- [var prohibitedInterfaces: [NWInterface]?](nwparameters/prohibitedinterfaces.md)
  A list of specific interfaces that connections and listeners will not use.
### Customizing Connection Options
- [var multipathServiceType: NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
- [NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [var serviceClass: NWParameters.ServiceClass](nwparameters/serviceclass-swift.property.md)
  A level of service quality for connections to use for Cellular Network Slicing.
- [NWParameters.ServiceClass](nwparameters/serviceclass-swift.enum.md)
  Indicates the traffic characteristics of the network connections used by Cellular Network Slicing.
- [var allowFastOpen: Bool](nwparameters/allowfastopen.md)
  A Boolean that enables sending application data with protocol handshakes.
- [var expiredDNSBehavior: NWParameters.ExpiredDNSBehavior](nwparameters/expireddnsbehavior-swift.property.md)
  A behavior that defines how expired DNS answers will be used.
- [NWParameters.ExpiredDNSBehavior](nwparameters/expireddnsbehavior-swift.enum.md)
  Options for configuring how expired DNS answers should be used.
- [var requiresDNSSECValidation: Bool](nwparameters/requiresdnssecvalidation.md)
  A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [var preferNoProxies: Bool](nwparameters/prefernoproxies.md)
  A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [var includePeerToPeer: Bool](nwparameters/includepeertopeer.md)
  A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [var allowLocalEndpointReuse: Bool](nwparameters/allowlocalendpointreuse.md)
  A Boolean that allows reusing local addresses and ports across connections.
- [var acceptLocalOnly: Bool](nwparameters/acceptlocalonly.md)
  A Boolean that restricts listeners to only accepting connections from the local link.
### Configuring Privacy Settings
- [func setPrivacyContext(NWParameters.PrivacyContext)](nwparameters/setprivacycontext(_:).md)
  Associates a privacy context with any connections or listeners that use the parameters.
- [NWParameters.PrivacyContext](nwparameters/privacycontext.md)
  An object that defines the privacy requirements for a set of connections.
### Instance Properties
- [var allowUltraConstrainedPaths: Bool](nwparameters/allowultraconstrainedpaths.md)
  Allow connection to use interfaces considered ultra-constrained by the system
- [var attribution: NWParameters.Attribution](nwparameters/attribution-swift.property.md)
- [var wifiAware: WAParameters](nwparameters/wifiaware.md)
  Get and set Wi-Fi Aware specific connection parameters.
### Instance Methods
- [func wifiAware((inout WAParameters) -> Void) -> Self](nwparameters/wifiaware(_:).md)
  Configure Wi-Fi Aware properties on an `NWParameters` object.
### Type Properties
- [class var applicationService: NWParameters](nwparameters/applicationservice.md)
  The default parameters for connecting with other, local devices that are running your app.
### Enumerations
- [NWParameters.Attribution](nwparameters/attribution-swift.enum.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [NWParametersProvider](nwparametersprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NWEndpoint](nwendpoint.md)
  A local or remote endpoint in a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters)*