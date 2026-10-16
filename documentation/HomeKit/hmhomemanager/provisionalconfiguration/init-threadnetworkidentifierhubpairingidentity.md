# init(threadNetworkIdentifier:hubPairingIdentity:)

**Framework**: HomeKit  
**Kind**: init

Creates the configuration for a provisional home.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(threadNetworkIdentifier: Data, hubPairingIdentity: HMHomeManager.PairingIdentity)
```

#### Return Value

The configuration for a provisional home.

#### Overview

## Parameters

- `threadNetworkIdentifier`: The unique identifier for a Thread network that a home hub provides.
- `hubPairingIdentity`: Identity information that an installation service uses to pair a home hub with their hardware during setup.

## See Also

- [init?(dictionaryRepresentation: [String : any Sendable])](hmhomemanager/provisionalconfiguration/init(dictionaryrepresentation:).md)
  Creates the configuration for a provisional home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration/init(threadnetworkidentifier:hubpairingidentity:))*