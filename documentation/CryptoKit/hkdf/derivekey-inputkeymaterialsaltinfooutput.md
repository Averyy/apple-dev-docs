# deriveKey(inputKeyMaterial:salt:info:output:)

**Framework**: Apple CryptoKit  
**Kind**: method

Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func deriveKey(inputKeyMaterial: SymmetricKey, salt: RawSpan? = nil, info: RawSpan? = nil, output outputKey: inout OutputRawSpan)
```

## Parameters

- `inputKeyMaterial`: The main key or passcode the derivation function uses to derive a key.
- `salt`: The salt to use for key derivation.
- `info`: The shared information to use for key derivation.
- `outputKey`: An output span that will be populated with the derived symmetric key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:salt:info:output:))*