# kAuthorizationEnvironmentShared

**Framework**: Security  
**Kind**: var

The type for an authorization item containing a shared right.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kAuthorizationEnvironmentShared: String { get }
```

#### Discussion

Adding a kAuthorizationEnvironmentShared entry in the environment causes the username and password to be added to the shared credential pool of the calling application’s session. This means that further calls by other applications in this session automatically have this credential available to them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kauthorizationenvironmentshared)*