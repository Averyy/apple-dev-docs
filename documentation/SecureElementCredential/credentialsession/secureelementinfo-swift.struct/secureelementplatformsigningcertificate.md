# secureElementPlatformSigningCertificate

**Framework**: SecureElementCredential  
**Kind**: property

A certificate you use to authenticate against the Certification Authority of the Secure Element hardware.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
let secureElementPlatformSigningCertificate: Data
```

#### Discussion

This certificate contains Controlling Authority Security Domain public key information for authenticating a Secure Element Platform.

For more details, see the Mobile Secure Element specification from [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login).

## See Also

- [let hardwareReleaseVersionInfo: String](credentialsession/secureelementinfo-swift.struct/hardwarereleaseversioninfo.md)
  A string that encodes the hardware and software release versions of the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.struct/secureelementplatformsigningcertificate)*