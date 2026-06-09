# ExtensibleSSOPlatformSSO_AccountObject

**Framework**: Device Management  
**Kind**: dictionary

Account display and profile settings.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_AccountObject
```

## Properties

- `DisplayName` (string): The display name for the account in notifications and authentication requests.
- `SynchronizeProfilePicture` (boolean): If `true`, the system requests the user’s profile picture from the SSO extension.

## See Also

- [object ExtensibleSSOPlatformSSO_AccessKeyObject](extensiblessoplatformsso_accesskeyobject.md)
  Settings for Access Key authentication.
- [object ExtensibleSSOPlatformSSO_AuthorizationObject](extensiblessoplatformsso_authorizationobject.md)
  Settings for authorization prompts and group management.
- [object ExtensibleSSOPlatformSSO_PoliciesObject](extensiblessoplatformsso_policiesobject.md)
  Policies for login, unlock, and FileVault behavior.
- [object ExtensibleSSOPlatformSSO_UserCreationObject](extensiblessoplatformsso_usercreationobject.md)
  Settings for creating new users via Platform SSO.
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_accountobject)*