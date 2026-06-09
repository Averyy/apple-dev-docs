# VPN.IKEv2.ChildSecurityAssociationParameters

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains child security association parameters.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
object VPN.IKEv2.ChildSecurityAssociationParameters
```

## Properties

- `DiffieHellmanGroup` (integer): The Diffie-Hellman group. For `AlwaysOn` VPN in iOS 14.2 and later, the minimum allowed value is `14`. `1`, `2`, and `5` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.
- `EncryptionAlgorithm` (string): The encryption algorithm. In watchOS and tvOS, the default value is `AES-256-GCM`. `DES` and `3DES` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.
- `IntegrityAlgorithm` (string): The integrity algorithm. `SHA1-96` and `SHA1-160` are available only in iOS, macOS, and visionOS prior to iOS 26, macOS 26, and visionOS 26.
- `LifeTimeInMinutes` (integer): The SA lifetime (rekey interval) in minutes.
- `PostQuantumKeyExchangeMethods` ([integer]): An array of integers representing postquantum key exchange methods the device uses during SA establishment and rekey. You can specify up to seven items, which correspond to ADDKE1 - ADDKE7 from RFC 9370. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | tvOS 16+ | visionOS 26+ | watchOS 26+

## See Also

- [object VPN.IKEv2.IKESecurityAssociationParameters](vpn/ikev2-data.dictionary/ikesecurityassociationparameters-data.dictionary.md)
  The dictionary that contains security association parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ikev2-data.dictionary/childsecurityassociationparameters-data.dictionary)*