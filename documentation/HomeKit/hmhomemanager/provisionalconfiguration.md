# HMHomeManager.ProvisionalConfiguration

**Framework**: HomeKit  
**Kind**: struct

The configuration you use to create a temporary, provisional home for performing installation services.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct ProvisionalConfiguration
```

#### Overview

The `ProvisionalConfiguration` structure provides Thread network credentials and a pairing identity for the home hub that an installation service uses to configure a provisional home and later transfer it to the owner of the home.

## Topics

### Creating the configuration
- [init?(dictionaryRepresentation: [String : any Sendable])](hmhomemanager/provisionalconfiguration/init(dictionaryrepresentation:).md)
  Creates the configuration for a provisional home.
- [init(threadNetworkIdentifier: Data, hubPairingIdentity: HMHomeManager.PairingIdentity)](hmhomemanager/provisionalconfiguration/init(threadnetworkidentifier:hubpairingidentity:).md)
  Creates the configuration for a provisional home.
### Identifying a provisional home
- [let hubPairingIdentity: HMHomeManager.PairingIdentity](hmhomemanager/provisionalconfiguration/hubpairingidentity.md)
  Identity information that an installation service uses to set up a provisional home and pair devices.
- [let threadNetworkIdentifier: Data](hmhomemanager/provisionalconfiguration/threadnetworkidentifier.md)
  The unique identifier for a Thread network that a home hub provides.
- [var dictionaryRepresentation: [String : any Sendable]](hmhomemanager/provisionalconfiguration/dictionaryrepresentation.md)
  A dictionary of attributes that an installation service uses to configure a home.

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
- [HMHomeManager.PairingIdentity](hmhomemanager/pairingidentity.md)
  Identity information that an installation service uses to set up a provisional home for a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration)*