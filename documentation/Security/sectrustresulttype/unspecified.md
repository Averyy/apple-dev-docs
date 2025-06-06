# SecTrustResultType.unspecified

**Framework**: Security  
**Kind**: case

The user did not specify a trust setting.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case unspecified
```

#### Discussion

This value indicates that evaluation reached an (implicitly trusted) anchor certificate without any evaluation failures, but never encountered any explicitly stated user-trust preference. This is the most common return value. The Keychain Access utility refers to this value as the “Use System Policy,” which is the default user setting.

When receiving this value, most apps should trust the chain. If you want to ask the user what to do in macOS, use an instance of the [`SFCertificateTrustPanel`](https://developer.apple.com/documentation/SecurityInterface/SFCertificateTrustPanel) class.

When you evaluate a trust, the evaluation starts with the leaf certificate and works through the chain down to the anchor. The [`SecTrustSettingsCopyTrustSettings(_:_:_:)`](sectrustsettingscopytrustsettings(_:_:_:).md) method returns the user trust settings of the first certificate for which the result code is other than [`SecTrustResultType.unspecified`](sectrustresulttype/unspecified.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustresulttype/unspecified)*