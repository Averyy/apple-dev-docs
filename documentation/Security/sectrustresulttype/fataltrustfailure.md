# SecTrustResultType.fatalTrustFailure

**Framework**: Security  
**Kind**: case

Trust is denied and no simple fix is available.

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
case fatalTrustFailure
```

#### Discussion

This value indicates that evaluation failed because a certificate in the chain is defective. This usually represents a fundamental defect in the certificate data, such as an invalid encoding for a critical `subjectAltName` extension, an unsupported critical extension, or some other critical portion of the certificate that couldn’t be interpreted. Changing parameter values and reevaluating is unlikely to succeed unless you provide different certificates.

You might receive the [`SecTrustResultType.fatalTrustFailure`](sectrustresulttype/fataltrustfailure.md) value after an evaluation, but you can’t store the value as part of the user trust settings with a call to the [`SecTrustSettingsSetTrustSettings(_:_:_:)`](sectrustsettingssettrustsettings(_:_:_:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustresulttype/fataltrustfailure)*