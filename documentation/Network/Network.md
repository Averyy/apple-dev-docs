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
- [struct NWTXTRecord](nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.
- [struct ProxyConfiguration](proxyconfiguration.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
### Classes
- [class NWMultiplexGroup](nwmultiplexgroup.md)
### Reference
- [Network Constants](network-constants.md)
  Access Network framework constants used in C.
- [Network Functions](network-functions.md)
  Access Network framework functions used in C.
- [Network Data Types](network-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Network)*