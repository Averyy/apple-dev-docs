# CertificateTransparency

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures certificate transparency enforcement.

**Availability**:
- iOS 12.1.1+
- iPadOS 12.1.1+
- Mac Catalyst 12.1.1+
- macOS 10.14.2+
- tvOS 12.1.1+
- visionOS 1.0+
- watchOS 5.1.1+

## Declaration

```swift
object CertificateTransparency
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)

#### Discussion

Specify `com.apple.security.certificatetransparency` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | N/A |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
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

## Properties

- `DisabledForCerts` ([CertificateTransparency.SubjectPublicKeyInfoHashDict]): An array of certificates for which certificate transparency is disabled. One of the following conditions needs to be met to disable certificate transparency enforcement when this policy is set: - The hash is of the server certificate’s `subjectPublicKeyInfo`.
- The hash is of a `subjectPublicKeyInfo` that appears in a CA certificate in the certificate chain; the CA certificate is constrained through the X.509v3 `nameConstraints` extension. One or more `directoryName` `nameConstraints` are present in the `permittedSubtrees`, and the `directoryName` contains an `organizationName` attribute.
- The hash is of a `subjectPublicKeyInfo` that appears in a CA certificate in the certificate chain. The CA certificate has one or more `organizationName` attributes in the certificate `Subject`, and the server’s certificate contains the same number of `organizationName` attributes, in the same order, and with byte-for-byte identical values.
- `DisabledForDomains` ([string]): An array of strings that represent the domains to exclude from certificate transparency enforcement. The system supports using a leading period (`.`) to signify subdomains. However, the system doesn’t support wildcards. If you include a leading period, the domain can’t be a top-level domain, such as `.com` and `.co.uk`.

## See Also

- [object ACMECertificate](acmecertificate.md)
  The payload that configures Automated Certificate Management Environment (ACME) settings.
- [object ActiveDirectoryCertificate](activedirectorycertificate.md)
  The payload that configures Active Directory Certificate settings.
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
- [object SCEP](scep.md)
  The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/certificatetransparency)*