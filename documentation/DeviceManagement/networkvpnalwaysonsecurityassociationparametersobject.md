# NetworkVPNAlwaysOnSecurityAssociationParametersObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```
object NetworkVPNAlwaysOnSecurityAssociationParametersObject
```

## Properties

- `DiffieHellmanGroup` (integer): The Diffie-Hellman group.

  For `AlwaysOn` VPN, the minimum allowed value is `14`.

  **Default**: `14`; **Allowed Values**: `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `31`, `32`
- `EncryptionAlgorithm` (string): The encryption algorithm.

  In tvOS the default value is `AES-256-GCM`.

  **Default**: `AES-256`; **Allowed Values**: `AES-128`, `AES-256`, `AES-128-GCM`, `AES-256-GCM`, `ChaCha20Poly1305`
- `IntegrityAlgorithm` (string): The integrity algorithm.

  **Default**: `SHA2-256`; **Allowed Values**: `SHA2-256`, `SHA2-384`, `SHA2-512`
- `LifeTimeInMinutes` (integer): The SA lifetime (rekey interval) in minutes.

  **Default**: `1440`; **Minimum**: `10`; **Maximum**: `1440`
- `PostQuantumKeyExchangeMethods` ([integer]): An array of integers representing postquantum key exchange methods the device uses during SA establishment and rekey. You can specify up to seven items, which correspond to ADDKE1 - ADDKE7 from RFC 9370.

  **Allowed Values**: `0`, `36`, `37`

## See Also

### Objects
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_AuthenticationObject](./networkvpnalwaysontunnelconfigurationelement_ikev2_authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_IdleObject](./networkvpnalwaysontunnelconfigurationelement_ikev2_idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2_PostQuantumKeyExchangeObject](./networkvpnalwaysontunnelconfigurationelement_ikev2_postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonsecurityassociationparametersobject)*