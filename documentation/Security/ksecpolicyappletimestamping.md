# kSecPolicyAppleTimeStamping

**Framework**: Security  
**Kind**: var

Policy that causes evaluation of the validity of the time stamp on a signature. This can be used to allow verification that a certificate was valid at the time that something was signed with that certificate even if the certificate is no longer valid.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecPolicyAppleTimeStamping: CFString
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecpolicyappletimestamping)*