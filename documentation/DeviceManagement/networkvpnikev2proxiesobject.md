# NetworkVPNIKEV2ProxiesObject

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
object NetworkVPNIKEV2ProxiesObject
```

## Topics

### Objects
- [object NetworkVPNIKEV2Proxies_ProtocolObject](networkvpnikev2proxies_protocolobject.md)
  The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

## Properties

- `AutoConfigEnable` (boolean): If `true`, enables automatic proxy configuration.
- `AutoConfigURLString` (string): The URL to the location of the proxy auto-configuration file. Used only when `ProxyAutoConfigEnable` is `true`.
- `AutoDiscoveryEnable` (boolean): If `true`, enables proxy auto discovery.
- `Protocol` (NetworkVPNIKEV2Proxies_ProtocolObject): The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.
- `SupplementalMatchDomains` ([string]): An array of domains that defines which hosts use proxy settings for hosts.

## See Also

- [object NetworkVPNIKEV2AuthenticationObject](networkvpnikev2authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIKEV2DNSObject](networkvpnikev2dnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIKEV2IdleObject](networkvpnikev2idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIKEV2NetworkRoutingObject](networkvpnikev2networkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNIKEV2OnDemandObject](networkvpnikev2ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIKEV2PostQuantumKeyExchangeObject](networkvpnikev2postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNIKEV2ProviderObject](networkvpnikev2providerobject.md)
  Specifies details about the provider.
- [object NetworkVPNIKEV2SecurityAssociationParametersObject](networkvpnikev2securityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2proxiesobject)*