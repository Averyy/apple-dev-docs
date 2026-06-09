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
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
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

## Properties

- `AllowAllAppsAccess` (boolean): If `true`, gives apps access to the private key. Available: macOS 10.10+
- `CertificateAcquisitionMechanism` (string): This value is most commonly `RPC`; if using web enrollment, use `HTTP`. Available: macOS 10.8+
- `CertificateAuthority` (string): The name of the certificate authority (CA), which is determined from the common name (CN) of the Active Directory entry. Valid values: - CN=
- CN=`Certification Authorities`
- CN=`Public Key Services`
- CN=`Services`
- CN=`Configuration`
- CN= Available: macOS 10.8+
- `CertificateRenewalTimeInterval` (integer): The number of days in advance of certificate expiration that the notification center notifies the user.
- `CertServer` (string) *(required)*: The fully qualified host name of the CA.
- `CertTemplate` (string) *(required)*: The certificate template for your environment. The default user certificate value is `User`. The default computer certificate value is `Machine`.
- `Description` (string): A user-friendly description of the certification identity.
- `EnableAutoRenewal` (boolean): If `true`, the certificate obtained with this payload attempts auto-renewal. Auto-renewal can only be used with device Active Directory certificate payloads. Available: macOS 10.13.4+
- `KeyIsExtractable` (boolean): If `true`, the system allows exporting the private key. Available: macOS 10.10+
- `Keysize` (integer): The RSA key size for the certificate signing request (CSR). Available: macOS 10.11+
- `PromptForCredentials` (boolean): If `true`, the system prompts the user for credentials when is installs the profile. This key applies only to user certificates with the Manual Download profile delivery method. Omit this key for computer certificates. Available: macOS 10.8+

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