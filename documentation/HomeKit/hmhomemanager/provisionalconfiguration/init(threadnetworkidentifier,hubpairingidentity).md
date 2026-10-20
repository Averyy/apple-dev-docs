# init(threadNetworkIdentifier:hubPairingIdentity:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

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

### Creating the configuration
- [init?(dictionaryRepresentation: [String : any Sendable])](./init%28dictionaryrepresentation%29.md)
  Creates the configuration for a provisional home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration/init(threadnetworkidentifier:hubpairingidentity:))*