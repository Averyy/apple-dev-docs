# ExtensibleSSOPlatformSSO_AuthorizationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for authorization prompts and group management.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_AuthorizationObject
```

## Topics

### Objects
- [object ExtensibleSSOPlatformSSO_Authorization_AuthorizationGroupsObject](extensiblessoplatformsso_authorization_authorizationgroupsobject.md)
  The pairing of Authorization Rights to group names. When using this, the system updates the Authorization Right to use the group.

## Properties

- `AdditionalGroups` ([string]): The list of created groups that don’t have administrator access.
- `AdministratorGroups` ([string]): The list of groups to use for administrator access. The system requests membership during authentication.
- `AuthorizationGroups` (ExtensibleSSOPlatformSSO_Authorization_AuthorizationGroupsObject): The pairing of Authorization Rights to group names. When using this, the system updates the Authorization Right to use the group.
- `EnableIdentityProviderAccounts` (boolean): Enables using identity provider accounts at authorization prompts. Requires that `UseSharedDeviceKeys` is `true`. The system assigns groups using `AdministratorGroups`, `AdditionalGroups`, or `AuthorizationGroups`.
- `UserAuthorizationMode` (string): The permission to apply to an account each time the user authenticates. Allowed values: - `Standard`: The account is a standard user.
- `Admin`: The system adds the account to the local administrators group.
- `Groups`: The system assigns group to the account using `AdministratorGroups`, `AdditionalGroups`, or `AuthorizationGroups`.

## See Also

- [object ExtensibleSSOPlatformSSO_AccessKeyObject](extensiblessoplatformsso_accesskeyobject.md)
  Settings for Access Key authentication.
- [object ExtensibleSSOPlatformSSO_AccountObject](extensiblessoplatformsso_accountobject.md)
  Account display and profile settings.
- [object ExtensibleSSOPlatformSSO_PoliciesObject](extensiblessoplatformsso_policiesobject.md)
  Policies for login, unlock, and FileVault behavior.
- [object ExtensibleSSOPlatformSSO_UserCreationObject](extensiblessoplatformsso_usercreationobject.md)
  Settings for creating new users via Platform SSO.
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_authorizationobject)*