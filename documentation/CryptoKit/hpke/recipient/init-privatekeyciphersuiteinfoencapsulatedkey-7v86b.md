# init(privateKey:ciphersuite:info:encapsulatedKey:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a recipient in base mode.

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
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data) throws where SK : HPKEKEMPrivateKey
```

#### Discussion

The `Receiver` decrypts messages in base mode using the encapsulated key with the key schedule information (`info` data).

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `privateKey`: The recipient’s private key for decrypting the incoming messages.
- `ciphersuite`: The cipher suite that defines the cryptographic algorithms to use.
- `info`: Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same   data.
- `encapsulatedKey`: The encapsulated symmetric key that the sender provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:)-7v86b)*