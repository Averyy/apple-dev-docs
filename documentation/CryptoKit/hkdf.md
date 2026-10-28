# HKDF

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).

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
struct HKDF<H> where H : HashFunction
```

## Overview

The key derivation functions allow you to derive one or more secrets of the size of your choice from a main key or passcode. The key derivation function is compliant with IETF RFC 5869. Use one of the `deriveKey` functions, such as [`deriveKey(inputKeyMaterial:outputByteCount:)`](./hkdf/derivekey%28inputkeymaterial,outputbytecount%29.md) or [`deriveKey(inputKeyMaterial:salt:info:outputByteCount:)`](./hkdf/derivekey%28inputkeymaterial,salt,info,outputbytecount%29.md), to derive a key from a main secret or passcode in a single function.

To derive a key with more fine-grained control, use `extract(inputKeyMaterial:salt:)` to create cryptographically strong key material in the form of a hashed authentication code, then call [`expand(pseudoRandomKey:info:outputByteCount:)`](./hkdf/expand%28pseudorandomkey,info,outputbytecount%29.md) using that key material to generate a symmetric key of the length you specify.

## Topics

### Deriving a key
- [static func deriveKey(inputKeyMaterial: SymmetricKey, outputByteCount: Int) -> SymmetricKey](./hkdf/derivekey%28inputkeymaterial,outputbytecount%29.md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation.
- [static func deriveKey<Info>(inputKeyMaterial: SymmetricKey, info: Info, outputByteCount: Int) -> SymmetricKey](./hkdf/derivekey%28inputkeymaterial,info,outputbytecount%29.md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information you specify.
- [static func deriveKey<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt, outputByteCount: Int) -> SymmetricKey](./hkdf/derivekey%28inputkeymaterial,salt,outputbytecount%29.md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with salt that you specify.
- [static func deriveKey<Salt, Info>(inputKeyMaterial: SymmetricKey, salt: Salt, info: Info, outputByteCount: Int) -> SymmetricKey](./hkdf/derivekey%28inputkeymaterial,salt,info,outputbytecount%29.md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.
### Controlling key derivation
- [static func expand<PRK, Info>(pseudoRandomKey: PRK, info: Info?, outputByteCount: Int) -> SymmetricKey](./hkdf/expand%28pseudorandomkey,info,outputbytecount%29.md)
  Expands cryptographically strong key material into a derived symmetric key.
### Type Methods
- [static func deriveKey(inputKeyMaterial: SymmetricKey, salt: RawSpan?, info: RawSpan?, output: inout OutputRawSpan)](./hkdf/derivekey%28inputkeymaterial,salt,info,output%29.md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.
- [static func expand(pseudoRandomKey: RawSpan, info: RawSpan?, into: inout OutputRawSpan)](./hkdf/expand%28pseudorandomkey,info,into%29.md)
  Expands cryptographically strong key material into a derived symmetric key.
- [static func extract<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt?) -> HashedAuthenticationCode<H>](./hkdf/extract%28inputkeymaterial,salt%29-4f5wf.md)
  Creates cryptographically strong key material from a main key or passcode that you specify.
- [static func extract(inputKeyMaterial: SymmetricKey, salt: RawSpan?) -> HashedAuthenticationCode<H>](./hkdf/extract%28inputkeymaterial,salt%29-7qmzj.md)
  Creates cryptographically strong key material from a main key or passcode that you specify.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf)*