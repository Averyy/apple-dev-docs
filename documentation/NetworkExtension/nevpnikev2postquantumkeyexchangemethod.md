# NEVPNIKEv2PostQuantumKeyExchangeMethod

**Framework**: Network Extension  
**Kind**: enum

Quantum-secure key exchange methods you use with IKEv2 servers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NEVPNIKEv2PostQuantumKeyExchangeMethod
```

## Topics

### Key exchange methods
- [NEVPNIKEv2PostQuantumKeyExchangeMethod.method36](nevpnikev2postquantumkeyexchangemethod/method36.md)
  Instructs the server to use the ML-KEM-768 key exchange method.
- [NEVPNIKEv2PostQuantumKeyExchangeMethod.method37](nevpnikev2postquantumkeyexchangemethod/method37.md)
  Instructs the server to use the ML-KEM-1024 key exchange method.
- [NEVPNIKEv2PostQuantumKeyExchangeMethod.methodNone](nevpnikev2postquantumkeyexchangemethod/methodnone.md)
  Instructs the server not to use a quantum-secure key exchange method.
### Initializers
- [init?(rawValue: Int)](nevpnikev2postquantumkeyexchangemethod/init(rawvalue:).md)

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
- [enum NEVPNIKEv2EncryptionAlgorithm](nevpnikev2encryptionalgorithm.md)
  An enumeration of encryption algorithm values.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2postquantumkeyexchangemethod)*