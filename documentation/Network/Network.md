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

- [Inspecting app activity data](inspecting-app-activity-data.md)
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)

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
- [struct BonjourListenerProvider](bonjourlistenerprovider.md)
- [struct Coder](coder.md)
- [struct DefaultProtocolStorage](defaultprotocolstorage.md)
- [struct Framer](framer.md)
- [struct IP](ip.md)
- [struct NWParametersBuilder](nwparametersbuilder.md)
- [struct NWTXTRecord](nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.
- [struct NetworkJSONCoder](networkjsoncoder.md)
- [struct NetworkPropertyListCoder](networkpropertylistcoder.md)
- [struct ProtocolMetadataBuilder](protocolmetadatabuilder.md)
- [struct ProtocolStackBuilder](protocolstackbuilder.md)
- [struct ProxyConfiguration](proxyconfiguration.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- [struct QUIC](quic.md)
  The QUIC type can be used to insert QUIC into a protocol stack. As it conforms to MultiplexProtocol, it exposes configuration a multiplexing instance of QUIC to be used with NetworkConnection, which will in turn expose the ability to handle multiple streams of data over QUIC.
- [struct QUICDatagram](quicdatagram.md)
  QUICDatagram exposes sending unreliable datagrams over QUIC via RFC 9221
- [struct QUICStream](quicstream.md)
  The default QUIC Stream type for Subconnection objects returned from a NetworkConnection over QUIC. Connection’s parameterized over QUICStream will expose a nearly identical stream interface as TCP. This type is not intended to be inserted into the protocol stack manually.
- [struct TCP](tcp.md)
- [struct TLS](tls.md)
- [struct TLV](tlv.md)
- [struct TXTRecordDecoder](txtrecorddecoder.md)
- [struct UDP](udp.md)
- [struct UnexpectedEndpointType](unexpectedendpointtype.md)
- [struct WebSocket](websocket.md)
- [struct nw_link_quality_t](nw_link_quality_t.md)
### Classes
- [class NWMultiplexGroup](nwmultiplexgroup.md)
- [class NetworkBrowser](networkbrowser.md)
- [class NetworkConnection](networkconnection.md)
- [class NetworkListener](networklistener.md)
### Reference
- [Network Constants](network-constants.md)
  Access Network framework constants used in C.
- [Network Functions](network-functions.md)
  Access Network framework functions used in C.
- [Network Data Types](network-data-types.md)
### Protocols
- [protocol BrowserProvider](browserprovider.md)
- [protocol Connectable](connectable.md)
- [protocol ConnectionProtocol](connectionprotocol.md)
- [protocol ConnectionStorage](connectionstorage.md)
  Types that conform to ConnectionStorage can be used as additional storage within a NetworkConnection
- [protocol DatagramProtocol](datagramprotocol.md)
- [protocol FramerProtocol](framerprotocol.md)
- [protocol ListenerProvider](listenerprovider.md)
- [protocol MessageProtocol](messageprotocol.md)
- [protocol MultiplexProtocol](multiplexprotocol.md)
  Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects. Generally network protocols conforming to this will not directly expose send or receive methods. Instead, they usually expose methods to open and listen for multiplexed Subconnections which can be sent and received on
- [protocol NWParametersProvider](nwparametersprovider.md)
- [protocol NetworkCoder](networkcoder.md)
- [protocol NetworkDecoder](networkdecoder.md)
- [protocol NetworkEncoder](networkencoder.md)
- [protocol NetworkFixedWidthInteger](networkfixedwidthinteger.md)
- [protocol NetworkMetadataProtocol](networkmetadataprotocol.md)
- [protocol NetworkProtocolOptions](networkprotocoloptions.md)
- [protocol OneToOneProtocol](onetooneprotocol.md)
  Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for standard, non-multiplexed Connections
- [protocol StreamProtocol](streamprotocol.md)
- [protocol SubConnectionProtocol](subconnectionprotocol.md)
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
### Enumerations
- [enum AdvertisedRoute](advertisedroute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network)*