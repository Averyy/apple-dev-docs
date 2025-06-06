# kSecCSStrictValidate

**Framework**: Security  
**Kind**: var

Perform additional checks to ensure the validity of code in bundle form.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSStrictValidate: UInt32 { get }
```

#### Discussion

For code in bundle form, perform additional checks to verify that the bundle is not structured in a way that would allow tampering, and reject any resource envelope that introduces weaknesses into the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccsstrictvalidate)*