# AuthorizationResult

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The permissible values for an authorization evaluation result.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum AuthorizationResult : UInt32;
```

## Topics

### Constants
- [kAuthorizationResultAllow](./authorizationresult/kauthorizationresultallow.md)
  The authorization operation succeeded and authorization should be granted.
- [kAuthorizationResultDeny](./authorizationresult/kauthorizationresultdeny.md)
  The authorization operation succeeded and authorization should be denied.
- [kAuthorizationResultUndefined](./authorizationresult/kauthorizationresultundefined.md)
  The authorization operation failed and should not be retried for this session.
- [kAuthorizationResultUserCanceled](./authorizationresult/kauthorizationresultusercanceled.md)
  The user has requested that the authorization evaluation be terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationresult)*