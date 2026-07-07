# SCEP.PayloadContent

**Framework**: Device Management  
**Kind**: dictionary

The SCEP dictionary.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
object SCEP.PayloadContent
```

## Topics

### Objects
- [object SCEP.PayloadContent.SubjectAltName](scep/payloadcontent-data.dictionary/subjectaltname-data.dictionary.md)
  An optional dictionary that provides values required by the CA for issuing a certificate.

## Properties

- `AllowAllAppsAccess` (boolean): If `true`, all apps have access to the private key. Available: iOS 4+ | iPadOS 4+ | macOS 10.10+ | tvOS 9+ | visionOS 1+ | watchOS 3+
- `CAFingerprint` (data): The fingerprint of the Certificate Authority certificate.
- `Challenge` (string): A preshared secret.
- `Key Type` (string): Always `RSA`.
- `Key Usage` (integer): A bitmask indicating the use of the key. Possible values: - `1`: Signing
- `4`: Encryption Some certificate authorities, such as Windows CA, support only encryption or signing, but not both at the same time. Available: iOS 4+ | iPadOS 4+ | macOS 10.11+ | tvOS 9+ | visionOS 1+ | watchOS 3+
- `KeyIsExtractable` (boolean): If `false`, the system disables exporting the private key from the keychain. Available: iOS 4+ | iPadOS 4+ | macOS 10.13.4+ | tvOS 9+ | visionOS 1+ | watchOS 3+
- `Keysize` (integer): The key size, in bits.
- `Name` (string): A string that’s understood by the SCEP server; for example, a domain name like example.org. If a certificate authority has multiple CA certificates, use this field to distinguish which is required.
- `Retries` (integer): The number of times the device should retry if the server sends a PENDING response. Available: iOS 4+ | iPadOS 4+ | macOS 10.10+ | tvOS 9+ | visionOS 1+ | watchOS 3+
- `RetryDelay` (integer): The number of seconds to wait between subsequent retries. The device attempts the first retry without this delay. Available: iOS 4+ | iPadOS 4+ | macOS 10.10+ | tvOS 9+ | visionOS 1+ | watchOS 3+
- `Subject` ([[[string]]]): The representation of an X.500 name as an array of OID and value. For example, `/C=US/O=Apple Inc./CN=foo/1.2.5.3=bar` translates to `[ [ ["C", "US"] ], [ ["O", "Apple Inc."] ], …, [ [ "1.2.5.3", "bar" ] ] ]`. You can represent OIDs as dotted numbers, with shortcuts for country (C), locality (L), state (ST), organization (O), organizational unit (OU), and common name (CN).
- `SubjectAltName` (SCEP.PayloadContent.SubjectAltName): The SCEP payload can specify an optional `SubjectAltName` dictionary that provides values required by the CA for issuing a certificate. You can specify a single string or an array of strings for each key. The values you specify depend on the CA you’re using, but might include DNS name, URL, or email values. For an example, see Sample Configuration Profile or Over-the-Air Profile Delivery and Configuration.
- `URL` (string) *(required)*: The SCEP URL. See Over-the-Air Profile Delivery and Configuration for more information about SCEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scep/payloadcontent-data.dictionary)*