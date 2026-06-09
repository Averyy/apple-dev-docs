# NetworkVPNIKEV2SecurityAssociationParametersObject

**Framework**: Device Management  
**Kind**: dictionary

These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIKEV2SecurityAssociationParametersObject
```

## Properties

- `DiffieHellmanGroup` (integer): The Diffie-Hellman group. For `AlwaysOn` VPN, the minimum allowed value is `14`.
- `EncryptionAlgorithm` (string): The encryption algorithm. On tvOS, the default value is `AES-256-GCM`.
- `IntegrityAlgorithm` (string): The integrity algorithm.
- `LifeTimeInMinutes` (integer): The SA lifetime (rekey interval) in minutes.
- `PostQuantumKeyExchangeMethods` ([integer]): An array of integers representing postquantum key exchange methods the device uses during SA establishment and rekey. You can specify up to seven items, which correspond to ADDKE1 - ADDKE7 from RFC 9370.

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
- [object NetworkVPNIKEV2ProxiesObject](networkvpnikev2proxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2securityassociationparametersobject)*