# Sessions

**Framework**: Security

Manage login, authorization, and security sessions in macOS.

#### Overview

Use the `Security.AuthSession` API to work with session management and inquiry functions.

## Topics

### Creating a Session
- [func SessionCreate(SessionCreationFlags, SessionAttributeBits) -> OSStatus](sessioncreate(_:_:).md)
  Creates a security session.
- [struct SessionCreationFlags](sessioncreationflags.md)
  The flags that affect the creation of a security session.
- [struct SessionAttributeBits](sessionattributebits.md)
  The attributes of a security session.
### Session Information
- [func SessionGetInfo(SecuritySessionId, UnsafeMutablePointer<SecuritySessionId>?, UnsafeMutablePointer<SessionAttributeBits>?) -> OSStatus](sessiongetinfo(_:_:_:).md)
  Obtains information about a security session.
- [Session ID Values](session-id-values.md)
  Use these values as placeholders for specific sessions.
- [typealias SecuritySessionId](securitysessionid.md)
  A type that contains an authorization session identifier.
### Result Codes
- [Sessions API Result Codes](sessions-api-result-codes.md)
  Recognize result codes specific to the sessions API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sessions)*