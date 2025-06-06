# hardwareReleaseVersionInfo

**Framework**: SecureElementCredential  
**Kind**: property

A string that encodes the hardware and software release versions of the Secure Element.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
let hardwareReleaseVersionInfo: String
```

#### Discussion

Use this string to determine eligibility or select which applet bundle, previously submitted to [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login) (ABR), to install on this device.

This string uses the format `"JCOP X.Y"`, with the following semantics:

For more details, see the Mobile Secure Element specification from [`Apple Business Register`](https://developer.apple.comhttps://register.apple.com/login).

## See Also

- [let secureElementPlatformSigningCertificate: Data](credentialsession/secureelementinfo-swift.struct/secureelementplatformsigningcertificate.md)
  A certificate you use to authenticate against the Certification Authority of the Secure Element hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.struct/hardwarereleaseversioninfo)*