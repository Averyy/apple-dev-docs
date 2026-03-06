# Network

**Framework**: Network  
**Kind**: module

Create network connections to send and receive data using transport and security protocols.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Mentions

- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)
- [Inspecting app activity data](inspecting-app-activity-data.md)

#### Overview

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see [`TN3151: Choosing the right networking API`](https://developer.apple.com/documentation/Technotes/tn3151-choosing-the-right-networking-api).

> **Note**:  watchOS supports Network framework for specific use cases. For more details, see [`TN3135: Low-level networking on watchOS`](https://developer.apple.com/documentation/Technotes/tn3135-low-level-networking-on-watchOS).

## Topics

### Essentials
- [enum NWEndpoint](nwendpoint.md)
  A local or remote endpoint in a network connection.
- [class NWParameters](nwparameters.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
### Connections and Listeners
- [class NWConnection](nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWListener](nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWBrowser](nwbrowser.md)
  An object you use to browse for available network services.
- [class NWConnectionGroup](nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [class NWEthernetChannel](nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.
### Network Protocols
- [Building a custom peer-to-peer protocol](building-a-custom-peer-to-peer-protocol.md)
  Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionOS/connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.
- [class NWProtocolTCP](nwprotocoltcp.md)
  A network protocol for connections that use the Transmission Control Protocol.
- [class NWProtocolTLS](nwprotocoltls.md)
  A network protocol for connections that use Transport Layer Security.
- [class NWProtocolQUIC](nwprotocolquic.md)
  A network protocol for connections that use the QUIC transport protocol.
- [class NWProtocolUDP](nwprotocoludp.md)
  A network protocol for connections that use the User Datagram Protocol.
- [class NWProtocolIP](nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.
### Network Security and Privacy
- [Security Options](security-options.md)
  Configure security options for TLS handshakes.
- [Privacy Management](privacy-management.md)
  Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.
### Paths and Interfaces
- [struct NWPath](nwpath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [class NWPathMonitor](nwpathmonitor.md)
  An observer that you use to monitor and react to network changes.
- [struct NWInterface](nwinterface.md)
  An interface that a network connection uses to send and receive data.
### Errors
- [enum NWError](nwerror.md)
  The errors returned by objects in the Network framework.
### Network Debugging
- [Choosing a Network Debugging Tool](choosing-a-network-debugging-tool.md)
  Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](debugging-http-server-side-errors.md)
  Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](debugging-https-problems-with-cfnetwork-diagnostic-logging.md)
  Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](recording-a-packet-trace.md)
  Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](taking-advantage-of-third-party-network-debugging-tools.md)
  Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](testing-and-debugging-l4s-in-your-app.md)
  Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.
### C-Language Symbols
- [C-Language Symbols](c-language-symbols.md)
### Structures
- [struct nw_interface_radio_type_t](nw_interface_radio_type_t.md)
- [struct nw_multipath_version_t](nw_multipath_version_t.md)
- [struct nw_path_unsatisfied_reason_t](nw_path_unsatisfied_reason_t.md)
- [struct nw_quic_stream_type_t](nw_quic_stream_type_t.md)
- [struct Bonjour](bonjour.md)
  A browser that discovers Bonjour services.
- [struct BonjourListenerProvider](bonjourlistenerprovider.md)
  Advertise a Bonjour service.
- [struct Coder](coder.md)
  A protocol that frames and encodes/decodes Codable types.
- [struct DefaultProtocolStorage](defaultprotocolstorage.md)
- [struct Framer](framer.md)
  An instance of a Framer protocol to load into a protocol stack.
- [struct IP](ip.md)
  The system definition of the Internet Protocol (IP).
- [struct NWParametersBuilder](nwparametersbuilder.md)
  An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.
- [struct NWTXTRecord](nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.
- [struct NetworkJSONCoder](networkjsoncoder.md)
- [struct NetworkPropertyListCoder](networkpropertylistcoder.md)
- [struct ProtocolMetadataBuilder](protocolmetadatabuilder.md)
  A resultBuilder for configuring metadata in send methods in a declarative way.
- [struct ProtocolStackBuilder](protocolstackbuilder.md)
  A resultBuilder for specifying and configuring protocol stacks in a declarative way
- [struct ProxyConfiguration](proxyconfiguration.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- [struct QUIC](quic.md)
  The system definition of the QUIC protocol.
- [struct QUICDatagram](quicdatagram.md)
  Send and receive unreliable datagrams over QUIC via RFC 9221
- [struct QUICStream](quicstream.md)
  A QUIC stream that runs over a QUIC connection.
- [struct TCP](tcp.md)
  The system definition of the Transmission Control Protocol (TCP).
- [struct TLS](tls.md)
  The system definition of the Transport Layer Security (TLS) protocol.
- [struct TLV](tlv.md)
  A Type-Length-Value (TLV) framing protocol.
- [struct TXTRecordDecoder](txtrecorddecoder.md)
- [struct UDP](udp.md)
  The system definition of the User Datagram Protocol (UDP).
- [struct UnexpectedEndpointType](unexpectedendpointtype.md)
  An error generated when an unexpected endpoint type is supplied.
- [struct WebSocket](websocket.md)
  The system definition of the WebSocket protocol.
- [struct nw_link_quality_t](nw_link_quality_t.md)
### Classes
- [class NWMultiplexGroup](nwmultiplexgroup.md)
- [class NetworkBrowser](networkbrowser.md)
  Discover advertised services and devices on the network.
- [class NetworkChannel](networkchannel.md)
  A base class supporting sending and recieving data through an arbitrary network channel.
- [class NetworkConnection](networkconnection.md)
  Connect to an endpoint on the network to send and receive data.
- [class NetworkListener](networklistener.md)
  Listen for incoming network connections.
### Reference
- [Network Constants](network-constants.md)
  Access Network framework constants used in C.
- [Network Functions](network-functions.md)
  Access Network framework functions used in C.
- [Network Data Types](network-data-types.md)
### Protocols
- [protocol BrowserProvider](browserprovider.md)
  BrowserProviders can be used when creating NetworkBrowsers.
- [protocol Connectable](connectable.md)
  Describes types that can be used to make NetworkConnections.
- [protocol ConnectionStorage](connectionstorage.md)
  Types that conform to ConnectionStorage can be used as additional storage within a connection.
- [protocol DatagramProtocol](datagramprotocol.md)
  Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.
- [protocol FramerProtocol](framerprotocol.md)
  Framer protocols allow custom framing and serialization of messages on a connection.
- [protocol ListenerProvider](listenerprovider.md)
  Extensible support for configuring advertise descriptors to define the service a listener should advertise.
- [protocol MessageProtocol](messageprotocol.md)
  Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.
- [protocol MultiplexProtocol](multiplexprotocol.md)
  Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.
- [protocol NWParametersProvider](nwparametersprovider.md)
  Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.
- [protocol NetworkCoder](networkcoder.md)
- [protocol NetworkDecoder](networkdecoder.md)
  A type that conforms to the NetworkEncoder protocol can decode data to an Encodable object
- [protocol NetworkEncoder](networkencoder.md)
  A type that conforms to the NetworkEncoder protocol can encode a Encodable object to Data
- [protocol NetworkFixedWidthInteger](networkfixedwidthinteger.md)
- [protocol NetworkMetadataProtocol](networkmetadataprotocol.md)
  Types that conform to NetworkProtocolOptions can be used when configuring protocol stacks.
- [protocol NetworkProtocolOptions](networkprotocoloptions.md)
- [protocol OneToOneProtocol](onetooneprotocol.md)
  Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.
- [protocol StreamProtocol](streamprotocol.md)
  Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.
### Variables
- [let kNWErrorDomainWiFiAware: CFString](knwerrordomainwifiaware.md)
- [var nw_error_domain_wifi_aware: nw_error_domain_t](nw_error_domain_wifi_aware.md)
- [var nw_link_quality_good: nw_link_quality_t](nw_link_quality_good.md)
- [var nw_link_quality_minimal: nw_link_quality_t](nw_link_quality_minimal.md)
- [var nw_link_quality_moderate: nw_link_quality_t](nw_link_quality_moderate.md)
- [var nw_link_quality_unknown: nw_link_quality_t](nw_link_quality_unknown.md)
### Functions
- [func nw_parameters_get_allow_ultra_constrained(nw_parameters_t) -> Bool](nw_parameters_get_allow_ultra_constrained(_:).md)
- [func nw_parameters_set_allow_ultra_constrained(nw_parameters_t, Bool)](nw_parameters_set_allow_ultra_constrained(_:_:).md)
- [func nw_path_get_link_quality(nw_path_t) -> nw_link_quality_t](nw_path_get_link_quality(_:).md)
- [func nw_path_is_ultra_constrained(nw_path_t) -> Bool](nw_path_is_ultra_constrained(_:).md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](withnetworkconnection(to:using:_:)-1sik8.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](withnetworkconnection(to:using:_:)-4wpc9.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](withnetworkconnection(to:using:_:)-7skhi.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](withnetworkconnection(to:using:_:)-887ho.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network)*