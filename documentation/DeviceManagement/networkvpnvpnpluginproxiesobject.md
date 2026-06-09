# NetworkVPNVPNPluginProxiesObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginProxiesObject
```

## Topics

### Objects
- [object NetworkVPNVPNPluginProxies_ProtocolObject](networkvpnvpnpluginproxies_protocolobject.md)
  The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

## Properties

- `AutoConfigEnable` (boolean): If `true`, enables automatic proxy configuration.
- `AutoConfigURLString` (string): The URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is `true`.
- `AutoDiscoveryEnable` (boolean): If `true`, enables proxy auto discovery.
- `Protocol` (NetworkVPNVPNPluginProxies_ProtocolObject): The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.
- `SupplementalMatchDomains` ([string]): An array of domains that defines which hosts use proxy settings for hosts.

## See Also

- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNVPNPluginDNSObject](networkvpnvpnplugindnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNVPNPluginIdleObject](networkvpnvpnpluginidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNVPNPluginNetworkRoutingObject](networkvpnvpnpluginnetworkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNVPNPluginOnDemandObject](networkvpnvpnpluginondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNVPNPluginProviderObject](networkvpnvpnpluginproviderobject.md)
  Specifies details about the provider.
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginproxiesobject)*