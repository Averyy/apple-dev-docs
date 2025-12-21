# postQuantumKeyExchangeMethods

**Framework**: Network Extension  
**Kind**: property

A list of the quantum-secure key exchange methods the Security Association uses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod] { get set }
```

#### Discussion

You can specify up to seven key-exchange methods, which correspond to the Additional Key Exchange transform types `ADDKE1`–`ADDKE7` in RFC 9370.

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
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](nevpnikev2postquantumkeyexchangemethod.md)
  Quantum-secure key exchange methods you use with IKEv2 servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-3173s)*