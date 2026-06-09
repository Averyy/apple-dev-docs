# NetworkVPNIPSecProxiesObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecProxiesObject
```

## Topics

### Objects
- [object NetworkVPNIPSecProxies_ProtocolObject](networkvpnipsecproxies_protocolobject.md)
  The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

## Properties

- `AutoConfigEnable` (boolean): If `true`, enables automatic proxy configuration.
- `AutoConfigURLString` (string): The URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is `true`.
- `AutoDiscoveryEnable` (boolean): If `true`, enables proxy auto discovery.
- `Protocol` (NetworkVPNIPSecProxies_ProtocolObject): The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.
- `SupplementalMatchDomains` ([string]): An array of domains that defines which hosts use proxy settings for hosts.

## See Also

- [object NetworkVPNIPSecAuthenticationObject](networkvpnipsecauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIPSecDNSObject](networkvpnipsecdnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIPSecIdleObject](networkvpnipsecidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIPSecOnDemandObject](networkvpnipsecondemandobject.md)
  Specifies details about how the system controls on-demand VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecproxiesobject)*