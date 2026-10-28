# forceKill

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Always set the termination status flag on launch.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var forceKill: SecCodeSignatureFlags { get }
```

```c
kSecCodeSignatureForceKill
```

## Discussion

The `kSecCodeStatusKill` flag indicates that the code wishes to be terminated if it is ever invalidated. Once this is set, it cannot be cleared. Therefore, setting this option flag guarantees that the running code will always be valid, since it will die immediately if it becomes invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodesignatureflags/forcekill)*