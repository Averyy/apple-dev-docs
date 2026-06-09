# NetworkVPNIKEV2ProviderObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about the provider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIKEV2ProviderObject
```

## Properties

- `ComposedIdentifier` (string): In iOS, tvOS, and visionOS, the identifier is a bundle ID, for example, “com.example.app”. In macOS, the identifier is a composed identifier. The format of the composed identifier is either “Bundle-ID” or “Bundle-ID {Designated-Requirement}”. “Bundle-ID” is the bundle identifier string of the provider. “Designated-Requirement” is the designated requirement string from the code signature of the provider. For example, “com.example.app” for the bundle ID format, or “com.example.app {anchor apple generic}” for the designated requirement format.
- `Type` (string): The type of VPN service. If the value is `app-proxy`, the service tunnels traffic at the app level. If the value is `packet-tunnel`, the service tunnels traffic at the IP layer.

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
- [object NetworkVPNIKEV2ProxiesObject](networkvpnikev2proxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNIKEV2SecurityAssociationParametersObject](networkvpnikev2securityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2providerobject)*