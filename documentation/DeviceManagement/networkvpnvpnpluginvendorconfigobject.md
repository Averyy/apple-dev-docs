# NetworkVPNVPNPluginVendorConfigObject

**Framework**: Device Management  
**Kind**: dictionary

The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginVendorConfigObject
```

## Properties

- `Group` (string): The group to connect to on the head end. Valid for Cisco AnyConnect and Cisco Legacy AnyConnect.
- `LoginGroupOrDomain` (string): The login group or domain. Valid only for SonicWALL Mobile Connect.
- `Realm` (string): The Kerberos realm name, which needs to be properly capitalized. Valid only for Juniper SSL and Pulse Secure.
- `Role` (string): The role to select when connecting to the server. Valid only for Juniper SSL and Pulse Secure.

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
- [object NetworkVPNVPNPluginProxiesObject](networkvpnvpnpluginproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginvendorconfigobject)*