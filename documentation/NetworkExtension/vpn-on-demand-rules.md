# VPN On Demand Rules

**Framework**: Network Extension

Set up VPN On Demand.

#### Overview

VPN On Demand allows the system to automatically start or stop a VPN connection based on various criteria. For example, you can use VPN On Demand to configure an iPhone to start a VPN connection when it’s on Wi-Fi and stop the connection when it’s on cellular. Or, you can start the VPN connection when an app tries to connect to a specific service that’s only available via VPN.

For more information, see “VPN On Demand” in [`Apple Platform Deployment Guide`](https://developer.apple.comhttps://support.apple.com/guide/deployment/welcome/web).

## Topics

### Settings
- [class NEOnDemandRuleConnect](neondemandruleconnect.md)
  A VPN On Demand rule that connects the VPN.
- [class NEOnDemandRuleDisconnect](neondemandruledisconnect.md)
  A VPN On Demand rule that disconnects the VPN.
- [class NEOnDemandRuleIgnore](neondemandruleignore.md)
  A VPN On Demand rule that doesn’t change the status of the VPN.
- [class NEOnDemandRuleEvaluateConnection](neondemandruleevaluateconnection.md)
  A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.
- [class NEOnDemandRule](neondemandrule.md)
  A base class shared by all VPN On Demand rules.

## See Also

- [Personal VPN](personal-vpn.md)
  Create and manage a VPN configuration that uses one of the built-in VPN protocols (IPsec or IKEv2).
- [Packet tunnel provider](packet-tunnel-provider.md)
  Implement a VPN client for a packet-oriented, custom VPN protocol.
- [App proxy provider](app-proxy-provider.md)
  Implement a VPN client for a flow-oriented, custom VPN protocol.
- [class NEAppProxyProviderManager](neappproxyprovidermanager.md)
  An object to create and manage the app proxy provider’s VPN configuration.
- [class NETunnelProviderManager](netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [class NEAppRule](neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/vpn-on-demand-rules)*