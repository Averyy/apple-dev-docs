# ACMECertificate

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Automated Certificate Management Environment (ACME) settings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.1+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
object ACMECertificate
```

## Mentions

- [Implementing Platform SSO during Automated Device Enrollment](implementing-platform-sso-during-automated-device-enrollment.md)
- [Validating a Managed Device Attestation](validating-a-managed-device-attestation-attestation.md)

#### Discussion

Specify `com.apple.security.acme` as the payload type.

Use this payload to specify how the device requests a client certificate from an Automated Certificate Management Environment (ACME) server. Other payloads can reference the resulting client identity by the payload’s `PayloadUUID`.

First the device generates an asymmetric key pair based upon the `KeyType`, `KeySize`, and `HardwareBound` fields. Then the device communicates with the ACME server. It requests a new order using the `ClientIdentifier` as the `permanent-identifier`. The ACME server responds with a challenge type of `device-attest-01`. If `Attest` is `true` the device requests an attestation of the key and device properties. Then it replies to the challenge with a WebAuthn attestation statement, and this contains the attestation if the device obtained one. The device submits a certificate signing request matching the key and containing the `ClientIdentifier`, `Subject`, `SubjectAltName`, `UsageFlags`, and `ExtendedKeyUsage` fields. The ACME server issues a certificate, and the device stores the resulting identity.

For details on the content of the attestation provided to the ACME server, see the documentation of the `DevicePropertiesAttestation` key in the [`DeviceInformationResponse.QueryResponses`](deviceinformationresponse/queryresponses-data.dictionary.md)response. In the attestation certificate the value of the freshness code OID is the SHA-256 hash of the `token` from the `device-attest-01` challenge.

##### Acme Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support ACME attestation. If the Attest key is false or ignored, the ACME server does not receive an attestation.

| Attest key support | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Must be false | none | T1 and earlier | none | none | none |
| Ignored | A10x Fusion and earlier | T2 | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple silicon | A12 Bionic and later | S4 and later | All |

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, tvOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
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

## Properties

- `AllowAllAppsAccess` (boolean): If `true`, all apps have access to the private key. Available: macOS 13.1+
- `Attest` (boolean): If `true`, the device provides attestations that describe the device and the generated key to the ACME server. The server can use the attestations as strong evidence that the key is bound to the device, and that the device has properties listed in the attestation. The server can use that as part of a trust score to decide whether to issue the requested certificate. When `Attest` is `true`, `HardwareBound` also needs to be `true`. macOS 14 supports setting this key to `true`. Older macOS versions require this key but it must have a value of `false`. See below for hardware requirements. Available: iOS 16+ | iPadOS 16+ | macOS 13.1+ | tvOS 16+ | visionOS 1+ | watchOS 10+
- `ClientIdentifier` (string) *(required)*: A unique string identifying a specific device. The server may use this as an anti-replay code to prevent issuing multiple certificates. This identifier also indicates to the ACME server that the device has access to a valid client identifier issued by the enterprise infrastructure. This can help the ACME server determine whether to trust the device. Though this is a relatively weak indication because of the risk that an attacker can intercept the client identifier.
- `DirectoryURL` (string) *(required)*: The directory URL of the ACME server. The URL must use the https scheme.
- `ExtendedKeyUsage` ([string]): The value is an array of strings. Each string is an OID in dotted notation. For instance, `["1.3.6.1.5.5.7.3.2", "1.3.6.1.5.5.7.3.4"]` indicates client authentication and email protection. The device requests this field for the certificate that the ACME server issues. The ACME server may override or ignore this field in the certificate it issues.
- `HardwareBound` (boolean) *(required)*: If `false`, the private key isn’t bound to the device. If `true`, the private key is bound to the device. The Secure Enclave generates the key pair, and the private key is cryptographically entangled with a system key. This prevents the system from exporting the private key. If `true`, `KeyType` must be `ECSECPrimeRandom` and `KeySize` must be 256 or 384. macOS 14 on Apple silicon and Intel devices that have a T2 chip support setting this key to `true`. Older macOS versions or other Mac devices require this key but it must have a value of `false`.
- `KeyIsExtractable` (boolean): If `false`, the device tags the private key of the identity obtained through Automated Certificate Management Environment (ACME) as “non-extractable” in the keychain. Available: macOS 13.1+
- `KeySize` (integer) *(required)*: The valid values for `KeySize` depend on the values of `KeyType` and `HardwareBound`. See those keys for specific requirements.
- `KeyType` (string) *(required)*: The type of key pair to generate. Allowed values: - `RSA`: Specifies an RSA key pair. RSA key pairs need to have a `KeySize` that’s a multiple of 8 in the range of 1024 through 4096 (inclusive), and `HardwareBound` needs to be `false`.
- `ECSECPrimeRandom`: Specifies a key pair on the P-192, P-256, P-384, or P-521 curves as defined in FIPS Pub 186-4. `KeySize` defines the particular curve, which needs to be `192`, `256`, `384`, or `521`. Hardware bound keys only support values of `256` and `384`. > **Note**:  The key size is `521`, not `512`, even though the other key sizes are multiples of 64.
- `Subject` ([[[string]]]) *(required)*: The device requests this subject for the certificate that the ACME server issues. The ACME server may override or ignore this field in the certificate it issues. The representation of a X.500 name represented as an array of OID and value. For example, `/C=US/O=Apple Inc./CN=foo/1.2.5.3=bar` corresponds to: `[ [ ["C", "US"] ], [ ["O", "Apple Inc."] ], ..., [ [ "1.2.5.3", "bar" ] ] ]` Dotted numbers can represent OIDs , with shortcuts for country (C), locality (L), state (ST), organization (O), organizational unit (OU), and common name (CN).
- `SubjectAltName` (ACMECertificate.SubjectAltName): The Subject Alt Name that the device requests for the certificate that the ACME server issues. The ACME server may override or ignore this field in the certificate it issues.
- `UsageFlags` (integer): This value is a bit field. - Bit `0x01` indicates digital signature.
- Bit `0x04` indicates encryption. The device requests this key for the certificate that the ACME server issues. The ACME server may override or ignore this field in the certificate it issues.

## See Also

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
- [object CertificateTransparency](certificatetransparency.md)
  The payload that configures certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/acmecertificate)*