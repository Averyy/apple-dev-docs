# Session ID Values

**Framework**: Security

Use these values as placeholders for specific sessions.

#### Discussion

You can use these values as the `session` input to the [`SessionGetInfo(_:_:_:)`](sessiongetinfo(_:_:_:).md) function as a stand-in for specific sessions when you don’t already know the ID for that session. They are  returned in the `sessionId` output of that function. Instead, you receive the actual session ID.

## Topics

### Constants
- [var callerSecuritySession: SecuritySessionId](callersecuritysession.md)
  A value that is a placeholder for the caller’s session.
- [var noSecuritySession: SecuritySessionId](nosecuritysession.md)
  Not a valid session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/session-id-values)*