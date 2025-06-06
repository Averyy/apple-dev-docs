# errSecCSHostReject

**Framework**: Security  
**Kind**: var

Code rejected its host.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSHostReject: OSStatus { get }
```

#### Discussion

This error indicates that there’s an internal requirement in the signature on the guest code that specifies conditions that the code host must meet, and the host failed to meet that requirement. For example, if the guest requires that the host be signed by Apple and it wasn’t, the system returns this error when validating requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccshostreject)*