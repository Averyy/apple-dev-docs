# NetworkVPNAlwaysOnProxiesObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnProxiesObject
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnProxies_ProtocolObject](networkvpnalwaysonproxies_protocolobject.md)
  The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

## Properties

- `AutoConfigEnable` (boolean): If `true`, enables automatic proxy configuration.
- `AutoConfigURLString` (string): The URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is `true`.
- `AutoDiscoveryEnable` (boolean): If `true`, enables proxy auto discovery.
- `Protocol` (NetworkVPNAlwaysOnProxies_ProtocolObject): The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.
- `SupplementalMatchDomains` ([string]): An array of domains that defines which hosts use proxy settings for hosts.

## See Also

- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnApplicationExceptionElementObject](networkvpnalwaysonapplicationexceptionelementobject.md)
  An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- [object NetworkVPNAlwaysOnDNSObject](networkvpnalwaysondnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNAlwaysOnServiceExceptionElementObject](networkvpnalwaysonserviceexceptionelementobject.md)
  An array that contains an arbitrary number of service exceptions.
- [object NetworkVPNAlwaysOnTunnelConfigurationElementObject](networkvpnalwaysontunnelconfigurationelementobject.md)
  An array that contains an arbitrary number of tunnel configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonproxiesobject)*