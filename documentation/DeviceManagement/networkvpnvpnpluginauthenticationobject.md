# NetworkVPNVPNPluginAuthenticationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control authentication.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginAuthenticationObject
```

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the VPN server. Required when `Authentication.Method` is set to `Password`.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that this account requires to authenticate with the VPN server. Required when `Authentication.Method` is set to `Certificate`.
- `Method` (string) *(required)*: The authentication method to use.

## See Also

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
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginauthenticationobject)*