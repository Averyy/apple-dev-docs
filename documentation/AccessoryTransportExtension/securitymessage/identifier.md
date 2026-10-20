# identifier

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Instance Property

An optional Bluetooth identifier that the system uses to derive HPKE keys.

**Availability**:
- iOS 26.5+

## Declaration

```swift
let identifier: String?
```

#### Discussion

The system provides this identifier when delivering [`SecurityMessage.KeyType.encapsulatedKey`](./keytype-swift.enum/encapsulatedkey.md) to your extension. Forward it to your accessory for key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/identifier)*