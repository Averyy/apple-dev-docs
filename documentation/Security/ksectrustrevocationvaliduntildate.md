# kSecTrustRevocationValidUntilDate

**Framework**: Security  
**Kind**: var

A key whose value indicates the earliest date at which revocation information becomes stale.

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
let kSecTrustRevocationValidUntilDate: CFString
```

#### Discussion

This key is only present if the [`kSecTrustRevocationChecked`](ksectrustrevocationchecked.md) key has a value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue). The value is a [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate) representing the earliest date at which the revocation information for one of the certificates in this chain might change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustrevocationvaliduntildate)*