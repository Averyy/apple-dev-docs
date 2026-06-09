# extract(inputKeyMaterial:salt:)

**Framework**: Apple CryptoKit  
**Kind**: method

Creates cryptographically strong key material from a main key or passcode that you specify.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func extract(inputKeyMaterial: SymmetricKey, salt: RawSpan?) -> HashedAuthenticationCode<H>
```

#### Return Value

A pseudorandom, cryptographically strong key in the form of a hashed authentication code.

#### Discussion

Generate a derived symmetric key from the cryptographically strong key material this function creates by calling [`expand(pseudoRandomKey:info:outputByteCount:)`](hkdf/expand(pseudorandomkey:info:outputbytecount:).md).

## Parameters

- `inputKeyMaterial`: The main key or passcode the derivation function uses to derive a key.
- `salt`: The salt to use for key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:)-7qmzj)*