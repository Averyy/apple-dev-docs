# NetworkVPNVPNPluginNetworkRoutingObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the VPN routes different types of network traffic.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginNetworkRoutingObject
```

## Properties

- `EnforceRoutes` (boolean): If `true`, all the VPN’s non-default routes take precedence over any locally defined routes. If `IncludeAllNetworks` is `true`, the system ignores the value of `EnforceRoutes`.
- `ExcludeAPNs` (boolean): If `true` and `IncludeAllNetworks` is `true`, then the system excludes the network traffic for the Apple Push Notification service (APNs) from the tunnel.
- `ExcludeCellularServices` (boolean): If `true` and `IncludeAllNetworks` is `true`, then the system excludes internet-routable network traffic for cellular services (VoLTE, Wi-Fi Calling, IMS, MMS, Visual Voicemail, etc.) from the tunnel. Note that some cellular carriers route cellular services traffic directly to the carrier network, bypassing the internet. Such cellular services traffic is always excluded from the tunnel.
- `ExcludeDeviceCommunication` (boolean): If set to `true` and `IncludeAllNetworks` is set to `true`, the device excludes network traffic used for communicating with devices connected via USB or Wi-Fi from the tunnel.
- `ExcludeLocalNetworks` (boolean): If `true` and `IncludeAllNetworks` is `true`, routes all local network traffic outside the VPN.
- `IncludeAllNetworks` (boolean): If `true`, routes all traffic through the VPN, with some exclusions. Several of the exclusions can be controlled with the `ExcludeLocalNetworks`, `ExcludeCellularServices`, `ExcludeAPNs` and `ExcludeDeviceCommunication` properties. The following traffic is always excluded from the tunnel: - Traffic necessary for connecting and maintaining the device’s network connection, such as DHCP.
- Traffic necessary for connecting to captive networks.
- Certain cellular services traffic that’s not routable over the internet and is instead directly routed to the cellular network. See the ExcludeCellularServices property for more details.

## See Also

- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNVPNPluginDNSObject](networkvpnvpnplugindnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNVPNPluginIdleObject](networkvpnvpnpluginidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNVPNPluginOnDemandObject](networkvpnvpnpluginondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNVPNPluginProviderObject](networkvpnvpnpluginproviderobject.md)
  Specifies details about the provider.
- [object NetworkVPNVPNPluginProxiesObject](networkvpnvpnpluginproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginnetworkroutingobject)*