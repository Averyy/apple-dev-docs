# ActiveDirectoryCertificate

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Active Directory Certificate settings.

**Availability**:
- macOS 10.7+

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
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | macOS |
| Allow multiple payloads | macOS |

##### Example Profile

```plist
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
  The payload that configures Automated Certificate Management Environment (ACME) settings.
- [object CertificatePEM](certificatepem.md)
  The payload that configures a PEM-formatted certificate.
- [object CertificatePKCS1](certificatepkcs1.md)
  The payload that configures a PKCS #1-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload that configures a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload that configures a root certificate.
- [object CertificatePreference](certificatepreference.md)
  The payload that configures a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload that configures certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload that configures certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activedirectorycertificate)*