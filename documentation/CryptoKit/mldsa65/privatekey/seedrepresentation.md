# seedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

The seed representation of the private key.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var seedRepresentation: Data { get }
```

#### Discussion

The seed representation is 32 bytes long, and is the parameter for the `ML-DSA.KeyGen_internal` algorithm (Algorithm 16) of FIPS 204.

## See Also

- [var integrityCheckedRepresentation: Data](mldsa65/privatekey/integritycheckedrepresentation.md)
  The integrity-checked data representation of the private key.
- [var publicKey: MLDSA65.PublicKey](mldsa65/privatekey/publickey.md)
  The associated public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/seedrepresentation)*