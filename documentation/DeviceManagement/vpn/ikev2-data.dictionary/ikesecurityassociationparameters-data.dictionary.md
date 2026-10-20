# VPN.IKEv2.IKESecurityAssociationParameters

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary that contains security association parameters.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```
object VPN.IKEv2.IKESecurityAssociationParameters
```

## Properties

- `DiffieHellmanGroup` (integer): The Diffie-Hellman group.

  For `AlwaysOn` VPN in iOS 14.2 and later, the minimum allowed value is `14`.

  `1`, `2`, and `5` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.

  **Default**: `14`; **Allowed Values**: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `31`, `32`
- `EncryptionAlgorithm` (string): The encryption algorithm.

  In watchOS and tvOS, the default value is `AES-256-GCM`. `DES` and `3DES` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.

  **Default**: `AES-256`; **Allowed Values**: `DES`, `3DES`, `AES-128`, `AES-256`, `AES-128-GCM`, `AES-256-GCM`, `ChaCha20Poly1305`
- `IntegrityAlgorithm` (string): The integrity algorithm.

  `SHA1-96` and `SHA1-160` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.

  **Default**: `SHA2-256`; **Allowed Values**: `SHA1-96`, `SHA1-160`, `SHA2-256`, `SHA2-384`, `SHA2-512`
- `LifeTimeInMinutes` (integer): The SA lifetime (rekey interval) in minutes.

  **Default**: `1440`; **Minimum**: `10`; **Maximum**: `1440`
- `PostQuantumKeyExchangeMethods` ([integer]): An array of integers representing postquantum key exchange methods the device uses during SA establishment and rekey. You can specify up to seven items, which correspond to ADDKE1 - ADDKE7 from RFC 9370.

  Available: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 16+ | visionOS 26+ | watchOS 26+

  **Allowed Values**: `0`, `36`, `37`

## See Also

### Objects
- [object VPN.IKEv2.ChildSecurityAssociationParameters](./childsecurityassociationparameters-data.dictionary.md)
  The dictionary that contains child security association parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ikev2-data.dictionary/ikesecurityassociationparameters-data.dictionary)*