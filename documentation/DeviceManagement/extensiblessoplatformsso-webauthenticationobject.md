# ExtensibleSSOPlatformSSO_WebAuthenticationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for web authentication behavior.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_WebAuthenticationObject
```

## Properties

- `AllowPasswordSync` (boolean): If `true`, the system detects the password during web authentication and synchronizes it to the local account password for the user.
- `URLAllowList` ([string]): The set of allowed hosts that the system can load in the PSSO web view. Required if `AuthenticationMethod` is set to `OpenID`, or `UserCreation.AuthenticationMethods` contains `OpenID`.

## See Also

- [object ExtensibleSSOPlatformSSO_AccessKeyObject](extensiblessoplatformsso_accesskeyobject.md)
  Settings for Access Key authentication.
- [object ExtensibleSSOPlatformSSO_AccountObject](extensiblessoplatformsso_accountobject.md)
  Account display and profile settings.
- [object ExtensibleSSOPlatformSSO_AuthorizationObject](extensiblessoplatformsso_authorizationobject.md)
  Settings for authorization prompts and group management.
- [object ExtensibleSSOPlatformSSO_PoliciesObject](extensiblessoplatformsso_policiesobject.md)
  Policies for login, unlock, and FileVault behavior.
- [object ExtensibleSSOPlatformSSO_UserCreationObject](extensiblessoplatformsso_usercreationobject.md)
  Settings for creating new users via Platform SSO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_webauthenticationobject)*