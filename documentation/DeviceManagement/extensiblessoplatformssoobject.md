# ExtensibleSSOPlatformSSOObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to configure Platform SSO.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSOObject
```

## Topics

### Objects
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
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.

## Properties

- `AccessKey` (ExtensibleSSOPlatformSSO_AccessKeyObject): Settings for Access Key authentication.
- `Account` (ExtensibleSSOPlatformSSO_AccountObject): Account display and profile settings.
- `AllowDeviceIdentifiersInAttestation` (boolean): If `true`, the system includes the device UDID and serial number in Platform SSO attestations.
- `AuthenticationMethod` (string): The Platform SSO authentication method to use with the extension. Requires that the SSO Extension also support the method.
- `Authorization` (ExtensibleSSOPlatformSSO_AuthorizationObject): Settings for authorization prompts and group management.
- `LoginFrequency` (integer): The duration, in seconds, until the system requires a full login instead of a refresh. The default value is 64,800 (18 hours). The minimum value is 3600 (1 hour).
- `Policies` (ExtensibleSSOPlatformSSO_PoliciesObject): Policies for login, unlock, and FileVault behavior.
- `RegistrationToken` (string): The token this device uses for registration with Platform SSO. Use it for silent registration with the Identity Provider. Requires that `AuthenticationMethod` in `PlatformSSO` isn’t empty.
- `UserCreation` (ExtensibleSSOPlatformSSO_UserCreationObject): Settings for creating new users via Platform SSO.
- `UseSharedDeviceKeys` (boolean): If `true`, the system uses the same signing and encryption keys for all users. Allowed scopes: system
- `WebAuthentication` (ExtensibleSSOPlatformSSO_WebAuthenticationObject): Settings for web authentication behavior.

## See Also

- [object ExtensibleSSOExtensionDataObject](extensiblessoextensiondataobject.md)
  A dictionary of arbitrary data passed through to the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformssoobject)*