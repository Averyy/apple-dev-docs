# HMHomeManager.PairingIdentity

**Framework**: HomeKit  
**Kind**: struct

Identity information that an installation service uses to set up a provisional home for a client.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct PairingIdentity
```

## Topics

### Creating a pairing identity
- [init(pairingIdentifier: String, publicKey: Data)](hmhomemanager/pairingidentity/init(pairingidentifier:publickey:).md)
  Creates identity information that an installation service uses to set up a provisional home.
- [let pairingIdentifier: String](hmhomemanager/pairingidentity/pairingidentifier.md)
  The HomeKit Accessory Protocol identifier you use to configure a temporary, provisional home.
- [let publicKey: Data](hmhomemanager/pairingidentity/publickey.md)
  The Ed25519 HAP public key for pairing a HomeKit accessory.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func addProvisionalHome(named: String, configuration: HMHomeManager.ProvisionalConfiguration) async throws -> HMHome](hmhomemanager/addprovisionalhome(named:configuration:).md)
  Adds a temporary provisional home while someone performs HomeKit installation services for a client.
- [HMHomeManager.ProvisionalConfiguration](hmhomemanager/provisionalconfiguration.md)
  The configuration you use to create a temporary, provisional home for performing installation services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/pairingidentity)*