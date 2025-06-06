# Policy Database Constants

**Framework**: Security

Use these constants to set rights and rules in the policy database.

#### Overview

Use these constants when creating or modifying a rule in the policy database using the [`AuthorizationRightSet(_:_:_:_:_:_:)`](authorizationrightset(_:_:_:_:_:_:).md) function.

## Topics

### Constants
- [var kAuthorizationRightRule: String](kauthorizationrightrule.md)
  Indicates a rule delegation key.
- [var kAuthorizationRuleIsAdmin: String](kauthorizationruleisadmin.md)
  Indicates a delegate rule definition constant specifying that the user must be an administrator.
- [var kAuthorizationRuleAuthenticateAsAdmin: String](kauthorizationruleauthenticateasadmin.md)
  Indicates a delegate rule definition constant specifying that the user must authenticate as an administrator.
- [var kAuthorizationRuleAuthenticateAsSessionUser: String](kauthorizationruleauthenticateassessionuser.md)
  Indicates a delegate rule definition constant specifying that the user must authenticate as the session owner (logged-in user).
- [var kAuthorizationRuleClassAllow: String](kauthorizationruleclassallow.md)
  Indicates a delegate rule definition constant that always allows the specified right.
- [var kAuthorizationRuleClassDeny: String](kauthorizationruleclassdeny.md)
  Indicates a delegate rule definition constant that always denies the specified right.
- [var kAuthorizationComment: String](kauthorizationcomment.md)
  Indicates comments for a rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/policy-database-constants)*