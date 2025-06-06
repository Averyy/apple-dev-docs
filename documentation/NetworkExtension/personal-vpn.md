# Personal VPN

**Framework**: Network Extension

Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).

#### Overview

With the Personal VPN feature in macOS and iOS, your app can create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2). The user must explicitly authorize your app the first time it saves a VPN configuration.

> **Note**:  Personal VPN only supports recommended VPN protocols; it doesn’t support legacy VPN protocols, like PPTP and L2TP.

 Personal VPN only supports recommended VPN protocols; it doesn’t support legacy VPN protocols, like PPTP and L2TP.

Before starting with Personal VPN, verify that the client is compatible with your VPN server. Use Apple Configurator to create a configuration profile with a VPN payload for your server. If you can connect using the VPN configuration from your configuration profile, you should be able to connect using Personal VPN.

To get started, call the [`shared()`](nevpnmanager/shared().md) class method to access the [`NEVPNManager`](nevpnmanager.md) singleton. Then load the VPN configuration by calling [`loadFromPreferences(completionHandler:)`](nevpnmanager/loadfrompreferences(completionhandler:).md); if you haven’t previously saved a configuration, this call returns an empty configuration. Modify this configuration as you see fit, and save it using [`saveToPreferences(completionHandler:)`](nevpnmanager/savetopreferences(completionhandler:).md).

Once you’ve set up a Personal VPN configuration, you can connect and disconnect the VPN using the [`NEVPNConnection`](nevpnconnection.md) class. Use the [`connection`](nevpnmanager/connection.md) property of [`NEVPNManager`](nevpnmanager.md) to get the correct instance of that class.

Both iOS and macOS also support managed VPN, meaning VPN configurations installed by a configuration profile. Managed VPN configurations take precedence over Personal VPN configurations. If there’s simultaneously a managed VPN configuration and Personal VPN configuration, both configured to act as the default route, the managed tunnel serves as the default route.

> **Note**:  When a VPN configuration is active, connections use the VPN instead of iCloud Private Relay. Network Extension providers also don’t use iCloud Private Relay.

 When a VPN configuration is active, connections use the VPN instead of iCloud Private Relay. Network Extension providers also don’t use iCloud Private Relay.

## Topics

### Essentials
- [Personal VPN Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
### VPN configuration
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NEVPNProtocolIKEv2](nevpnprotocolikev2.md)
  Settings for an IKEv2 VPN configuration.
- [class NEVPNProtocolIPSec](nevpnprotocolipsec.md)
  Settings for an IPsec VPN configuration.
- [class NEVPNProtocol](nevpnprotocol.md)
  Settings common to both IKEv2 and IPsec VPN configurations.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.
### VPN control
- [class NEVPNConnection](nevpnconnection.md)
  An object to start and stop a Personal VPN connection and get its status.

## See Also

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)
  Configure your VPN to include and exclude some network traffic.
- [Packet tunnel provider](packet-tunnel-provider.md)
  Implement a VPN client for a packet-oriented, custom VPN protocol.
- [App proxy provider](app-proxy-provider.md)
  Implement a VPN client for a flow-oriented, custom VPN protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/personal-vpn)*