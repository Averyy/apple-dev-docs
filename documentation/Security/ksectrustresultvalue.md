# kSecTrustResultValue

**Framework**: Security  
**Kind**: var

A key whose value represents the trust evaluation result.

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
let kSecTrustResultValue: CFString
```

#### Discussion

The key is present after trust evaluation completes. Its value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) that holds one of the values listed in [`SecTrustResultType`](sectrustresulttype.md), indicating the outcome of the trust evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustresultvalue)*