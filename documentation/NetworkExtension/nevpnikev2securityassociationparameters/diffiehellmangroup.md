# diffieHellmanGroup

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The Diffie Hellman group used by the Security Association.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup { get set }
```

```objc
@property NEVPNIKEv2DiffieHellmanGroup diffieHellmanGroup;
```

#### Discussion

The default value of this property is [`NEVPNIKEv2DiffieHellmanGroup.group14`](../nevpnikev2diffiehellmangroup/group14.md).

The value of this property on [`childSecurityAssociationParameters`](../nevpnprotocolikev2/childsecurityassociationparameters.md) of [`NEVPNProtocolIKEv2`](../nevpnprotocolikev2.md) only takes effect if the [`enablePFS`](../nevpnprotocolikev2/enablepfs.md) of [`NEVPNProtocolIKEv2`](../nevpnprotocolikev2.md) is [`true`](../../Swift/true.md) (its default value is [`false`](../../Swift/false.md)).

## See Also

### IKEv2 Security Association parameters
- [var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm](./encryptionalgorithm.md)
  The algorithm used by the Security Association to encrypt and decrypt data.
- [enum NEVPNIKEv2EncryptionAlgorithm](../nevpnikev2encryptionalgorithm.md)
  An enumeration of encryption algorithm values.
- [var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm](./integrityalgorithm.md)
  The algorithm used by the Security Association to verify the integrity of data.
- [enum NEVPNIKEv2IntegrityAlgorithm](../nevpnikev2integrityalgorithm.md)
- [enum NEVPNIKEv2DiffieHellmanGroup](../nevpnikev2diffiehellmangroup.md)
  An enumeration of Diffie-Hellman group values.
- [var lifetimeMinutes: Int32](./lifetimeminutes.md)
  The duration of the lifetime of the Security Association, in minutes.
- [var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod]](./postquantumkeyexchangemethods-3173s.md)
  A list of the quantum-secure key exchange methods the Security Association uses.
- [enum NEVPNIKEv2PostQuantumKeyExchangeMethod](../nevpnikev2postquantumkeyexchangemethod.md)
  Quantum-secure key exchange methods you use with IKEv2 servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters/diffiehellmangroup)*