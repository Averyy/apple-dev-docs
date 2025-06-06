# hpkeRepresentation(kem:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Creates an encoded representation of the public key.

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
func hpkeRepresentation(kem: HPKE.KEM) throws -> Data
```

#### Return Value

The encoded key data.

#### Discussion

- kem: The key encapsulation mechanism for encapsulating the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization/hpkerepresentation(kem:))*