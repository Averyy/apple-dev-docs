# kSecTrustSettingsKeyUsage

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A number specifying the operations for which the encryption key in this certificate can be used.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecTrustSettingsKeyUsage: String { get }
```

```c
#define kSecTrustSettingsKeyUsage
```

#### Discussion

The value is a [`CFNumber`](../CoreFoundation/cfnumber.md) object containing an `SInt32` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingskeyusage)*