# NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about the provider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject
```

## Properties

- `ComposedIdentifier` (string): In iOS, tvOS, and visionOS, the identifier is a bundle ID, for example, “com.example.app”. In macOS, the identifier is a composed identifier. The format of the composed identifier is either “Bundle-ID”, “Bundle-ID (Team-ID)”, or “Bundle-ID {Designated-Requirement}”. “Bundle-ID” is the bundle identifier string of the provider. “Team-ID” is the team identifier from the provider’s code signature. “Designated-Requirement” is the designated requirement string from the code signature of the provider. For example, “com.example.app” for the bundle ID format, “com.example.app (ABCD1234)” for the team ID format, or “com.example.app {anchor apple generic}” for the designated requirement format.
- `Type` (string): The type of VPN service. If the value is `app-proxy`, the service tunnels traffic at the app level. If the value is `packet-tunnel`, the service tunnels traffic at the IP layer.

## See Also

- [object NetworkVPNAlwaysOnSecurityAssociationParametersObject](networkvpnalwaysonsecurityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject](networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject](networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_NetworkRoutingObject](networkvpnalwaysontunnelconfigurationelement_ikev2_networkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_OnDemandObject](networkvpnalwaysontunnelconfigurationelement_ikev2_ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelement_ikev2_providerobject)*