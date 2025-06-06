# extract(inputKeyMaterial:salt:)

**Framework**: Apple CryptoKit  
**Kind**: method

Creates cryptographically strong key material from a main key or passcode that you specify.

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
static func extract<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt?) -> HashedAuthenticationCode<H> where Salt : DataProtocol
```

#### Return Value

A pseudorandom, cryptographically strong key in the form of a hashed authentication code.

#### Discussion

Generate a derived symmetric key from the cryptographically strong key material this function creates by calling [`expand(pseudoRandomKey:info:outputByteCount:)`](hkdf/expand(pseudorandomkey:info:outputbytecount:).md).

## Parameters

- `inputKeyMaterial`: The main key or passcode the derivation function   uses to derive a key.
- `salt`: The salt to use for key derivation.

## See Also

- [static func expand<PRK, Info>(pseudoRandomKey: PRK, info: Info?, outputByteCount: Int) -> SymmetricKey](hkdf/expand(pseudorandomkey:info:outputbytecount:).md)
  Expands cryptographically strong key material into a derived symmetric key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:))*