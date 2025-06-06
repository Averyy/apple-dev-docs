# certificateType

**Framework**: Network Extension  
**Kind**: property

The type of the certificate in the identity configured in `identityReference` or `identityData`.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var certificateType: NEVPNIKEv2CertificateType { get set }
```

#### Discussion

The default value is [`NEVPNIKEv2CertificateType.RSA`](nevpnikev2certificatetype/rsa.md).

## See Also

- [var serverCertificateIssuerCommonName: String?](nevpnprotocolikev2/servercertificateissuercommonname.md)
  A string containing the value of the Subject Common Name field of the Certificate Authority certificate that issued the IKEv2 server’s certificate.
- [var serverCertificateCommonName: String?](nevpnprotocolikev2/servercertificatecommonname.md)
  A string containing the value of the Subject Common Name field of the IKEv2 server’s certificate.
- [enum NEVPNIKEv2CertificateType](nevpnikev2certificatetype.md)
  An enumeration of certificate type values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/certificatetype)*