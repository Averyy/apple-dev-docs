# MLKEM1024

**Framework**: Apple CryptoKit  
**Kind**: enum

The Module-Lattice key encapsulation mechanism (KEM).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum MLKEM1024
```

## Topics

### Keys
- [MLKEM1024.PrivateKey](mlkem1024/privatekey.md)
  A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.
- [MLKEM1024.PublicKey](mlkem1024/publickey.md)
  A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum KEM](kem.md)
  A key encapsulation mechanism.
- [enum MLKEM768](mlkem768.md)
  The Module-Lattice key encapsulation mechanism (KEM).
- [enum XWingMLKEM768X25519](xwingmlkem768x25519.md)
  The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024)*