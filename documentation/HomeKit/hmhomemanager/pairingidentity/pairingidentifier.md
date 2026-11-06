# pairingIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The HomeKit Accessory Protocol identifier you use to configure a temporary, provisional home.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- visionOS 27.2+

## Declaration

```swift
let pairingIdentifier: String
```

## See Also

### Creating a pairing identity
- [init(pairingIdentifier: String, publicKey: Data)](./init%28pairingidentifier,publickey%29.md)
  Creates identity information that an installation service uses to set up a provisional home.
- [let publicKey: Data](./publickey.md)
  The Ed25519 HAP public key for pairing a HomeKit accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/pairingidentity/pairingidentifier)*