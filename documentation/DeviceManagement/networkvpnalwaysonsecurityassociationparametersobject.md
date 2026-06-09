# NetworkVPNAlwaysOnSecurityAssociationParametersObject

**Framework**: Device Management  
**Kind**: dictionary

These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnSecurityAssociationParametersObject
```

## Properties

- `DiffieHellmanGroup` (integer): The Diffie-Hellman group. For `AlwaysOn` VPN, the minimum allowed value is `14`.
- `EncryptionAlgorithm` (string): The encryption algorithm. In tvOS the default value is `AES-256-GCM`.
- `IntegrityAlgorithm` (string): The integrity algorithm.
- `LifeTimeInMinutes` (integer): The SA lifetime (rekey interval) in minutes.
- `PostQuantumKeyExchangeMethods` ([integer]): An array of integers representing postquantum key exchange methods the device uses during SA establishment and rekey. You can specify up to seven items, which correspond to ADDKE1 - ADDKE7 from RFC 9370.

## See Also

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
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_ProviderObject](networkvpnalwaysontunnelconfigurationelement_ikev2_providerobject.md)
  Specifies details about the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonsecurityassociationparametersobject)*