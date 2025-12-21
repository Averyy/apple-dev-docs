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
- [Performing Common Cryptographic Operations](performing-common-cryptographic-operations.md)
  Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](storing-cryptokit-keys-in-the-keychain.md)
  Convert between strongly typed cryptographic keys and native keychain types.
- [Enhancing your app’s privacy and security with quantum-secure workflows](enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows.md)
  Use quantum-secure cryptography to protect your app from quantum attacks.
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
### Key encapsulation mechanisms (KEM)
- [enum KEM](kem.md)
  A key encapsulation mechanism.
- [enum MLKEM768](mlkem768.md)
  The Module-Lattice key encapsulation mechanism (KEM).
- [enum MLKEM1024](mlkem1024.md)
  The Module-Lattice key encapsulation mechanism (KEM).
- [enum XWingMLKEM768X25519](xwingmlkem768x25519.md)
  The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06
### KEM keys
- [protocol KEMPrivateKey](kemprivatekey.md)
  The private key for a key encapsulation mechanism.
- [protocol KEMPublicKey](kempublickey.md)
  The public key for a key encapsulation mechanism.
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
- [protocol HPKEKEMPrivateKey](hpkekemprivatekey.md)
  A type that represents the private key in HPKE.
- [protocol HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)
  A type that represents the generation of private keys in HPKE
- [protocol HPKEKEMPublicKey](hpkekempublickey.md)
  A type that represents the public key in HPKE
- [protocol HPKEPublicKeySerialization](hpkepublickeyserialization.md)
  A type that [`HPKE`](hpke.md) uses to encode the public key.
### Structures
- [struct CorecryptoCurveType](corecryptocurvetype.md)
- [struct SHA3_256](sha3_256.md)
  An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 256-bit digest.
- [struct SHA3_256Digest](sha3_256digest.md)
  The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.
- [struct SHA3_384](sha3_384.md)
  An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 384-bit digest.
- [struct SHA3_384Digest](sha3_384digest.md)
  The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 384-bit digest.
- [struct SHA3_512](sha3_512.md)
  An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 512-bit digest.
- [struct SHA3_512Digest](sha3_512digest.md)
  The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 512-bit digest.
### Type Aliases
- [typealias CryptoKitMetaError](cryptokitmetaerror.md)
- [typealias SHA2_256](sha2_256.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.
- [typealias SHA2_384](sha2_384.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- [typealias SHA2_512](sha2_512.md)
  An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.
### Enumerations
- [enum MLDSA65](mldsa65.md)
  The MLDSA65 Digital Signature Algorithm
- [enum MLDSA87](mldsa87.md)
  The MLDSA87 Digital Signature Algorithm


---

*[View on Apple Developer](https://developer.apple.com/documentation/CryptoKit)*