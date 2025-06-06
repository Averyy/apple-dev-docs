# kSecTrustSettingsPolicyString

**Framework**: Security  
**Kind**: var

A string containing policy-specific data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecTrustSettingsPolicyString: String { get }
```

#### Discussion

The value is a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) object. For the SMIME policy, this string contains an email address. For the SSL policy, it contains a host name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingspolicystring)*