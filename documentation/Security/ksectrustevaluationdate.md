# kSecTrustEvaluationDate

**Framework**: Security  
**Kind**: var

A key whose value indicates the time that the trust evaluation took place.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecTrustEvaluationDate: CFString
```

#### Discussion

This key is present after the results become available from performing the trust evaluation. The value is a [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate) object representing when the evaluation took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustevaluationdate)*