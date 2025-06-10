# init(recipientKey:ciphersuite:info:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a sender in base mode.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data) throws where PK : HPKEKEMPublicKey
```

#### Discussion

The `Sender` encrypts messages in base mode with a symmetric encryption key it derives using a key derivation function (KDF). The KDF uses the key schedule data in `info` as input to generate the key. The `Sender` encapsulates the derived key using the recipient’s public key. You access the encapsulated key using [`encapsulatedKey`](hpke/sender/encapsulatedkey.md).

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `recipientKey`: The recipient’s public key for encrypting the messages.
- `ciphersuite`: The cipher suite that defines the cryptographic algorithms to use.
- `info`: Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same   data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:)-swk5)*