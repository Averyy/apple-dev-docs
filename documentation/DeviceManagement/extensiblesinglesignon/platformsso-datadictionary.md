# ExtensibleSingleSignOn.PlatformSSO

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to configure Platform SSO. Requires `Type` to be set to `Redirect`.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object ExtensibleSingleSignOn.PlatformSSO
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

## Topics

### Objects
- [object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups](extensiblesinglesignon/platformsso-data.dictionary/authorizationgroups-data.dictionary.md)
  The pairing of Authorization Rights to group names.
- [object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping](extensiblesinglesignon/platformsso-data.dictionary/tokentousermapping-data.dictionary.md)
  The attribute mapping to use when creating users, or for authorization.

## Properties

- `AccessKeyReaderGroupIdentifier` (data): The reader group identifier for use with the `AccessKey`. The value needs to match the configured access key. Required if `NewUserAuthenticationMethods` contains `AccessKey`.
- `AccessKeyReaderIssuerCertificateUUID` (string): The `PayloadUUID` of a certificate payload for the issuer certificate of the `Terminal` identity of the access key. Other specifications refer to the key as the “Reader CA Public Key”. The key must be an elliptic curve key. Required if `NewUserAuthenticationMethods` includes `AccessKey`. The issuer of the Terminal identity of the access key needs to match this certificate, otherwise the device fails the authentication.
- `AccessKeyTerminalIdentityUUID` (string): The `PayloadUUID` of an identity payload to use as the `Terminal` identity of the access key. The identity needs to be trusted by the access key. Required if `NewUserAuthenticationMethods` includes `AccessKey`. Allowed identity payload types: - `com.apple.security.pkcs12`
- `com.apple.security.acme`
- `com.apple.security.scep`
- `AccountDisplayName` (string): The display name for the account in notifications and authentication requests.
- `AdditionalGroups` ([string]): The list of created groups that don’t have administrator access.
- `AdministratorGroups` ([string]): The list of groups to use for administrator access. The system requests membership during authentication.
- `AllowAccessKeyExpressMode` (boolean): If `true`, the system uses the access key in express mode, and doesn’t require authentication before use.
- `AllowDeviceIdentifiersInAttestation` (boolean): If `true`, the system includes the device UDID and serial number in Platform SSO attestations.
- `AuthenticationGracePeriod` (integer): The amount of time after receiving or updating a `FileVaultPolicy`, `LoginPolicy`, or `UnlockPolicy` that the system can use unregistered local accounts. Required when `AllowAuthenticationGracePeriod` is set. Available in macOS 15 and later.
- `AuthenticationMethod` (string): The Platform SSO authentication method to use with the extension. Requires that the SSO Extension also support the method.
- `AuthorizationGroups` (ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups): The pairing of Authorization Rights to group names. When using this, the system updates the Authorization Right to use the group.
- `EnableAuthorization` (boolean): Enables using identity provider accounts at authorization prompts. Requires that `UseSharedDeviceKeys` is `true`. The system assigns groups using `AdministratorGroups`, `AdditionalGroups`, or `AuthorizationGroups`.
- `EnableCreateFirstUserDuringSetup` (boolean): If `true`, the device uses Platform SSO to create the first user account on the Mac during `Setup Assistant`.
- `EnableCreateUserAtLogin` (boolean): Enables creating users at the Login Window with an `AuthenticationMethod` of either `Password` or `SmartCard`. Requires that `UseSharedDeviceKeys` is `true`.
- `EnableRegistrationDuringSetup` (boolean): If `true`, the system enables the PlatformSSO registration process during Setup Assistant on devices running macOS 26 and later. Set this key to `true` when configuring PlatformSSO before enrollment using the `com.apple.psso.required` error response.
- `FileVaultPolicy` ([string]): The policy to apply when using Platform SSO at FileVault unlock on a Mac with Apple silicon. Applies when `AuthenticationMethod` is `Password`. Available in macOS 15 and later.
- `LoginFrequency` (integer): The duration, in seconds, until the system requires a full login instead of a refresh. The default value is 64,800 (18 hours). The minimum value is 3600 (1 hour).
- `LoginPolicy` ([string]): The policy to apply when using Platform SSO at the Login Window. Applies when `AuthenticationMethod` is `Password`. Available in macOS 15 and later.
- `NewUserAuthenticationMethods` ([string]): The set of authentication methods to use for newly created accounts at login or during `Setup Assistant`. The system uses `Password` and `SmartCard` if this key isn’t present.
- `NewUserAuthorizationMode` (string): The permission to apply to newly created accounts at login. Allowed values: - `Standard`: The account is a standard user.
- `Admin`: The system adds the account to the local administrators group.
- `Groups`: The system assigns groups to the account using `AdministratorGroups`, `AdditionalGroups`, or `AuthorizationGroups`.
- `Temporary`: The system uses a temporary session configuration for newly created accounts at login.
- `NonPlatformSSOAccounts` ([string]): The list of local accounts that aren’t subject to the `FileVaultPolicy`, `LoginPolicy`, or `UnlockPolicy`. The accounts don’t receive a prompt to register for Platform SSO. Available in macOS 15 and later.
- `OfflineGracePeriod` (integer): The amount of time after the last successful Platform SSO login for using a local account password offline. Required when setting `AllowOfflineGracePeriod`. Available in macOS 15 and later.
- `SynchronizeProfilePicture` (boolean): If `true`, the system requests the user’s profile picture from the SSO extension.
- `TemporarySessionQuickLogin` (boolean): If `true`, the system uses a quicker Authenticated Guest Mode login to Mac behavior. The system erases user data from only select locations in the user home directory after each session completes. Once every eight hours the system erases the full user home directory after a session completes. Turn this on for shared environments that have a high frequency of short sessions.
- `TokenToUserMapping` (ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping): The attribute mapping to use when creating users, or for authorization.
- `UnlockPolicy` ([string]): The policy to apply when using Platform SSO at screensaver unlock. Applies when `AuthenticationMethod` is `Password`. Available in macOS 15 and later.
- `UserAuthorizationMode` (string): The permission to apply to an account each time the user authenticates. Allowed values: - **`Standard`**: The account is a standard user.
- **`Admin`**: The system adds the account to the local administrators group.
- **`Groups`**: The system assigns group to the account using `AdministratorGroups`, `AdditionalGroups`, or `AuthorizationGroups`.
- `UseSharedDeviceKeys` (boolean): If `true`, the system uses the same signing and encryption keys for all users. Only supported on the device channel.

## See Also

- [object ExtensibleSingleSignOn.ExtensionData](extensiblesinglesignon/extensiondata-data.dictionary.md)
  The additional data to pass to the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary)*