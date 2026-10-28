# kSecTrustSettingsAllowedError

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A number which, if encountered during certificate verification, is ignored for that certificate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecTrustSettingsAllowedError: String { get }
```

```c
#define kSecTrustSettingsAllowedError
```

## Discussion

The value is a [`CFNumber`](../CoreFoundation/cfnumber.md) object containing an `SInt32` value indicating a `CSSM_RETURN` result code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingsallowederror)*