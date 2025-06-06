# forceExpiration

**Framework**: Security  
**Kind**: property

Always set the [`considerExpiration`](seccsflags/considerexpiration.md) flag when validating the code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var forceExpiration: SecCodeSignatureFlags { get }
```

#### Discussion

When passed to a function that performs code validation, the `kSecCSConsiderExpiration` flag requests that code signatures made by expired certificates be rejected. By default, expiration of participating certificates is not automatic grounds for rejection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodesignatureflags/forceexpiration)*