# NEVPNIKEv2SecurityAssociationParameters

**Framework**: Network Extension  
**Kind**: class

Parameters for an IKEv2 Security Association.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNIKEv2SecurityAssociationParameters
```

## Topics

### IKEv2 Security Association parameters
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
### Instance Properties
- [var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod]](nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-3173s.md)
  The post-quantum key exchange method(s) used by the Security Association, if any.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var ikeSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters](nevpnprotocolikev2/ikesecurityassociationparameters.md)
  An [`NEVPNIKEv2SecurityAssociationParameters`](nevpnikev2securityassociationparameters.md) object containing the parameters for the initial IKE security association to be negotiated with the IKEv2 server.
- [var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters](nevpnprotocolikev2/childsecurityassociationparameters.md)
  An [`NEVPNIKEv2SecurityAssociationParameters`](nevpnikev2securityassociationparameters.md) object containing the parameters for the child IPSec security associations to be negotiated for each IKEv2 policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters)*