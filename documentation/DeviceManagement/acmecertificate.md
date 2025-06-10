# ACMECertificate

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure Automated Certificate Management Environment (ACME) Certificate settings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.1+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
object ACMECertificate
```

#### Discussion

Specify `com.apple.security.acme` as the payload type.

Use this payload to specify settings that allow the device to request a client certificate from an Automated Certificate Management Environment (ACME) server. The device generates an asymmetric key pair based upon the `KeyType`, `KeySize`, and `HardwareBound` fields. If attest is `true` it requests an attestation of the key and device properties. Then it communicates with the ACME server to authenticate the device, provide the attestation, and request a matching certificate based upon the `ClientIdentifier`, `Subject`, `SubjectAltName`, `UsageFlags`, and `ExtendedKeyUsage` fields. The ACME server issues a certificate and the device installs it in the keychain. Other payloads can reference the resulting client identity by the payload’s `PayloadUUID`.

The device issues a new order request using the `ClientIdentifier` as the `permanent-identifier`. For compatibility, the ACME server needs to respond with a challenge type of `device-attest-01`. Then the client replies with a WebAuthn attestation statement.

##### Acme Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support ACME attestation. If the Attest key is false or ignored, the ACME server does not receive an attestation.

| Attest key support | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Must be false | none | T1 and earlier | none | none | none |
| Ignored | A10x Fusion and earlier | T2 | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple Silicon | A12 Bionic and later | S4 and later | All |

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
            <key>ClientIdentifier</key>
            <string>this is an identifier</string>
            <key>ExtendedKeyUsage</key>
            <array>
                <string>1.3.6.1.5.5.7.3.2</string>
            </array>
            <key>HardwareBound</key>
            <true/>
            <key>KeySize</key>
            <integer>384</integer>
            <key>KeyType</key>
            <string>ECSECPrimeRandom</string>
            <key>UsageFlags</key>
            <integer>5</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.myacmepayload</string>
            <key>PayloadType</key>
            <string>com.apple.security.acme</string>
            <key>PayloadUUID</key>
            <string>cbdc6238-feec-4171-878d-34e576bbb813</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>Subject</key>
            <array>
                <array>
                    <array>
                        <string>C</string>
                        <string>US</string>
                    </array>
                </array>
                <array>
                    <array>
                        <string>O</string>
                        <string>Example Inc.</string>
                    </array>
                </array>
                <array>
                    <array>
                        <string>1.2.840.113635.100.6.99999.99999</string>
                        <string>test custom OID value</string>
                    </array>
                </array>
            </array>
            <key>SubjectAltName</key>
            <dict>
                <key>dNSName</key>
                <string>site.example.com</string>
            </dict>
            <key>DirectoryURL</key>
            <string>https://acme.example.com/acme</string>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>ACME</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>ce876f81-abf0-46f9-9e68-9b3a7ede8097</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ACMECertificate.SubjectAltName](acmecertificate/subjectaltname-data.dictionary.md)
  The subject’s alternative name details.

## See Also

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
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/acmecertificate)*