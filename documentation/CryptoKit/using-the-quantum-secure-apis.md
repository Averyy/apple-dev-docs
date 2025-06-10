# Using the quantum-secure APIs

**Framework**: Apple CryptoKit

Enhance your app’s privacy and security by using quantum-secure workflows.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 314: [`Get ahead with quantum-secure cryptography`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/314).

This sample code project demonstrates how to use the quantum-secure APIs, including:

- Post-quantum HPKE with X-Wing
- ML-KEM-768 and ML-KEM-1024
- ML-DSA-65 and ML-DSA-87

It also gives an example of how to build post-quantum hybrid signatures at the application code level.

These workflows store the CryptoKit keys in Keychain by converting between strongly typed cryptographic keys and native Keychain types. Where applicable, they also show how to protect keys with the Secure Enclave.

## See Also

- [Complying with Encryption Export Regulations](../Security/complying-with-encryption-export-regulations.md)
  Declare the use of encryption in your app to streamline the app submission process.
- [Performing Common Cryptographic Operations](performing_common_cryptographic_operations.md)
  Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](storing-cryptokit-keys-in-the-keychain.md)
  Convert between strongly typed cryptographic keys and native keychain types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/using-the-quantum-secure-apis)*