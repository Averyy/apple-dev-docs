# HMHomeManager.PairingIdentity

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

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
- [init(pairingIdentifier: String, publicKey: Data)](./pairingidentity/init%28pairingidentifier,publickey%29.md)
  Creates identity information that an installation service uses to set up a provisional home.
- [let pairingIdentifier: String](./pairingidentity/pairingidentifier.md)
  The HomeKit Accessory Protocol identifier you use to configure a temporary, provisional home.
- [let publicKey: Data](./pairingidentity/publickey.md)
  The Ed25519 HAP public key for pairing a HomeKit accessory.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Providing installation services
- [func addProvisionalHome(named: String, configuration: HMHomeManager.ProvisionalConfiguration) async throws -> HMHome](./addprovisionalhome%28named,configuration%29.md)
  Adds a temporary provisional home while someone performs HomeKit installation services for a client.
- [HMHomeManager.ProvisionalConfiguration](./provisionalconfiguration.md)
  The configuration you use to create a temporary, provisional home for performing installation services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/pairingidentity)*