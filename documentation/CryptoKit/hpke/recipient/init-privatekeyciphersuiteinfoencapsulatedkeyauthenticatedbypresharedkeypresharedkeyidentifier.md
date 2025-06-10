# init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:presharedKey:presharedKeyIdentifier:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a recipient in authentication and preshared key mode.

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
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data, authenticatedBy authenticationKey: SK.PublicKey, presharedKey psk: SymmetricKey, presharedKeyIdentifier pskID: Data) throws where SK : HPKEDiffieHellmanPrivateKey
```

#### Discussion

The `Receiver` decrypts messages it receives in authentication and preshared key (`auth_psk`) mode using the encapsulated key with the key schedule information (`info` data), in addition to a symmetric encryption key that the sender and recipient both know in advance. Messages also include authentication data so that the recipient can verify the authenticity of the sender’s private key.

> **Note**: The system throws errors from [`HPKE.Errors`](hpke/errors.md) when it encounters them.

## Parameters

- `privateKey`: The recipient’s private key for decrypting the incoming messages.
- `ciphersuite`: The cipher suite that defines the cryptographic algorithms to use.
- `info`: Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same   data.
- `encapsulatedKey`: The encapsulated symmetric key that the sender provides.
- `authenticationKey`: The sender’s public key for authenticating the messages.
- `psk`: A preshared key (PSK) that the sender and the recipient both hold.
- `pskID`: An identifier for the PSK.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:presharedkey:presharedkeyidentifier:))*