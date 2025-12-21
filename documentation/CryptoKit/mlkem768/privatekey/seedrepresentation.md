# seedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

The private key’s seed representation.

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
var seedRepresentation: Data { get }
```

#### Discussion

The seed is `d||z`, as specified in the algorithm `ML-KEM.KeyGen_internal(d,z)` (Algorithm 16) of FIPS 203.

## See Also

- [var integrityCheckedRepresentation: Data](mlkem768/privatekey/integritycheckedrepresentation.md)
  An integrity-checked representation of the private key.
- [var publicKey: MLKEM768.PublicKey](mlkem768/privatekey/publickey.md)
  The corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/seedrepresentation)*