# forceHard

**Framework**: Security  
**Kind**: property

Always set the [`hard`](seccodestatus/hard.md) status flag on launch.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var forceHard: SecCodeSignatureFlags { get }
```

#### Discussion

The `kSecCodeStatusHard` flag indicates that the code prefers to be denied access to a resource if gaining such access would cause its invalidation. Once the hard bit is set, it cannot be cleared. Therefore, setting this option flag guarantees that the code will always have the `kSecCodeStatusHard` flag set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodesignatureflags/forcehard)*