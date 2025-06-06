# CertificateRevocation

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure certificate revocation checking.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object CertificateRevocation
```

#### Discussion

Specify `com.apple.security.certificaterevocation` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad |
| User Channel | - |
| Allow Manual Install | iOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS |
| Allow Multiple Payloads | iOS, Shared iPad |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>EnabledForCerts</key>
            <array>
                <dict>
                    <key>Algorithm</key>
                    <string>sha256</string>
                    <key>Hash</key>
                    <data>ExampleDatY=</data>
                </dict>
            </array>
            <key>PayloadDescription</key>
            <string>Configures certificate Revocation</string>
            <key>PayloadDisplayName</key>
            <string>Certificate Revocation</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mycertrevpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.certificaterevocation</string>
            <key>PayloadUUID</key>
            <string>2a4deb38-4c9f-43fd-a933-6598f4866e3b</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Certificate Revocation</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b548e6df-10ad-438a-a65b-6b39374b7aff</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object CertificateRevocation.SubjectPublicKeyInfoHashDict](certificaterevocation/subjectpublickeyinfohashdict.md)
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
- [object CertificateTransparency](certificatetransparency.md)
  The payload you use to configure certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificaterevocation)*