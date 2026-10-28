# kSecTrustExtendedValidation

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kSecTrustExtendedValidation;
```

## Discussion

When the key is present and the value set to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), it indicates the chain is validated for Extended Validation (EV).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustextendedvalidation)*