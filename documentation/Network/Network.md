# Network

**Framework**: Network  
**Kind**: module  
**Role**: Framework

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

- [Indicating the source of network activity](./indicating-the-source-of-network-activity.md)
- [Inspecting app activity data](./inspecting-app-activity-data.md)

## Overview

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use [`URLSession`](../Foundation/urlsession.md), which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see [TN3151: Choosing the right networking API](../Technotes/tn3151-choosing-the-right-networking-api.md).

> **Note**:  watchOS supports Network framework for specific use cases. For more details, see [TN3135: Low-level networking on watchOS](../Technotes/tn3135-low-level-networking-on-watchos.md).

## Topics

### Essentials
- [enum NWEndpoint](./nwendpoint.md)
  A local or remote endpoint in a network connection.
- [class NWParameters](./nwparameters.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [nw_endpoint_t](./nw_endpoint_t.md)
  A local or remote endpoint in a network connection.
- [nw_parameters_t](./nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
### Connections and Listeners
- [class NWConnection](./nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWListener](./nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWBrowser](./nwbrowser.md)
  An object you use to browse for available network services.
- [class NWConnectionGroup](./nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [class NWEthernetChannel](./nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.
- [Implementing netcat with Network Framework](./implementing-netcat-with-network-framework.md)
  Build a simple `netcat` tool that establishes network connections and transfers data.
- [nw_connection_t](./nw_connection_t.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [nw_listener_t](./nw_listener_t.md)
  An object you use to listen for incoming network connections.
- [nw_browser_t](./nw_browser_t.md)
  An object you use to browse for available network services.
- [nw_connection_group_t](./nw_connection_group_t.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [nw_ethernet_channel_t](./nw_ethernet_channel_t.md)
  An object you use to send and receive custom Ethernet frames.
### Network Protocols
- [Building a custom peer-to-peer protocol](./building-a-custom-peer-to-peer-protocol.md)
  Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](../visionOS/connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.
- [class NWProtocolTCP](./nwprotocoltcp.md)
  A network protocol for connections that use the Transmission Control Protocol.
- [class NWProtocolTLS](./nwprotocoltls.md)
  A network protocol for connections that use Transport Layer Security.
- [class NWProtocolQUIC](./nwprotocolquic.md)
  A network protocol for connections that use the QUIC transport protocol.
- [class NWProtocolUDP](./nwprotocoludp.md)
  A network protocol for connections that use the User Datagram Protocol.
- [class NWProtocolIP](./nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](./nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.
- [class NWProtocolFramer](./nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.
- [TCP Options](./tcp-options.md)
  Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](./tls-options.md)
  Configure options for connections that use Transport Layer Security.
- [QUIC Options](./quic-options.md)
  Configure options for connections that use the QUIC transport protocol.
- [UDP Options](./udp-options.md)
  Configure options for connections that use the User Datagram Protocol.
- [IP Options](./ip-options.md)
  Configure Internet Protocol options on connections.
- [WebSocket Options](./websocket-options.md)
  Configure options for connections that use WebSocket.
- [Framer Protocol Options](./framer-protocol-options.md)
  Create custom protocols to frame applications messages over a connection.
### Network Security and Privacy
- [Security Options](./security-options.md)
  Configure security options for TLS handshakes.
- [Privacy Management](./privacy-management.md)
  Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](./creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.
### Paths and Interfaces
- [struct NWPath](./nwpath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [class NWPathMonitor](./nwpathmonitor.md)
  An observer that you use to monitor and react to network changes.
- [struct NWInterface](./nwinterface.md)
  An interface that a network connection uses to send and receive data.
- [nw_path_t](./nw_path_t.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [nw_path_monitor_t](./nw_path_monitor_t.md)
  An observer that you use to monitor and react to network changes.
- [nw_interface_t](./nw_interface_t.md)
  An interface that a network connection uses to send and receive data.
### Errors
- [enum NWError](./nwerror.md)
  The errors returned by objects in the Network framework.
- [nw_error_t](./nw_error_t.md)
  The errors returned by the Network framework.
### Network Debugging
- [Choosing a Network Debugging Tool](./choosing-a-network-debugging-tool.md)
  Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](./debugging-http-server-side-errors.md)
  Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](./debugging-https-problems-with-cfnetwork-diagnostic-logging.md)
  Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](./recording-a-packet-trace.md)
  Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](./taking-advantage-of-third-party-network-debugging-tools.md)
  Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](./testing-and-debugging-l4s-in-your-app.md)
  Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.
### C-Language Symbols
- [C-Language Symbols](./c-language-symbols.md)
### Structures
- [struct nw_interface_radio_type_t](./nw_interface_radio_type_t.md)
- [struct nw_multipath_version_t](./nw_multipath_version_t.md)
- [struct nw_path_unsatisfied_reason_t](./nw_path_unsatisfied_reason_t.md)
- [struct nw_quic_stream_type_t](./nw_quic_stream_type_t.md)
- [struct Bonjour](./bonjour.md)
  A browser that discovers Bonjour services.
- [struct BonjourListenerProvider](./bonjourlistenerprovider.md)
  Advertise a Bonjour service.
- [struct Coder](./coder.md)
  A protocol that frames and encodes/decodes Codable types.
- [struct DTLS](./dtls.md)
  The system definition of the Datagram Transport Layer Security (DTLS) protocol.
- [struct DefaultProtocolStorage](./defaultprotocolstorage.md)
- [struct Framer](./framer.md)
  An instance of a Framer protocol to load into a protocol stack.
- [struct IP](./ip.md)
  The system definition of the Internet Protocol (IP).
- [struct NWParametersBuilder](./nwparametersbuilder.md)
  An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.
- [struct NWTXTRecord](./nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.
- [struct NetworkJSONCoder](./networkjsoncoder.md)
- [struct NetworkPropertyListCoder](./networkpropertylistcoder.md)
- [struct ProtocolMetadataBuilder](./protocolmetadatabuilder.md)
  A resultBuilder for configuring metadata in send methods in a declarative way.
- [struct ProtocolStackBuilder](./protocolstackbuilder.md)
  A resultBuilder for specifying and configuring protocol stacks in a declarative way
- [struct ProxyConfiguration](./proxyconfiguration.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- [struct QUIC](./quic.md)
  The system definition of the QUIC protocol.
- [struct QUICDatagram](./quicdatagram.md)
  Send and receive unreliable datagrams over QUIC via RFC 9221
- [struct QUICStream](./quicstream.md)
  A QUIC stream that runs over a QUIC connection.
- [struct TCP](./tcp.md)
  The system definition of the Transmission Control Protocol (TCP).
- [struct TLS](./tls.md)
  The system definition of the Transport Layer Security (TLS) protocol.
- [struct TLV](./tlv.md)
  A Type-Length-Value (TLV) framing protocol.
- [struct TXTRecordDecoder](./txtrecorddecoder.md)
- [struct UDP](./udp.md)
  The system definition of the User Datagram Protocol (UDP).
- [struct UnexpectedEndpointType](./unexpectedendpointtype.md)
  An error generated when an unexpected endpoint type is supplied.
- [struct WebSocket](./websocket.md)
  The system definition of the WebSocket protocol.
- [struct nw_link_quality_t](./nw_link_quality_t.md)
### Classes
- [class NWMultiplexGroup](./nwmultiplexgroup.md)
- [class NetworkBrowser](./networkbrowser.md)
  Discover advertised services and devices on the network.
- [class NetworkChannel](./networkchannel.md)
  A base class supporting sending and recieving data through an arbitrary network channel.
- [class NetworkConnection](./networkconnection.md)
  Connect to an endpoint on the network to send and receive data.
- [class NetworkListener](./networklistener.md)
  Listen for incoming network connections.
### Reference
- [Network Constants](./network-constants.md)
  Access Network framework constants used in C.
- [Network Functions](./network-functions.md)
  Access Network framework functions used in C.
- [Network Data Types](./network-data-types.md)
- [Network Enumerations](./network-enumerations.md)
- [Network Macros](./network-macros.md)
### Protocols
- [protocol BrowserProvider](./browserprovider.md)
  BrowserProviders can be used when creating NetworkBrowsers.
- [protocol Connectable](./connectable.md)
  Describes types that can be used to make NetworkConnections.
- [protocol ConnectionStorage](./connectionstorage.md)
  Types that conform to ConnectionStorage can be used as additional storage within a connection.
- [protocol DatagramProtocol](./datagramprotocol.md)
  Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.
- [protocol FramerProtocol](./framerprotocol.md)
  Framer protocols allow custom framing and serialization of messages on a connection.
- [protocol ListenerProvider](./listenerprovider.md)
  Extensible support for configuring advertise descriptors to define the service a listener should advertise.
- [protocol MessageProtocol](./messageprotocol.md)
  Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.
- [protocol MultiplexProtocol](./multiplexprotocol.md)
  Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.
- [protocol NWParametersProvider](./nwparametersprovider.md)
  Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.
- [protocol NetworkCoder](./networkcoder.md)
- [protocol NetworkDecoder](./networkdecoder.md)
  A type that conforms to the NetworkEncoder protocol can decode data to an Encodable object
- [protocol NetworkEncoder](./networkencoder.md)
  A type that conforms to the NetworkEncoder protocol can encode a Encodable object to Data
- [protocol NetworkFixedWidthInteger](./networkfixedwidthinteger.md)
- [protocol NetworkMetadataProtocol](./networkmetadataprotocol.md)
  Types that conform to NetworkProtocolOptions can be used when configuring protocol stacks.
- [protocol NetworkProtocolOptions](./networkprotocoloptions.md)
- [protocol OneToOneProtocol](./onetooneprotocol.md)
  Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.
- [protocol StreamProtocol](./streamprotocol.md)
  Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.
- [OS_nw_advertise_descriptor](./os_nw_advertise_descriptor.md)
- [OS_nw_browse_descriptor](./os_nw_browse_descriptor.md)
- [OS_nw_browse_result](./os_nw_browse_result.md)
- [OS_nw_browser](./os_nw_browser.md)
- [OS_nw_connection](./os_nw_connection.md)
- [OS_nw_connection_group](./os_nw_connection_group.md)
- [OS_nw_content_context](./os_nw_content_context.md)
- [OS_nw_data_transfer_report](./os_nw_data_transfer_report.md)
- [OS_nw_endpoint](./os_nw_endpoint.md)
- [OS_nw_error](./os_nw_error.md)
- [OS_nw_establishment_report](./os_nw_establishment_report.md)
- [OS_nw_ethernet_channel](./os_nw_ethernet_channel.md)
- [OS_nw_framer](./os_nw_framer.md)
- [OS_nw_group_descriptor](./os_nw_group_descriptor.md)
- [OS_nw_interface](./os_nw_interface.md)
- [OS_nw_listener](./os_nw_listener.md)
- [OS_nw_object](./os_nw_object.md)
- [OS_nw_parameters](./os_nw_parameters.md)
- [OS_nw_path](./os_nw_path.md)
- [OS_nw_path_monitor](./os_nw_path_monitor.md)
- [OS_nw_privacy_context](./os_nw_privacy_context.md)
- [OS_nw_protocol_definition](./os_nw_protocol_definition.md)
- [OS_nw_protocol_metadata](./os_nw_protocol_metadata.md)
- [OS_nw_protocol_options](./os_nw_protocol_options.md)
- [OS_nw_protocol_stack](./os_nw_protocol_stack.md)
- [OS_nw_proxy_config](./os_nw_proxy_config.md)
- [OS_nw_relay_hop](./os_nw_relay_hop.md)
- [OS_nw_resolution_report](./os_nw_resolution_report.md)
- [OS_nw_resolver_config](./os_nw_resolver_config.md)
- [OS_nw_txt_record](./os_nw_txt_record.md)
- [OS_nw_ws_request](./os_nw_ws_request.md)
- [OS_nw_ws_response](./os_nw_ws_response.md)
### Variables
- [let kNWErrorDomainWiFiAware: CFString](./knwerrordomainwifiaware.md)
- [var nw_error_domain_wifi_aware: nw_error_domain_t](./nw_error_domain_wifi_aware.md)
- [var nw_link_quality_good: nw_link_quality_t](./nw_link_quality_good.md)
- [var nw_link_quality_minimal: nw_link_quality_t](./nw_link_quality_minimal.md)
- [var nw_link_quality_moderate: nw_link_quality_t](./nw_link_quality_moderate.md)
- [var nw_link_quality_unknown: nw_link_quality_t](./nw_link_quality_unknown.md)
### Functions
- [func nw_parameters_get_allow_ultra_constrained(nw_parameters_t) -> Bool](./nw_parameters_get_allow_ultra_constrained%28_%29.md)
- [func nw_parameters_set_allow_ultra_constrained(nw_parameters_t, Bool)](./nw_parameters_set_allow_ultra_constrained%28_,_%29.md)
- [func nw_path_get_link_quality(nw_path_t) -> nw_link_quality_t](./nw_path_get_link_quality%28_%29.md)
- [func nw_path_is_ultra_constrained(nw_path_t) -> Bool](./nw_path_is_ultra_constrained%28_%29.md)
- [func nw_tcp_set_max_pacing_rate(nw_protocol_metadata_t, UInt64) -> Int32](./nw_tcp_set_max_pacing_rate%28_,_%29.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](./withnetworkconnection%28to,using,_%29-1sik8.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: () -> ApplicationProtocol, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](./withnetworkconnection%28to,using,_%29-4wpc9.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](./withnetworkconnection%28to,using,_%29-7skhi.md)
- [func withNetworkConnection<ApplicationProtocol>(to: NWEndpoint, using: NWParametersBuilder<ApplicationProtocol>, (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws](./withnetworkconnection%28to,using,_%29-887ho.md)
### Memory Management
- [nw_release](./nw_release.md)
  Releases a reference count on a Network.framework object.
- [nw_retain](./nw_retain.md)
  Adds a reference count to a Network.framework object.
- [nw_object_t](./nw_object_t.md)
  The generic type for objects in the Network framework.
### Macros
- [NW_ASSUME_EXTERNALLY_RETAINED_BEGIN](./nw_assume_externally_retained_begin.md)
- [NW_ASSUME_EXTERNALLY_RETAINED_END](./nw_assume_externally_retained_end.md)
- [NW_EXPORT](./nw_export.md)
- [NW_EXTERNALLY_RETAINED](./nw_externally_retained.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network)*