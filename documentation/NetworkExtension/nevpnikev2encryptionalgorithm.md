# NEVPNIKEv2EncryptionAlgorithm

**Framework**: Network Extension  
**Kind**: enum

An enumeration of encryption algorithm values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNIKEv2EncryptionAlgorithm
```

## Topics

### Encryption algorithms
- [NEVPNIKEv2EncryptionAlgorithm.algorithmDES](nevpnikev2encryptionalgorithm/algorithmdes.md)
  Data Encryption Standard (DES)
- [NEVPNIKEv2EncryptionAlgorithm.algorithm3DES](nevpnikev2encryptionalgorithm/algorithm3des.md)
  Triple Data Encryption Algorithm (aka 3DES)
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128](nevpnikev2encryptionalgorithm/algorithmaes128.md)
  Advanced Encryption Standard 256-bit (AES256).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256](nevpnikev2encryptionalgorithm/algorithmaes256.md)
  Advanced Encryption Standard 256 bit (AES256).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128GCM](nevpnikev2encryptionalgorithm/algorithmaes128gcm.md)
  Advanced Encryption Standard 128-bit Galois/Counter Mode (AES128GCM).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256GCM](nevpnikev2encryptionalgorithm/algorithmaes256gcm.md)
  Advanced Encryption Standard 256-bit Galois/Counter Mode (AES256GCM).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmChaCha20Poly1305](nevpnikev2encryptionalgorithm/algorithmchacha20poly1305.md)
  ChaCha20 and Poly1305 (ChaCha20Poly1305).
### Initializers
- [init?(rawValue: Int)](nevpnikev2encryptionalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm](nevpnikev2securityassociationparameters/encryptionalgorithm.md)
  The algorithm used by the Security Association to encrypt and decrypt data.
- [var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm](nevpnikev2securityassociationparameters/integrityalgorithm.md)
  The algorithm used by the Security Association to verify the integrity of data.
- [enum NEVPNIKEv2IntegrityAlgorithm](nevpnikev2integrityalgorithm.md)
- [var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup](nevpnikev2securityassociationparameters/diffiehellmangroup.md)
  The Diffie Hellman group used by the Security Association.
- [enum NEVPNIKEv2DiffieHellmanGroup](nevpnikev2diffiehellmangroup.md)
  An enumeration of Diffie-Hellman group values.
- [var lifetimeMinutes: Int32](nevpnikev2securityassociationparameters/lifetimeminutes.md)
  The duration of the lifetime of the Security Association, in minutes.
- [var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod]](nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-3173s.md)
  A list of the quantum-secure key exchange methods the Security Association uses.
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](nevpnikev2postquantumkeyexchangemethod.md)
  Quantum-secure key exchange methods you use with IKEv2 servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm)*