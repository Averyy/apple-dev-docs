# NEVPNIKEv2EncryptionAlgorithm

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NEVPNIKEv2EncryptionAlgorithm : NSInteger;
```

## Topics

### Encryption algorithms
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128](./nevpnikev2encryptionalgorithm/algorithmaes128.md)
  Advanced Encryption Standard 256-bit (AES256).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256](./nevpnikev2encryptionalgorithm/algorithmaes256.md)
  Advanced Encryption Standard 256 bit (AES256).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES128GCM](./nevpnikev2encryptionalgorithm/algorithmaes128gcm.md)
  Advanced Encryption Standard 128-bit Galois/Counter Mode (AES128GCM).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmAES256GCM](./nevpnikev2encryptionalgorithm/algorithmaes256gcm.md)
  Advanced Encryption Standard 256-bit Galois/Counter Mode (AES256GCM).
- [NEVPNIKEv2EncryptionAlgorithm.algorithmChaCha20Poly1305](./nevpnikev2encryptionalgorithm/algorithmchacha20poly1305.md)
  ChaCha20 and Poly1305 (ChaCha20Poly1305).
### Initializers
- [init?(rawValue: Int)](./nevpnikev2encryptionalgorithm/init%28rawvalue%29.md)
### Enumeration Cases
- [NEVPNIKEv2EncryptionAlgorithm3DES](./nevpnikev2encryptionalgorithm/nevpnikev2encryptionalgorithm3des.md)
- [NEVPNIKEv2EncryptionAlgorithmDES](./nevpnikev2encryptionalgorithm/nevpnikev2encryptionalgorithmdes.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### IKEv2 Security Association parameters
- [var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm](./nevpnikev2securityassociationparameters/encryptionalgorithm.md)
  The algorithm used by the Security Association to encrypt and decrypt data.
- [var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm](./nevpnikev2securityassociationparameters/integrityalgorithm.md)
  The algorithm used by the Security Association to verify the integrity of data.
- [enum NEVPNIKEv2IntegrityAlgorithm](./nevpnikev2integrityalgorithm.md)
- [var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup](./nevpnikev2securityassociationparameters/diffiehellmangroup.md)
  The Diffie Hellman group used by the Security Association.
- [enum NEVPNIKEv2DiffieHellmanGroup](./nevpnikev2diffiehellmangroup.md)
  An enumeration of Diffie-Hellman group values.
- [var lifetimeMinutes: Int32](./nevpnikev2securityassociationparameters/lifetimeminutes.md)
  The duration of the lifetime of the Security Association, in minutes.
- [var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod]](./nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-3173s.md)
  A list of the quantum-secure key exchange methods the Security Association uses.
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](./nevpnikev2postquantumkeyexchangemethod.md)
  Quantum-secure key exchange methods you use with IKEv2 servers.
- [postQuantumKeyExchangeMethods](./nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-56672.md)
  A list of the quantum-secure key exchange methods the Security Association uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2encryptionalgorithm)*