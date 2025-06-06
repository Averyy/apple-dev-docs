# NEVPNIKEv2IntegrityAlgorithm

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNIKEv2IntegrityAlgorithm
```

## Topics

### Integrity algorithms
- [NEVPNIKEv2IntegrityAlgorithm.SHA96](nevpnikev2integrityalgorithm/sha96.md)
  SHA-1 96-bit.
- [NEVPNIKEv2IntegrityAlgorithm.SHA160](nevpnikev2integrityalgorithm/sha160.md)
  SHA-1 160-bit.
- [NEVPNIKEv2IntegrityAlgorithm.SHA256](nevpnikev2integrityalgorithm/sha256.md)
  SHA-2 256-bit.
- [NEVPNIKEv2IntegrityAlgorithm.SHA384](nevpnikev2integrityalgorithm/sha384.md)
  SHA-2 384-bit.
- [NEVPNIKEv2IntegrityAlgorithm.SHA512](nevpnikev2integrityalgorithm/sha512.md)
  SHA-2 512-bit.
### Initializers
- [init?(rawValue: Int)](nevpnikev2integrityalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var encryptionAlgorithm: NEVPNIKEv2EncryptionAlgorithm](nevpnikev2securityassociationparameters/encryptionalgorithm.md)
  The algorithm used by the Security Association to encrypt and decrypt data.
- [enum NEVPNIKEv2EncryptionAlgorithm](nevpnikev2encryptionalgorithm.md)
  An enumeration of encryption algorithm values.
- [var integrityAlgorithm: NEVPNIKEv2IntegrityAlgorithm](nevpnikev2securityassociationparameters/integrityalgorithm.md)
  The algorithm used by the Security Association to verify the integrity of data.
- [var diffieHellmanGroup: NEVPNIKEv2DiffieHellmanGroup](nevpnikev2securityassociationparameters/diffiehellmangroup.md)
  The Diffie Hellman group used by the Security Association.
- [enum NEVPNIKEv2DiffieHellmanGroup](nevpnikev2diffiehellmangroup.md)
  An enumeration of Diffie-Hellman group values.
- [var lifetimeMinutes: Int32](nevpnikev2securityassociationparameters/lifetimeminutes.md)
  The duration of the lifetime of the Security Association, in minutes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2integrityalgorithm)*