# HPKE.Errors

**Framework**: Apple CryptoKit  
**Kind**: enum

Hybrid public key encryption (HPKE) errors that CryptoKit uses.

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
enum Errors
```

## Topics

### Enumeration Cases
- [HPKE.Errors.ciphertextTooShort](hpke/errors/ciphertexttooshort.md)
  The ciphertext is too short.
- [HPKE.Errors.expectedPSK](hpke/errors/expectedpsk.md)
  The PSK is nil and the object is in PSK mode, or in authentication and PSK mode.
- [HPKE.Errors.exportOnlyMode](hpke/errors/exportonlymode.md)
  The object is in export-only mode and received a request to encrypt or decrypt data.
- [HPKE.Errors.inconsistentCiphersuiteAndKey](hpke/errors/inconsistentciphersuiteandkey.md)
  The supplied encryption key is incompatible with the requested cipher suite.
- [HPKE.Errors.inconsistentPSKInputs](hpke/errors/inconsistentpskinputs.md)
  The PSK is nil and the PSK ID isn’t nil, or the PSK ID is nil and the PSK isn’t nil.
- [HPKE.Errors.inconsistentParameters](hpke/errors/inconsistentparameters.md)
  The parameters for initializing an HPKE sender or receiver are inconsistent.
- [HPKE.Errors.outOfRangeSequenceNumber](hpke/errors/outofrangesequencenumber.md)
  The sequence number for encrypting or decrypting the message is out of range.
- [HPKE.Errors.unexpectedPSK](hpke/errors/unexpectedpsk.md)
  The PSK isn’t nil and the object is in base mode, or in authentication mode.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/errors)*