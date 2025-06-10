# Packet tunnel provider

**Framework**: Network Extension

Implement a VPN client for a packet-oriented, custom VPN protocol.

#### Overview

A virtual private network (VPN) is a form of network tunnel where a VPN client uses the public Internet to create a connection to a VPN server and then passes private network traffic over that connection. If you want to build a VPN client that implements a packet-oriented, custom VPN protocol, create a packet tunnel provider app extension.

When the system starts a VPN configuration that uses your packet tunnel provider, it performs the following steps:

- Launches your app extension.
- Instantiates your packet tunnel provider subclass within that app extension.
- Starts forwarding packets to your provider.

Your provider should open a tunnel to a VPN server and send those packets over that tunnel. Similarly, if your provider receives packets from the tunnel, it should pass them back to the system.

Packet tunnel providers can run in destination IP mode or source-application mode. The latter is one form of per-app VPN (the other form is an [`App proxy provider`](app-proxy-provider.md)).

For detailed information about packet tunnel provider deployment options, see [`TN3134: Network Extension provider deployment`](https://developer.apple.com/documentation/Technotes/tn3134-network-extension-provider-deployment).

> **Note**:  When a VPN configuration is active, connections use the VPN instead of iCloud Private Relay. Network Extension providers also don’t use iCloud Private Relay.

## Topics

### Essentials
- [Network Extensions Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
### Packet tunnel provider
- [class NEPacketTunnelProvider](nepackettunnelprovider.md)
  The principal class for a packet tunnel provider app extension.
- [class NETunnelProvider](netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NEProvider](neprovider.md)
  An abstract base class for all NetworkExtension providers.
- [class NEPacketTunnelNetworkSettings](nepackettunnelnetworksettings.md)
  The configuration for a packet tunnel provider’s virtual interface.
- [class NETunnelNetworkSettings](netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.
- [class NEEthernetTunnelProvider](neethernettunnelprovider.md)
  A type that implements the client side of a custom link-layer packet tunneling protocol.
- [class NEEthernetTunnelNetworkSettings](neethernettunnelnetworksettings.md)
  The network settings for an ethernet-based VPN tunnel.
### Packet handling
- [class NEPacketTunnelFlow](nepackettunnelflow.md)
  An object you use to read and write packets to and from the tunnel’s virtual interface.
- [class NEPacket](nepacket.md)
  A network packet and its associated properties.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
### VPN configuration
- [class NETunnelProviderManager](netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [class NEAppRule](neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.
### VPN control
- [class NETunnelProviderSession](netunnelprovidersession.md)
  An object to start and stop a tunnel connection and get its status.
- [class NEVPNConnection](nevpnconnection.md)
  An object to start and stop a Personal VPN connection and get its status.

## See Also

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)
  Configure your VPN to include and exclude some network traffic.
- [Personal VPN](personal-vpn.md)
  Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- [App proxy provider](app-proxy-provider.md)
  Implement a VPN client for a flow-oriented, custom VPN protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider)*