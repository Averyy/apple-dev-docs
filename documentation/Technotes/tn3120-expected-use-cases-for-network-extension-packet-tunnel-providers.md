# TN3120: Expected use cases for Network Extension packet tunnel providers

**Framework**: Technotes  
**Role**: Technote

Learn the expected use cases for Network Extension packet tunnel providers, and about use cases that are not supported.

## Overview

[`NEPacketTunnelProvider`](../NetworkExtension/nepackettunnelprovider.md) is very powerful and useful on Apple platforms. It has many valid use cases such as providing users access to secure resources and securing network traffic on an insecure network. While this API is very powerful, there are certain use cases that do not line up with its intended purpose. This technote briefly explains the recommended use cases for packet tunnel providers, along with common scenarios that are unsupported.

## Recommended use cases for packet tunnel providers

Recommended use cases for a packet tunnel provider include:

- Do use a packet tunnel provider to access secure resources on an isolated network. For example, use `NEPacketTunnelProvider` to implement an iOS or macOS VPN client that tunnels network traffic through a VPN connection into a private enterprise network. This can be done by tunneling specific destination IP and DNS traffic to the isolated network.
- Do use a packet tunnel provider to secure network access while on an insecure network.  For example, use `NEPacketTunnelProvider` to implement an iOS or macOS VPN client that tunnels network traffic through a public VPN service that provides access to the wider internet.  Common techniques used to achieve this functionality include creating a full tunnel VPN that routes all traffic to the remote VPN server that then forwards the traffic to its final destination.

## Unsupported uses of packet tunnel providers

While there are many reasons to use a packet tunnel provider, there are also many unsupported uses of this API. If you find yourself implementing any one of the code paths below, consider using one of the suggested alternatives:

- Do not use a packet tunnel provider to implement a network content filter. Packets that are read from [`NEPacketTunnelFlow`](../NetworkExtension/nepackettunnelflow.md) are meant to be sent over a tunnel connection to a remote server for injection into a remote network. They are not meant to be dropped or re-injected back into the system. Doing so is a content filter action, as supported by one of the Network Extension [Content filter providers](../NetworkExtension/content-filter-providers.md). On iOS, implement a connection-based content filter using [`NEFilterDataProvider`](../NetworkExtension/nefilterdataprovider.md) and [`NEFilterControlProvider`](../NetworkExtension/nefiltercontrolprovider.md). On macOS, implement a connection-based content filter with `NEFilterDataProvider` or a packet-based content filter with [`NEFilterPacketProvider`](../NetworkExtension/nefilterpacketprovider.md). On macOS, using both providers at the same time is supported.

  For information on how to deploy a content filter, see [TN3134: Network Extension provider deployment](./tn3134-network-extension-provider-deployment.md).  If those options don’t work for your product, consider creating a [URL filter](../NetworkExtension/url-filters.md).
- Do not use a packet tunnel provider to intercept all DNS traffic on the system.
  For small sets of DNS traffic inside your isolated network, this is reasonable. However, trying to intercept all DNS traffic on the system can result in endless edge cases and problems during development and deployment. As an alternative use the [`NEDNSProxyProvider`](../NetworkExtension/nednsproxyprovider.md) or the [DNS settings](../NetworkExtension/dns-settings.md) APIs.  These APIs were built for handling all DNS traffic on the system.
- Do not use a packet tunnel provider to selectively claim traffic for the packet tunnel and proxy all other traffic elsewhere. Traffic that is claimed by a `NEPacketTunnelProvider` is meant to be sent through the tunnel connection and not be routed through another interface via a proxy.  The recommended alternative is to implement a [`NETransparentProxyProvider`](../NetworkExtension/netransparentproxyprovider.md) on macOS.  On iOS, consider either claiming the network traffic that’s needed for your tunnel with [per-app VPN](../NetworkExtension/netunnelprovidermanager.md) or claiming traffic by destination IP with [`includedRoutes`](../NetworkExtension/neipv4settings/includedroutes.md).  To learn more about how the system routes VPN traffic, see [Routing your VPN network traffic](../NetworkExtension/routing-your-vpn-network-traffic.md).
- Do not use a packet tunnel provider to host a network listener or proxy server.
  There is no reasonable alternative here other than using one of the [App proxy provider](../NetworkExtension/app-proxy-provider.md) APIs.  This path is simply not a recommended use case for a packet tunnel provider or any other Network Extension.

Avoiding the unsupported scenarios will save your project many edges cases and bugs during the development and deployment process.

## Revision History

- **2025-07-22** Added a reference to the new [URL filters](../NetworkExtension/url-filters.md) mechanism.  Added links to documents that further explain specific topics.  Fixed a broken link.  Made other minor editorial changes.
- **2022-05-24** Made minor editorial changes.
- **2022-03-29** Added additional links to APIs.
- **2022-03-22** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers)*