# kSecTrustExtendedValidation

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean used to indicate Extended Validation.

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
let kSecTrustExtendedValidation: CFString
```

#### Discussion

When the key is present and the value set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), it indicates the chain is validated for Extended Validation (EV).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustextendedvalidation)*