# serverCertificateCommonName

**Framework**: Network Extension  
**Kind**: property

A string containing the value of the Subject Common Name field of the IKEv2 server’s certificate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var serverCertificateCommonName: String? { get set }
```

#### Discussion

This string is used to help verify the identity of the IKEv2 server.

## See Also

- [var serverCertificateIssuerCommonName: String?](nevpnprotocolikev2/servercertificateissuercommonname.md)
  A string containing the value of the Subject Common Name field of the Certificate Authority certificate that issued the IKEv2 server’s certificate.
- [var certificateType: NEVPNIKEv2CertificateType](nevpnprotocolikev2/certificatetype.md)
  The type of the certificate in the identity configured in `identityReference` or `identityData`.
- [enum NEVPNIKEv2CertificateType](nevpnikev2certificatetype.md)
  An enumeration of certificate type values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/servercertificatecommonname)*