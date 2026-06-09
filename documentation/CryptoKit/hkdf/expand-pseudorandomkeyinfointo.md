# expand(pseudoRandomKey:info:into:)

**Framework**: Apple CryptoKit  
**Kind**: method

Expands cryptographically strong key material into a derived symmetric key.

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
static func expand(pseudoRandomKey prk: RawSpan, info: RawSpan?, into output: inout OutputRawSpan)
```

#### Discussion

Generate cryptographically strong key material to use with this function by calling `extract(inputKeyMaterial:salt:)`.

## Parameters

- `prk`: A pseudorandom, cryptographically strong key generated from the `extract(inputKeyMaterial:salt:)` function.
- `info`: The shared information to use for key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hkdf/expand(pseudorandomkey:info:into:))*