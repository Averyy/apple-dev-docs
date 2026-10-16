# ExtensibleSSOPlatformSSO_AccountObject

**Framework**: Device Management  
**Kind**: dictionary

Account display and profile settings.

**Availability**:
- macOS 27.0+

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
- [object ExtensibleSSOPlatformSSO_AdditionalHTTPHeadersObject](extensiblessoplatformsso_additionalhttpheadersobject.md)
  A dictionary with keys and values that are strings. The keys are HTTP header names, and the values are HTTP header values. The device adds these headers to nonce, pre-authentication, login, key and key exchange requests for Platform SSO. The device limits the number of headers to 20, the length of the header name to 128 characters, and the length of the header value to 2048 characters.
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