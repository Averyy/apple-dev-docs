# host

**Framework**: Security  
**Kind**: property

May host guest code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var host: SecCodeSignatureFlags { get }
```

#### Discussion

Indicates that the code may act as a host that controls and supervises guest code. If this flag is not set in a code signature, the code is never considered eligible to be a host, and any attempt to act like one is ignored or rejected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodesignatureflags/host)*