# CredentialSession.SecureElementInfo

**Framework**: SecureElementCredential  
**Kind**: struct  
**Role**: Structure

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
- [let hardwareReleaseVersionInfo: String](./secureelementinfo-swift.struct/hardwarereleaseversioninfo.md)
  A string that encodes the hardware and software release versions of the Secure Element.
- [let secureElementPlatformSigningCertificate: Data](./secureelementinfo-swift.struct/secureelementplatformsigningcertificate.md)
  A certificate you use to authenticate against the Certification Authority of the Secure Element hardware.
### Instance Properties
- [let platformIdentifier: String](./secureelementinfo-swift.struct/platformidentifier.md)
  A unique identifier that describes the hardware and operating system combination of a device, along with its version information.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)

## See Also

### Accessing hardware information
- [var secureElementInfo: CredentialSession.SecureElementInfo](./secureelementinfo-swift.property.md)
  A property that provides information about the Secure Element hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.struct)*