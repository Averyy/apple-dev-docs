# deriveKey(inputKeyMaterial:info:outputByteCount:)

**Framework**: Apple CryptoKit  
**Kind**: method

Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information you specify.

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
static func deriveKey<Info>(inputKeyMaterial: SymmetricKey, info: Info, outputByteCount: Int) -> SymmetricKey where Info : DataProtocol
```

#### Return Value

The derived symmetric key.

## Parameters

- `inputKeyMaterial`: The main key or passcode the derivation function   uses to derive a key.
- `info`: The shared information to use for key derivation.
- `outputByteCount`: The length in bytes of the resulting symmetric key.

## See Also

- [static func deriveKey(inputKeyMaterial: SymmetricKey, outputByteCount: Int) -> SymmetricKey](hkdf/derivekey(inputkeymaterial:outputbytecount:).md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation.
- [static func deriveKey<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt, outputByteCount: Int) -> SymmetricKey](hkdf/derivekey(inputkeymaterial:salt:outputbytecount:).md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with salt that you specify.
- [static func deriveKey<Salt, Info>(inputKeyMaterial: SymmetricKey, salt: Salt, info: Info, outputByteCount: Int) -> SymmetricKey](hkdf/derivekey(inputkeymaterial:salt:info:outputbytecount:).md)
  Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:info:outputbytecount:))*