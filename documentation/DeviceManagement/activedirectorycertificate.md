# ActiveDirectoryCertificate

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Active Directory Certificate settings.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ActiveDirectoryCertificate
```

#### Discussion

Specify `com.apple.ADCertificate.managed` as the payload type.

To get a certificate from a Microsoft CA, follow the instructions at [`Request a certificate from a Microsoft Certificate Authority`](https://developer.apple.comhttps://support.apple.com/en-us/HT204602).

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | macOS |
| Allow Multiple Payloads | macOS |

##### Example Profile

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>CertServer</key>
            <string>server.example.com</string>
            <key>CertTemplate</key>
            <string>MachineUser</string>
            <key>CertificateAcquisitionMechanism</key>
            <string>RPC</string>
            <key>CertificateAuthority</key>
            <string>Example</string>
            <key>Description</key>
            <string>Active Directory Certificate</string>
            <key>PromptForCredentials</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.myADcertpayload</string>
            <key>PayloadType</key>
            <string>com.apple.myadcertificate.managed</string>
            <key>PayloadUUID</key>
            <string>59729e65-4c09-4fa1-b367-7a38cfd1b190</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Active Directory Certificate</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>com.apple.ADCertificate.managed</string>
    <key>PayloadUUID</key>
    <string>55a22a34-02b7-49d8-8116-ea95c3545261</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ACMECertificate](acmecertificate.md)
  The payload you use to configure Automated Certificate Management Environment (ACME) Certificate settings.
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
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activedirectorycertificate)*