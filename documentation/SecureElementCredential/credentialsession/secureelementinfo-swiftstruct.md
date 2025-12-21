# CredentialSession.SecureElementInfo

**Framework**: SecureElementCredential  
**Kind**: struct

A type that provides information about the Secure Element hardware.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
struct SecureElementInfo
```

## Topics

### Getting hardware information
- [let hardwareReleaseVersionInfo: String](credentialsession/secureelementinfo-swift.struct/hardwarereleaseversioninfo.md)
  A string that encodes the hardware and software release versions of the Secure Element.
- [let secureElementPlatformSigningCertificate: Data](credentialsession/secureelementinfo-swift.struct/secureelementplatformsigningcertificate.md)
  A certificate you use to authenticate against the Certification Authority of the Secure Element hardware.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [var secureElementInfo: CredentialSession.SecureElementInfo](credentialsession/secureelementinfo-swift.property.md)
  A property that provides information about the Secure Element hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.struct)*