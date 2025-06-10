# init(ikm:)

**Framework**: Apple CryptoKit  
**Kind**: init

Create a P256 curve key from input keying material via the DeriveKeyPair functionality from RFC9180. The minimum length of the input keying material is determined by the curve; see Nsk from https://datatracker.ietf.org/doc/html/rfc9180#name-key-encapsulation-mechanism.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(ikm: SymmetricKey) throws
```

## Parameters

- `ikm`: Cryptographic input keying material of length at least Nsk=32 bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/privatekey/init(ikm:))*