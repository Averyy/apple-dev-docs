# ExtensibleSSOPlatformSSO_UserCreationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for creating new users via Platform SSO.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_UserCreationObject
```

## Topics

### Objects
- [object ExtensibleSSOPlatformSSO_UserCreation_TokenToUserMappingObject](extensiblessoplatformsso_usercreation_tokentousermappingobject.md)
  The attribute mapping to use when creating users, or for authorization.

## Properties

- `EnableAtLogin` (boolean): Enables creating users at the Login Window with an `AuthenticationMethod` of either `Password` or `SmartCard`. Requires that `UseSharedDeviceKeys` is `true`.
- `EnableFirstUserDuringSetup` (boolean): If `true`, the device uses Platform SSO to create the first user account on the Mac during `Setup Assistant`.
- `EnableRegistrationDuringSetup` (boolean): If `true`, the system enables the PlatformSSO registration process during Setup Assistant on devices running macOS 26 and later. Set this key to `true` when configuring PlatformSSO before enrollment using the `com.apple.psso.required` error response.
- `NewUserAuthenticationMethods` ([string]): The set of authentication methods to use for newly created accounts at login or during `Setup Assistant`. The system uses `Password` and `SmartCard` if this key isn’t present.
- `NewUserAuthorizationMode` (string): The permission to apply to newly created accounts at login. Allowed values: - `Standard`: The account is a standard user.
- `Admin`: The system adds the account to the local administrators group.
- `Groups`: The system assigns groups to the account using `Authorization.AdministratorGroups`, `Authorization.AdditionalGroups`, or `Authorization.AuthorizationGroups`.
- `Temporary`: The system uses a temporary session configuration for newly created accounts at login.
- `TemporarySessionQuickLogin` (boolean): If `true`, the system uses a quicker Authenticated Guest Mode login to Mac behavior. The system erases user data from only select locations in the user home directory after each session completes. Once every eight hours the system erases the full user home directory after a session completes. Turn this on for shared environments that have a high frequency of short sessions.
- `TokenToUserMapping` (ExtensibleSSOPlatformSSO_UserCreation_TokenToUserMappingObject): The attribute mapping to use when creating users, or for authorization.

## See Also

- [object ExtensibleSSOPlatformSSO_AccessKeyObject](extensiblessoplatformsso_accesskeyobject.md)
  Settings for Access Key authentication.
- [object ExtensibleSSOPlatformSSO_AccountObject](extensiblessoplatformsso_accountobject.md)
  Account display and profile settings.
- [object ExtensibleSSOPlatformSSO_AuthorizationObject](extensiblessoplatformsso_authorizationobject.md)
  Settings for authorization prompts and group management.
- [object ExtensibleSSOPlatformSSO_PoliciesObject](extensiblessoplatformsso_policiesobject.md)
  Policies for login, unlock, and FileVault behavior.
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_usercreationobject)*