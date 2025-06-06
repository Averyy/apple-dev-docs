# init(combined:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init<D>(combined: D) throws where D : DataProtocol
```

## Parameters

- `combined`: The combined bytes of the nonce, encrypted data, and   authentication tag.

## See Also

- [init<C, T>(nonce: AES.GCM.Nonce, ciphertext: C, tag: T) throws](aes/gcm/sealedbox/init(nonce:ciphertext:tag:).md)
  Creates a sealed box from the given tag, nonce, and ciphertext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/init(combined:))*