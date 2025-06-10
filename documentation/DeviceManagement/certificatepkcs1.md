# CertificatePKCS1

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a PKCS #1-formatted certificate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
object CertificatePKCS1
```

#### Discussion

Specify `com.apple.security.pkcs1` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Example Profile

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadContent</key>
            <data>Exam</data>
            <key>PayloadDisplayName</key>
            <string>CertificatePKCS1</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycertpkcs1payload</string>
            <key>PayloadType</key>
            <string>com.apple.security.pkcs1</string>
            <key>PayloadUUID</key>
            <string>72d2c549-2a97-4032-b818-d8ebf7cb88f2</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>CertificatePKCS1</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadType</key>
    <string>com.apple.security.pkcs1</string>
    <key>PayloadUUID</key>
    <string>d7d678c5-87ea-457d-82b9-25db21cd7868</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ACMECertificate](acmecertificate.md)
  The payload you use to configure Automated Certificate Management Environment (ACME) Certificate settings.
- [object ActiveDirectoryCertificate](activedirectorycertificate.md)
  The payload you use to configure Active Directory Certificate settings.
- [object CertificatePEM](certificatepem.md)
  The payload you use to configure a PEM-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload you use to configure a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload you use to configure a root certificate.
- [object CertificatePreference](certificatepreference.md)
  The payload you use to configure a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload you use to configure certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload you use to configure certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatepkcs1)*