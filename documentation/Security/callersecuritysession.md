# callerSecuritySession

**Framework**: Security  
**Kind**: var

A value that is a placeholder for the caller’s session.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var callerSecuritySession: SecuritySessionId { get }
```

#### Discussion

When you provide this value as the `session` input to the [`SessionGetInfo(_:_:_:)`](sessiongetinfo(_:_:_:).md) function, the function will return the actual session ID via the `sessionId` output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/callersecuritysession)*