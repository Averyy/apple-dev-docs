# NetworkVPNVPNPluginOnDemandObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system controls on-demand VPN.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginOnDemandObject
```

## Topics

### Objects
- [object NetworkVPNVPNPluginRulesElementObject](networkvpnvpnpluginruleselementobject.md)
  An array of dictionaries defining On Demand Rules.

## Properties

- `DisableUserOverride` (boolean): If `true`, the Connect On Demand toggle in Settings is disabled for this configuration. Available: iOS 27+ | iPadOS 27+ | tvOS 27+ | visionOS 27+
- `Enabled` (boolean): If `true`, enables VPN On Demand.
- `Rules` ([NetworkVPNVPNPluginRulesElementObject]): An array of dictionaries defining On Demand Rules.

## See Also

- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNVPNPluginDNSObject](networkvpnvpnplugindnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNVPNPluginIdleObject](networkvpnvpnpluginidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNVPNPluginNetworkRoutingObject](networkvpnvpnpluginnetworkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNVPNPluginProviderObject](networkvpnvpnpluginproviderobject.md)
  Specifies details about the provider.
- [object NetworkVPNVPNPluginProxiesObject](networkvpnvpnpluginproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginondemandobject)*