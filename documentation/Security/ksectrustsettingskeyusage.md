# kSecTrustSettingsKeyUsage

**Framework**: Security  
**Kind**: var

A number specifying the operations for which the encryption key in this certificate can be used.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecTrustSettingsKeyUsage: String { get }
```

#### Discussion

The value is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object containing an `SInt32` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingskeyusage)*