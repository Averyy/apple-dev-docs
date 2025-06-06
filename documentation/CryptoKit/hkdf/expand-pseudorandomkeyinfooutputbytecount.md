# expand(pseudoRandomKey:info:outputByteCount:)

**Framework**: Apple CryptoKit  
**Kind**: method

Expands cryptographically strong key material into a derived symmetric key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static func expand<PRK, Info>(pseudoRandomKey prk: PRK, info: Info?, outputByteCount: Int) -> SymmetricKey where PRK : ContiguousBytes, Info : DataProtocol
```

#### Return Value

The derived symmetric key.

#### Discussion

Generate cryptographically strong key material to use with this function by calling [`extract(inputKeyMaterial:salt:)`](hkdf/extract(inputkeymaterial:salt:).md).

## Parameters

- `prk`: A pseudorandom, cryptographically strong key generated from the    function.
- `info`: The shared information to use for key derivation.
- `outputByteCount`: The length in bytes of the resulting symmetric key.

## See Also

- [static func extract<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt?) -> HashedAuthenticationCode<H>](hkdf/extract(inputkeymaterial:salt:).md)
  Creates cryptographically strong key material from a main key or passcode that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:outputbytecount:))*