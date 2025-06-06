# SecPublicKeyHash

**Framework**: Security  
**Kind**: typealias

A container for a 20-byte public key hash.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecPublicKeyHash = (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

#### Discussion

The `SecPublicKeyHash` type represents a hash of a public key. You can use the constant `kSecPublicKeyHashItemAttr` as input to functions in the Keychain Services API to set or retrieve a certificate attribute value of this type. See [`Keychain services`](keychain-services.md) for information about getting and setting attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpublickeyhash)*