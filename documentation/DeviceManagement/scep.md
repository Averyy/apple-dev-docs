# SCEP

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SCEP
```

#### Discussion

Specify `com.apple.security.scep` as the payload type.

An SCEP payload automates the request of a client certificate from an SCEP server, as described in [`Over-the-Air Profile Delivery and Configuration`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html).

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | macOS |
| Allow Manual Install | iOS, macOS, tvOS, watchOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | iOS, macOS |
| Allow Multiple Payloads | iOS, macOS, Shared iPad, tvOS, watchOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadContent</key>
            <dict>
                <key>Challenge</key>
                <string>Example</string>
                <key>Key Type</key>
                <string>RSA</string>
                <key>Key Usage</key>
                <integer>5</integer>
                <key>Keysize</key>
                <integer>0</integer>
                <key>Name</key>
                <string>example.org</string>
                <key>Subject</key>
                <array>
                    <array>
                        <array>
                            <string>C</string>
                            <string>US</string>
                        </array>
                        <array>
                            <string>O</string>
                            <string>Example Inc.</string>
                        </array>
                        <array>
                            <string>CN</string>
                            <string>foo</string>
                        </array>
                        <array>
                            <string>1.2.5.3</string>
                            <string>bar</string>
                        </array>
                    </array>
                </array>
                <key>SubjectAltName</key>
                <dict>
                    <key>dNSName</key>
                    <string>example.com</string>
                    <key>ntPrincipalName</key>
                    <string>hostname.example.com</string>
                </dict>
                <key>URL</key>
                <string>https://hostname.example.com/</string>
            </dict>
            <key>PayloadIdentifier</key>
            <string>com.example.myscepcertpayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.scep</string>
            <key>PayloadUUID</key>
            <string>c0264fd7-1d89-4385-8806-759fbe78a622</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>SCEP Certificate</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>bc0328a9-c199-4572-9e5e-ed59a73454fa</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Supporting Objects
- [object SCEP.PayloadContent](scep/payloadcontent-data.dictionary.md)
  The SCEP dictionary.
- [object SCEP.PayloadContent.SubjectAltName](scep/payloadcontent-data.dictionary/subjectaltname-data.dictionary.md)
  An optional dictionary that provides values required by the CA for issuing a certificate.

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
- [object CertificateTransparency](certificatetransparency.md)
  The payload you use to configure certificate transparency enforcement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scep)*