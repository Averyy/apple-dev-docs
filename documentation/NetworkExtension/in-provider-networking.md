# In-Provider Networking

**Framework**: Network Extension

Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.

#### Overview

NetworkExtension providers and hotspot helpers run in an unusual network environment that can cause problems for general-purpose networking APIs. For example, [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) typically sends requests via the default route, which is inappropriate for a hotspot helper that must always use the Wi-Fi interface. The NetworkExtension framework includes a number of APIs that are useful in such situations.

These APIs have the following key characteristics:

- They aren’t general-purpose APIs; they can only be used in the context of a NetworkExtension provider or hotspot helper.
- In many cases, you don’t need to use them. For example, it’s possible for a packet tunnel provider to use a general-purpose networking API, like BSD Sockets, for its tunnel connection.

The recommended general-purpose networking APIs are the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system) for HTTP and the [`Network`](https://developer.apple.com/documentation/Network) framework for TCP and UDP.

## Topics

### TCP connections
- [class NWTCPConnection](nwtcpconnection.md)
  An object to manage a TCP connection, with or without TLS.
- [class NWTLSParameters](nwtlsparameters.md)
  TLS properties for creating a connection.
- [protocol NWTCPConnectionAuthenticationDelegate](nwtcpconnectionauthenticationdelegate.md)
  A delegate protocol to customize the TLS authentication done by a connection.
### UDP sessions
- [class NWUDPSession](nwudpsession.md)
  An object to manage a UDP session to a network endpoint.
### Endpoints
- [class NWHostEndpoint](nwhostendpoint.md)
  A network endpoint specified by DNS name (or IP address) and port.
- [class NWBonjourServiceEndpoint](nwbonjourserviceendpoint.md)
  A network endpoint specified as a Bonjour service name, type, and domain.
- [class NWEndpoint](nwendpoint.md)
  An abstract base class, shared by [`NWHostEndpoint`](nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.
### Network path information
- [class NWPath](nwpath.md)
  The path made by a network connection, including information about its viability.

## See Also

- [Packet tunnel provider](packet-tunnel-provider.md)
  Implement a VPN client for a packet-oriented, custom VPN protocol.
- [App proxy provider](app-proxy-provider.md)
  Implement a VPN client for a flow-oriented, custom VPN protocol.
- [Hotspot helper](hotspot-helper.md)
  Integrate your app with the iOS hotspot network subsystem.
- [class NEAppProxyTCPFlow](neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [class NEFlowMetaData](neflowmetadata.md)
  Additional information about data flowing through a per-app VPN provider.
- [Handling Flow Copying](handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/in-provider-networking)*