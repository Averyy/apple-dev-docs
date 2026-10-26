# lifetimeMinutes

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The duration of the lifetime of the Security Association, in minutes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var lifetimeMinutes: Int32 { get set }
```

```objc
@property int32_t lifetimeMinutes;
```

#### Discussion

The default is 60 for IKE Security Associations, and 30 for Child Security Associations. Before the end of the lifetime is reached, IKEv2 will attempt to negotiate new keys for the Security Association in order to maintain the IKEv2 session.

## See Also

### IKEv2 Security Association parameters
- [var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm](./encryptionalgorithm.md)
  The algorithm used by the Security Association to encrypt and decrypt data.
- [enum NEVPNIKEv2EncryptionAlgorithm](../nevpnikev2encryptionalgorithm.md)
  An enumeration of encryption algorithm values.
- [var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm](./integrityalgorithm.md)
  The algorithm used by the Security Association to verify the integrity of data.
- [enum NEVPNIKEv2IntegrityAlgorithm](../nevpnikev2integrityalgorithm.md)
- [var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup](./diffiehellmangroup.md)
  The Diffie Hellman group used by the Security Association.
- [enum NEVPNIKEv2DiffieHellmanGroup](../nevpnikev2diffiehellmangroup.md)
  An enumeration of Diffie-Hellman group values.
- [var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod]](./postquantumkeyexchangemethods-3173s.md)
  A list of the quantum-secure key exchange methods the Security Association uses.
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](../nevpnikev2postquantumkeyexchangemethod.md)
  Quantum-secure key exchange methods you use with IKEv2 servers.
- [postQuantumKeyExchangeMethods](./postquantumkeyexchangemethods-56672.md)
  A list of the quantum-secure key exchange methods the Security Association uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters/lifetimeminutes)*