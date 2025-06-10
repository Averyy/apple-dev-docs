# CertificateTransparency

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure certificate transparency enforcement.

**Availability**:
- iOS 12.1.1+
- iPadOS 12.1.1+
- macOS 10.14.2+
- tvOS 12.1.1+
- visionOS 1.0+
- watchOS 5.1.1+

## Declaration

```swift
object CertificateTransparency
```

#### Discussion

Specify `com.apple.security.certificatetransparency` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | NA |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>DisabledForCerts</key>
            <array>
                <dict>
                    <key>Algorithm</key>
                    <string>sha256</string>
                    <key>Hash</key>
                    <data>AAolBg==</data>
                </dict>
            </array>
            <key>DisabledForDomains</key>
            <array>
                <string>example.com</string>
            </array>
            <key>PayloadDescription</key>
            <string>Configures Certificate Transparency</string>
            <key>PayloadDisplayName</key>
            <string>Domains</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycerttransparencypayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.certificatetransparency</string>
            <key>PayloadUUID</key>
            <string>0ae54b4a-cbf5-4323-8524-262a3cc4b733</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Certificate Transparancy</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>a54d018e-864e-4ec9-9638-85fc50410ae3</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object CertificateTransparency.SubjectPublicKeyInfoHashDict](certificatetransparency/subjectpublickeyinfohashdict.md)
  A dictionary of hashed public keys.

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
- [object CertificatePreference](certificatepreference.md)
  The payload you use to configure a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload you use to configure certificate revocation checking.
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatetransparency)*