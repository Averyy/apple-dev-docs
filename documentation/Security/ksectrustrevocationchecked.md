# kSecTrustRevocationChecked

**Framework**: Security  
**Kind**: var

A key whose value indicates the outcome of revocation checking during trust evaluation.

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
let kSecTrustRevocationChecked: CFString
```

#### Discussion

This key is only present if the evaluation process conducted revocation checking on the chain. The value is a Boolean set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) if revocation checking was successful and none of the certificates in the chain were revoked. The value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) if no current revocation status could be obtained for one or more certificates in the chain due to connection problems or timeouts. You can take this outcome as a hint to retry revocation checking again at a later time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustrevocationchecked)*