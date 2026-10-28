# addProvisionalHome(named:configuration:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a temporary provisional home while someone performs HomeKit installation services for a client.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func addProvisionalHome(named name: String, configuration: HMHomeManager.ProvisionalConfiguration) async throws -> HMHome
```

## Return Value

The configured provisional home you use for installation services.

## Overview

When a person performs installation services at a home and pairs accessories, HomeKit automatically pre-installs the home hub as an administrative controller for each accessory. When using HomeKit accessory protocol (HAP) pairing, HomeKit enables seamless transfer of accessories without key rotation when an installation service provider transfers the provisional home to the home hub.

## Parameters

- `name`: The name of the provisional home. It must be different from the name of any existing home.
- `configuration`: The configuration for the provisional home with Thread network credentials and a home hub pairing identity.

## See Also

### Providing installation services
- [HMHomeManager.ProvisionalConfiguration](./provisionalconfiguration.md)
  The configuration you use to create a temporary, provisional home for performing installation services.
- [HMHomeManager.PairingIdentity](./pairingidentity.md)
  Identity information that an installation service uses to set up a provisional home for a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/addprovisionalhome(named:configuration:))*