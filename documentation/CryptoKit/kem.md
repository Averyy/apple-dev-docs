# KEM

**Framework**: Apple CryptoKit  
**Kind**: enum

A key encapsulation mechanism.

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
enum KEM
```

#### Overview

Use a key encapsulation mechanism (KEM) to protect a symmetric cryptographic key that you share with another party.

## Topics

### Defining encapsulation outputs
- [struct EncapsulationResult](kem/encapsulationresult.md)
  The result of a key encapsulation operation.
### Handling errors
- [enum Errors](kem/errors.md)
  Errors that CryptoKit throws when it encounters problems in key encapsulation mechanism (KEM) operations.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MLKEM768](mlkem768.md)
  The Module-Lattice key encapsulation mechanism (KEM).
- [enum MLKEM1024](mlkem1024.md)
  The Module-Lattice key encapsulation mechanism (KEM).
- [enum XWingMLKEM768X25519](xwingmlkem768x25519.md)
  The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kem)*