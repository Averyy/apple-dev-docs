# CertificatePreference

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a certificate preference.

**Availability**:
- macOS 10.12+

## Declaration

```swift
object CertificatePreference
```

#### Discussion

Specify `com.apple.security.certificatepreference` as the payload type.

A `CertificatePreference` payload lets you identify a certificate preference item in the user’s keychain that references a certificate payload included in the same profile. It can only appear in a user profile, not a device profile. You can include multiple `CertificatePreference` payloads as needed.

See also [`IdentityPreference`](identitypreference.md)  for information about setting up identity preferences.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | NA |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | macOS |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>Password</key>
            <string>Password123</string>
            <key>PayloadContent</key>
            <data>ExampleD</data>
            <key>PayloadIdentifier</key>
            <string>com.example.mypcertprefpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.certificatepreference</string>
            <key>PayloadUUID</key>
            <string>d669e184-6312-4214-9ebc-00346809f7f0</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>updated_at_xid</key>
            <integer>23387</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Certificate Preferences</string>
    <key>PayloadIdentifier</key>
    <string>com.example.profile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>89d2e0a7-0821-45c2-a566-c23eb98b137e</string>
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
- [object CertificatePKCS1](certificatepkcs1.md)
  The payload you use to configure a PKCS #1-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload you use to configure a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload you use to configure a root certificate.
- [object CertificateRevocation](certificaterevocation.md)
  The payload you use to configure certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload you use to configure certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatepreference)*