# seedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

The private key’s seed representation.

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

The seed is `d||z`, as specified in the algorithm `ML-KEM.KeyGen_internal(d,z)` (Algorithm 16) of FIPS 203.

## See Also

- [var integrityCheckedRepresentation: Data](mlkem1024/privatekey/integritycheckedrepresentation.md)
  An integrity-checked representation of the private key.
- [var publicKey: MLKEM1024.PublicKey](mlkem1024/privatekey/publickey.md)
  The corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/seedrepresentation)*