# Authorization Name Tags

**Framework**: Security

Use name tags to define authorization security items.

#### Overview

These tags are possible values for the `name` field of an [`AuthorizationItem`](authorizationitem.md) structure. This is not an all-inclusive set. You determine the name of the right to request. These environment tags are for future use.

## Topics

### Constants
- [var kAuthorizationEnvironmentUsername: String](kauthorizationenvironmentusername.md)
  The type for an authorization item containing a user name.
- [var kAuthorizationEnvironmentPassword: String](kauthorizationenvironmentpassword.md)
  The type for an authorization item containing a password.
- [var kAuthorizationEnvironmentShared: String](kauthorizationenvironmentshared.md)
  The type for an authorization item containing a shared right.
- [var kAuthorizationRightExecute: String](kauthorizationrightexecute.md)
  The type for an authorization item requesting the right to execute with privileges.
- [var kAuthorizationEnvironmentPrompt: String](kauthorizationenvironmentprompt.md)
  The type for an authorization item containing the name of the item that should be passed into the environment when specifying invocation-specific additional text.
- [var kAuthorizationEnvironmentIcon: String](kauthorizationenvironmenticon.md)
  The type for an authorization item containing the name of the item that should be passed into the environment when specifying an alternate icon.
- [var kAuthorizationPamResult: String](kauthorizationpamresult.md)
  The type for an authorization item containing a return code from a Pluggable Authentication Module (PAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorization-name-tags)*