# init(_:kem:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Required**: Yes

Creates a public key from an encoded representation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init<D>(_ serialization: D, kem: HPKE.KEM) throws where D : ContiguousBytes
```

#### Discussion

- serialization: The serialized key data.
- kem: The key encapsulation mechanism that the sender used to encapsulate the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization/init(_:kem:))*