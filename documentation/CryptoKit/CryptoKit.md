# Apple CryptoKit

**Framework**: Apple CryptoKit  
**Kind**: module

Perform cryptographic operations securely and efficiently.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

#### Overview

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.
- Use public-key cryptography to create and evaluate digital signatures, and to perform key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave.
- Generate symmetric keys, and use them in operations like message authentication and encryption.

Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.

## Topics

### Essentials
- [Complying with Encryption Export Regulations](../Security/complying-with-encryption-export-regulations.md)
  Declare the use of encryption in your app to streamline the app submission process.
- [Performing Common Cryptographic Operations](performing_common_cryptographic_operations.md)
  Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](storing_cryptokit_keys_in_the_keychain.md)
  Convert between strongly typed cryptographic keys and native keychain types.
### Cryptographically secure hashes
- [protocol HashFunction](hashfunction.md)
  A type that performs cryptographically secure hashing.
- [struct SHA512](sha512.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.
- [struct SHA384](sha384.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- [struct SHA256](sha256.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.
### Message authentication codes
- [struct HMAC](hmac.md)
  A hash-based message authentication algorithm.
- [struct SymmetricKey](symmetrickey.md)
  A symmetric cryptographic key.
- [struct SymmetricKeySize](symmetrickeysize.md)
  The sizes that a symmetric cryptographic key can take.
### Ciphers
- [enum AES](aes.md)
  A container for Advanced Encryption Standard (AES) ciphers.
- [enum ChaChaPoly](chachapoly.md)
  An implementation of the ChaCha20-Poly1305 cipher.
### Public key cryptography
- [enum Curve25519](curve25519.md)
  An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- [enum P521](p521.md)
  An elliptic curve that enables NIST P-521 signatures and key agreement.
- [enum P384](p384.md)
  An elliptic curve that enables NIST P-384 signatures and key agreement.
- [enum P256](p256.md)
  An elliptic curve that enables NIST P-256 signatures and key agreement.
- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
- [enum SecureEnclave](secureenclave.md)
  A representation of a device’s hardware-based key manager.
- [enum HPKE](hpke.md)
  A container for hybrid public key encryption (HPKE) operations.
### Key derivation functions
- [struct HKDF](hkdf.md)
  A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).
### Errors
- [enum CryptoKitError](cryptokiterror.md)
  General cryptography errors used by CryptoKit.
- [enum CryptoKitASN1Error](cryptokitasn1error.md)
  Errors from decoding ASN.1 content.
### Legacy algorithms
- [enum Insecure](insecure.md)
  A container for older, cryptographically insecure algorithms.
### Protocols
- [protocol DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md)
  A Diffie-Hellman Key Agreement Key
- [protocol HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
  A type that represents the private key in a Diffie-Hellman key exchange.
- [protocol HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)
  A type that represents the generation of private keys in a Diffie-Hellman key exchange.
- [protocol HPKEDiffieHellmanPublicKey](hpkediffiehellmanpublickey.md)
  A type that represents the public key in a Diffie-Hellman key exchange.
- [protocol HPKEPublicKeySerialization](hpkepublickeyserialization.md)
  A type that [`HPKE`](hpke.md) uses to encode the public key.
- [protocol KEMPrivateKey](kemprivatekey.md)
- [protocol KEMPublicKey](kempublickey.md)
### Structures
- [struct CorecryptoCurveType](corecryptocurvetype.md)
### Type Aliases
- [typealias CryptoKitMetaError](cryptokitmetaerror.md)
### Enumerations
- [enum KEM](kem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CryptoKit)*