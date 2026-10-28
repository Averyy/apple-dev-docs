# init(pairingIdentifier:publicKey:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates identity information that an installation service uses to set up a provisional home.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(pairingIdentifier: String, publicKey: Data)
```

## Return Value

Identity information that an installation service uses to set up a provisional home.

## Parameters

- `pairingIdentifier`: The HomeKit Accessory Protocol identifier you use to configure a temporary, provisional home.
- `publicKey`: The `Ed25519` HAP long-term public key for pairing a HomeKit accessory.

## See Also

### Creating a pairing identity
- [let pairingIdentifier: String](./pairingidentifier.md)
  The HomeKit Accessory Protocol identifier you use to configure a temporary, provisional home.
- [let publicKey: Data](./publickey.md)
  The Ed25519 HAP public key for pairing a HomeKit accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/pairingidentity/init(pairingidentifier:publickey:))*