# ExtensibleSSOPlatformSSO_PoliciesObject

**Framework**: Device Management  
**Kind**: dictionary

Policies for login, unlock, and FileVault behavior.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_PoliciesObject
```

## Properties

- `AuthenticationGracePeriod` (integer): The amount of time after receiving or updating a `Policies.FileVault`, `Policies.Login`, or `Policies.Unlock` that the system can use unregistered local accounts. Required when `AllowAuthenticationGracePeriod` is set.
- `FileVault` ([string]): The policy to apply when using Platform SSO at FileVault unlock on a Mac with Apple silicon. Applies when `AuthenticationMethod` is `Password`. - `AttemptAuthentication`: The device attempts Platform SSO authentication before proceeding. If offline, unlock continues if the local account password matches. If online and the credential is incorrect, then the device requires a successful Platform SSO authentication is required, even if taken offline.
- `RequireAuthentication`: The device requires Platform SSO authentication before proceeding.  If the device is offline and `AllowOfflineGracePeriod` is enabled, then the device uses the offline `OfflineGracePeriod` to determine if the user can proceed or not. If online and the credential is incorrect, then the device requires a valid Platform SSO authentication to proceed, regardless of the `OfflineGracePeriod`. If the account isn’t registered for Platform SSO and `AllowAuthenticationGracePeriod` is enabled, then the device uses `AuthenticationGracePeriod` to determine if the user can proceed or not.
- `AllowOfflineGracePeriod`: The device allows the use of the `OfflineGracePeriod` when `RequireAuthentication` is enabled.  If `AllowOfflineGracePeriod` isn’t set, then the device denies offline access.
- `AllowAuthenticationGracePeriod`: The device allows the use of the `AuthenticationGracePeriod` for other local accounts when `RequireAuthentication` is enabled. The `AuthenticationGracePeriod` starts when any of the policies are updated. If `AllowAuthenticationGracePeriod` isn’t set, then the device denies unregistered account access.
- `RequireTouchID`: The device requires the use of Touch ID (and not Apple Watch) for File Vault unlock.
- `RequireTouchIDOrWatch`: The device requires the use of Touch ID or Apple Watch for File Vault unlock.
- `AllowOpenIDForTouchIDFallback`: The device allows web login as a fallback if touchID fails or isn’t available.
- `Login` ([string]): The policy to apply when using Platform SSO at the Login Window. Applies when `AuthenticationMethod` is `Password`. - `AttemptAuthentication`: The device attempts Platform SSO authentication before proceeding. If offline, login continues if the local account password matches. If online and the credential is incorrect, then the device requires a successful Platform SSO authentication to proceed, even if taken offline.
- `RequireAuthentication`: The device requires Platform SSO authentication before proceeding.  If the device is offline and `AllowOfflineGracePeriod` is enabled, then the device uses the offline `OfflineGracePeriod` to determine if the user can proceed or not. If online and the credential is incorrect, then the device requires a valid Platform SSO authentication to proceed, regardless of the `OfflineGracePeriod`. If the account isn’t registered for Platform SSO and `AllowAuthenticationGracePeriod` is enabled, then the device uses the `AuthenticationGracePeriod` to determine if the user can proceed or not.
- `AllowOfflineGracePeriod`: The device allows the use of the `OfflineGracePeriod` when `RequireAuthentication` is enabled.  If `AllowOfflineGracePeriod` isn’t set, then the device denies offline access. Applies to web login and all offline passwords.
- `AllowAuthenticationGracePeriod`: The device allows the use of the `AuthenticationGracePeriod` for other local accounts when `RequireAuthentication` is enabled. The `AuthenticationGracePeriod` starts when any of the policies have been updated. If `AllowAuthenticationGracePeriod` isn’t set, then the device denies unregistered account access.
- `RequireTouchID`: The device requires the use of Touch ID (and not Apple Watch) for login.
- `RequireTouchIDOrWatch`: The device requires the use of Touch ID or Apple Watch for login.
- `AllowOpenIDForTouchIDFallback`: The device allows web login as fallback if touchID fails or isn’t available.
- `NonPlatformSSOAccounts` ([string]): The list of local accounts that aren’t subject to the `Policies.FileVault`, `Policies.Login`, or `Policies.Unlock` policies. The accounts don’t receive a prompt to register for Platform SSO.
- `OfflineGracePeriod` (integer): The amount of time after the last successful Platform SSO login for using a local account password offline. Required when setting `AllowOfflineGracePeriod`.
- `Unlock` ([string]): The policy to apply when using Platform SSO at screensaver unlock. Applies when `AuthenticationMethod` is `Password`. later. - `AttemptAuthentication`: The device attempts Platform SSO authentication before proceeding. If offline, unlock will continue if the local account password matches. If online and the credential is incorrect, then the device requires a successful Platform SSO authentication to proceed, even if taken offline.
- `RequireAuthentication`: The device requires Platform SSO authentication before proceeding.  If the device is offline and `AllowOfflineGracePeriod` is enabled, then the offline `OfflineGracePeriod` is used to determine if the user can proceed or not. If online and the credential is incorrect, then the device requires a valid Platform SSO authentication to proceed regardless of the `OfflineGracePeriod`. If the account isn’t registered for Platform SSO and `AllowAuthenticationGracePeriod` is enabled, then the device uses `AuthenticationGracePeriod` to determine if the user can proceed or not.
- `AllowOfflineGracePeriod`: The device allows the use of the `OfflineGracePeriod` when `RequireAuthentication` is enabled.  If `AllowOfflineGracePeriod` isn’t set, then the device denies offline access.
- `AllowAuthenticationGracePeriod`: The device allows the use of the `AuthenticationGracePeriod` for other local accounts when `RequireAuthentication` is enabled. The `AuthenticationGracePeriod` starts when any of the policies have been updated. If `AllowAuthenticationGracePeriod` isn’t set, then the device denies the unregistered account access.
- `AllowTouchIDOrWatchForUnlock`: The device allows TouchID or Watch to unlock the screensaver instead of Platform SSO authentication when `RequireAuthentication` is enabled.
- `RequireTouchID`: The device requires the use of Touch ID (and not Apple Watch) for unlock.
- `RequireTouchIDOrWatch`: RThe device requires the use of Touch ID or Apple Watch for unlock.
- `AllowOpenIDForTouchIDFallback`: The device allows web login as fallback if touchID fails or isn’t available.

## See Also

- [object ExtensibleSSOPlatformSSO_AccessKeyObject](extensiblessoplatformsso_accesskeyobject.md)
  Settings for Access Key authentication.
- [object ExtensibleSSOPlatformSSO_AccountObject](extensiblessoplatformsso_accountobject.md)
  Account display and profile settings.
- [object ExtensibleSSOPlatformSSO_AuthorizationObject](extensiblessoplatformsso_authorizationobject.md)
  Settings for authorization prompts and group management.
- [object ExtensibleSSOPlatformSSO_UserCreationObject](extensiblessoplatformsso_usercreationobject.md)
  Settings for creating new users via Platform SSO.
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_policiesobject)*