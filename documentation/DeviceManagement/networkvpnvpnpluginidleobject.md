# NetworkVPNVPNPluginIdleObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system handles idle VPN connections.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginIdleObject
```

## Properties

- `Disconnect` (boolean): If `true`, disconnects after an on-demand connection idles.
- `Timer` (integer): The length of time to wait, in seconds, before disconnecting an on-demand connection.

## See Also

- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNVPNPluginDNSObject](networkvpnvpnplugindnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNVPNPluginNetworkRoutingObject](networkvpnvpnpluginnetworkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNVPNPluginOnDemandObject](networkvpnvpnpluginondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNVPNPluginProviderObject](networkvpnvpnpluginproviderobject.md)
  Specifies details about the provider.
- [object NetworkVPNVPNPluginProxiesObject](networkvpnvpnpluginproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginidleobject)*