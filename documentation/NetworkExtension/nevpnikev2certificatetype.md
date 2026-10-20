# NEVPNIKEv2CertificateType

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

An enumeration of certificate type values.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNIKEv2CertificateType
```

```c
enum NEVPNIKEv2CertificateType : NSInteger;
```

## Topics

### Certificate types
- [NEVPNIKEv2CertificateType.RSA](./nevpnikev2certificatetype/rsa.md)
  The RSA certificate type.
- [NEVPNIKEv2CertificateType.ECDSA256](./nevpnikev2certificatetype/ecdsa256.md)
  The ECDSA with p-256 curve certificate type.
- [NEVPNIKEv2CertificateType.ECDSA384](./nevpnikev2certificatetype/ecdsa384.md)
  The ECDSA with p-384 curve certificate type.
- [NEVPNIKEv2CertificateType.ECDSA521](./nevpnikev2certificatetype/ecdsa521.md)
  The ECDSA with p-521 curve certificate type.
- [NEVPNIKEv2CertificateType.ed25519](./nevpnikev2certificatetype/ed25519.md)
  The Edwards 25519 curve certificate type.
- [NEVPNIKEv2CertificateType.RSAPSS](./nevpnikev2certificatetype/rsapss.md)
  The RSA-PSS certificate type.
### Initializers
- [init?(rawValue: Int)](./nevpnikev2certificatetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing certificate properties
- [var serverCertificateIssuerCommonName: String?](./nevpnprotocolikev2/servercertificateissuercommonname.md)
  A string containing the value of the Subject Common Name field of the Certificate Authority certificate that issued the IKEv2 server’s certificate.
- [var serverCertificateCommonName: String?](./nevpnprotocolikev2/servercertificatecommonname.md)
  A string containing the value of the Subject Common Name field of the IKEv2 server’s certificate.
- [var certificateType: NEVPNIKEv2CertificateType](./nevpnprotocolikev2/certificatetype.md)
  The type of the certificate in the identity configured in `identityReference` or `identityData`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2certificatetype)*