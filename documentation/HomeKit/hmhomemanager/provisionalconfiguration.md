# HMHomeManager.ProvisionalConfiguration

**Framework**: HomeKit  
**Kind**: struct  
**Role**: Structure

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
- [init?(dictionaryRepresentation: [String : any Sendable])](./provisionalconfiguration/init%28dictionaryrepresentation%29.md)
  Creates the configuration for a provisional home.
- [init(threadNetworkIdentifier: Data, hubPairingIdentity: HMHomeManager.PairingIdentity)](./provisionalconfiguration/init%28threadnetworkidentifier,hubpairingidentity%29.md)
  Creates the configuration for a provisional home.
### Identifying a provisional home
- [let hubPairingIdentity: HMHomeManager.PairingIdentity](./provisionalconfiguration/hubpairingidentity.md)
  Identity information that an installation service uses to set up a provisional home and pair devices.
- [let threadNetworkIdentifier: Data](./provisionalconfiguration/threadnetworkidentifier.md)
  The unique identifier for a Thread network that a home hub provides.
- [var dictionaryRepresentation: [String : any Sendable]](./provisionalconfiguration/dictionaryrepresentation.md)
  A dictionary of attributes that an installation service uses to configure a home.

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
- [HMHomeManager.PairingIdentity](./pairingidentity.md)
  Identity information that an installation service uses to set up a provisional home for a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration)*