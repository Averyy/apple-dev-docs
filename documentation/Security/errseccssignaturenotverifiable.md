# errSecCSSignatureNotVerifiable

**Framework**: Security  
**Kind**: var

Signature cannot be read.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSSignatureNotVerifiable: OSStatus { get }
```

#### Discussion

This error might be due to a filesystem that maps root to an unprivileged user, for example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccssignaturenotverifiable)*