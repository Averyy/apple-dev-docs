# encryptionAlgorithm

**Framework**: Network Extension  
**Kind**: property

The algorithm used by the Security Association to encrypt and decrypt data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm { get set }
```

#### Discussion

The default value of this property is [`NEVPNIKEv2EncryptionAlgorithm.algorithmAES256`](nevpnikev2encryptionalgorithm/algorithmaes256.md), except on tvOS where the default is [`NEVPNIKEv2EncryptionAlgorithm.algorithmAES256GCM`](nevpnikev2encryptionalgorithm/algorithmaes256gcm.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters/encryptionalgorithm)*