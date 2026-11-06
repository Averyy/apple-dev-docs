# init(threadNetworkIdentifier:hubPairingIdentity:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates the configuration for a provisional home.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- visionOS 27.2+

## Declaration

```swift
init(threadNetworkIdentifier: Data, hubPairingIdentity: HMHomeManager.PairingIdentity)
```

## Return Value

The configuration for a provisional home.

## Overview

## Parameters

- `threadNetworkIdentifier`: The unique identifier for a Thread network that a home hub provides.
- `hubPairingIdentity`: Identity information that an installation service uses to pair a home hub with their hardware during setup.

## See Also

### Creating the configuration
- [init?(dictionaryRepresentation: [String : any Sendable])](./init%28dictionaryrepresentation%29.md)
  Creates the configuration for a provisional home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/provisionalconfiguration/init(threadnetworkidentifier:hubpairingidentity:))*