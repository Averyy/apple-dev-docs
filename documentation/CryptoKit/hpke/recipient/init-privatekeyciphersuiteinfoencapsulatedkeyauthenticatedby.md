# init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a recipient in authentication mode.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data, authenticatedBy authenticationKey: SK.PublicKey) throws where SK : HPKEDiffieHellmanPrivateKey
```

#### Discussion

The `Receiver` decrypts messages in authentication mode using the encapsulated key with the key schedule information (`info` data). Messages also include authentication data so that the recipient can verify the authenticity of the sender’s private key.

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `privateKey`: The recipient’s private key for decrypting the incoming messages.
- `ciphersuite`: The cipher suite that defines the cryptographic algorithms to use.
- `info`: Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same   data.
- `encapsulatedKey`: The encapsulated symmetric key that the sender provides.
- `authenticationKey`: The sender’s public key for authenticating the messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:))*