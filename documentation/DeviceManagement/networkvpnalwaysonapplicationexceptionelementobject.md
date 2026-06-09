# NetworkVPNAlwaysOnApplicationExceptionElementObject

**Framework**: Device Management  
**Kind**: dictionary

An array that contains an arbitrary number of apps whose connections occur outside the VPN.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnApplicationExceptionElementObject
```

## Properties

- `BundleIdentifier` (string) *(required)*: The app’s bundle identifier.
- `LimitToProtocols` ([string]): Limit the exception to only the specified list of protocols, with support for `UDP` only.

## See Also

- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnDNSObject](networkvpnalwaysondnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNAlwaysOnProxiesObject](networkvpnalwaysonproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNAlwaysOnServiceExceptionElementObject](networkvpnalwaysonserviceexceptionelementobject.md)
  An array that contains an arbitrary number of service exceptions.
- [object NetworkVPNAlwaysOnTunnelConfigurationElementObject](networkvpnalwaysontunnelconfigurationelementobject.md)
  An array that contains an arbitrary number of tunnel configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonapplicationexceptionelementobject)*