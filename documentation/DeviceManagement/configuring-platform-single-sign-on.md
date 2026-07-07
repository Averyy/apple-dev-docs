# Configuring Platform Single Sign-on

**Framework**: Device Management

Provide a seamless login and authentication experience when integrating with your identity provider.

#### Overview

With Platform Single Sign-on (Platform SSO), people can use their organizational identity throughout macOS starting with the initial setup instead of having to repeatedly interact with authentication prompts. To use Platform SSO, you need to deploy and configure an SSO extension compatible with your identity provider that implements the Platform SSO framework.

To configure Platform SSO, deploy the [`ExtensibleSSO`](extensiblesso.md) configuration or the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile to your devices, which needs to include at a minimum the following keys:

| Key | Required | Value |
| --- | --- | --- |
| `PlatformSSO` | Yes | The dictionary must contain the keys required for the desired feature. For more information about the keys, see the sections that follow. |
| `Type` | Yes | Set to `Redirect`. |

The [`ExtensibleSSO`](extensiblesso.md) configuration and the [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) profile can be assigned to the device and the user channel. If you configure the same key on both, the device channel configuration takes precedence. If you assign `RegistrationToken` or `ExtensionData` to the user channel to provide user-specific settings, the device merges them before the Platform SSO initiates the registration process.

#### Register Devices and Users

Use the `Account.DisplayName` (configuration) or `AccountDisplayName` (profile) key to define the name that appears to the user in notifications and authentication requests. For example, set `Account.DisplayName` to *Mélard ID* to tell the user to enter their organizational identity from *Mélard*.

Set `Account.SynchronizeProfilePicture` (configuration) and `SynchronizeProfilePicture` (profile) to have SSO update the local account profile picture during user creation as well as daily from the identity provider.

After completing registration with the identity provider, the SSO extension works with Platform SSO when processing SSO requests. For example, the SSO extension can:

- Update the login configuration.
- Update SSO tokens.
- Request that the user authenticates again, such as if their credentials expire.
- Access the device keys to sign, encrypt, and decrypt their own additional requests.
- Restart registration if there’s an unrecoverable error.

To silently register a device with the identity provider, use one or both of the following methods:

- The `RegistrationToken` key, set to the value of a registration token provided by your identity provider.
- Attestation, which provides strong assurance that the SSO keys are created on genuine Apple hardware. By default, the attestation includes OID `1.2.840.113635.100.8.11.1` representing the freshness code. Additionally, you can set `AllowDeviceIdentifiersInAttestation` to `true`, which causes the attestation to include: - Serial number (OID `1.2.840.113635.100.8.9.1`)
- UDID (OID `1.2.840.113635.100.8.9.2`).

For more information, see [`https://support.apple.com/guide/security/sec8a37b4cb2`](https://developer.apple.comhttps://support.apple.com/guide/security/sec8a37b4cb2).

#### Use Shared Device Keys

If your SSO extension supports shared device keys, use them whenever possible and set `UseSharedDeviceKeys` to `true`.

#### Configure Authentication Methods

Two keys influence which authentication method you can use.

The `UserCreation.NewUserAuthenticationMethods` (configuration) and `NewUserAuthenticationMethods` (profile) keys influence which authentication method you can use to perform the initial authentication with the identity provider and complete user registration. The key refers to an array of the following values, which allow the corresponding authentication method:

- `AccessKey`
- `OpenID`
- `Password`
- `SmartCard`

If you don’t specify `UserCreation.NewUserAuthenticationMethods` (configuration) or `NewUserAuthenticationMethods` (profile), `Password` and `SmartCard` are available by default. Users can also use an access key to unlock the screen during an Authenticated Guest Mode session.

The method required for device registration is determined by the identity provider and doesn’t use this key. If the identity provider provides the necessary user information and tokens as part of the device registration and `UserSecureEnclaveKey` is configured as the `AuthenticationMethod`, the user isn’t prompted again to perform user registration. The Platform SSO extension can provision the Secure Enclave-backed key and register it with the identity provider in the background.

After the user performs the initial authentication to crate a local user account, `AuthenticationMethod` defines the authentication method to use for subsequent logins and can be set to one of the following values:

- `OpenID`
- `Password`
- `SmartCard`
- `UserSecureEnclaveKey`

Both keys let the user authenticate initially with one method and automatically migrate to another for subsequent logins. Switching methods may prompt the user to complete registration.

> ❗ **Important**:  The SSO extension and identity provider need to support the authentication methods specified in both of these keys. If the configuration is set to an authentication method not supported by the identity provider,  device registration won’t start.

To configure the authentication method, use the following keys:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Defines the authentication method to use for ongoing logins. |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | No | Defines the authentication method to use when creating user accounts. |
| `LoginFrequency` | `LoginFrequency` | No | The duration, in seconds, until Platform SSO requires a full login instead of a refresh. The default value is `64800` (18 hours). The minimum value is `3600` (1 hour). A full login may involve user interaction, for example, to present a smart card or perform biometric authentication. |
| `Policies.NonPlatformSSOAccounts` | `NonPlatformSSOAccounts` | No | Accounts listed in this key are excluded from Platform SSO login policies, Touch ID requirements, and aren’t prompted to register. |

#### Use Web Based Authentication

Users can use web-based authentication if you set `AuthenticationMethod`, `UserCreation.NewUserAuthenticationMethods` (configuration), or `NewUserAuthenticationMethods` (profile) to `OpenID`.

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Set to `OpenID` to use web-based authentication for every login. |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | No | Set to `OpenID` to use web-based authentication during Automated Device Enrollment and for on-demand account creation. |
| `WebAuthentication.URLAllowList` | `WebLoginURLAllowList` | Yes | Provide this if `AuthenticationMethod` or `NewUserAuthenticationMethods` is set to `OpenID`. |
| `Policies.OfflineGracePeriod` | `OfflineGracePeriod` | No | Set this to allow fallback to local user password authentication for a defined number of days. |

The initial sign-in URL of the identity provider to load during the registration process is provided by the SSO extension. Explicitly permit any URL the web view renders (including when using a static OpenID sign-in URL) using the `WebAuthentication.URLAllowList` (configuration) or `WebLoginURLAllowList` (profile) key.

> **Note**:  Fully define each URL using its FQDN and include the scheme and host, for example, `https://login.idp.com`. Web-based authentication with Platform SSO doesn’t support wildcards.

#### Set Up Platform Sso with Automated Device Enrollment

To set up and use Platform SSO during Automated Device Enrollment, the following keys are specifically relevant:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `UserCreation.EnableRegistrationDuringSetup` | `EnableRegistrationDuringSetup` | Yes | Set to `true`. |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Define this value. |
| `UserCreation.EnableFirstUserDuringSetup` | `EnableCreateFirstUserDuringSetup` | No | Set to `false` for unattended enrollments. |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | No | The array can include `OpenID`, `Password`, and `SmartCard`. If not specified, `Password` and `SmartCard` are available. |
| `UserCreation.NewUserAuthorizationMode` | `NewUserAuthorizationMode` | No | Set to `Standard` or `Groups` if the device management service creates a managed administrator account during Setup Assistant. |
| `UserCreation.TokenToUserMapping` | `TokenToUserMapping` | No | Defines which attributes of the identity provider account entry to use for the account name and full name. |
| `Account.SynchronizeProfilePicture` | `SynchronizeProfilePicture` | No | The device uses a profile picture provided by the SSO extension for the created account. |

For more details on the process, see [`Implementing Platform SSO during Automated Device Enrollment`](implementing-platform-sso-during-automated-device-enrollment.md).

#### Require Touch Id

If you configure `AuthenticationMethod` as `Password` or `UserSecureEnclaveKey`, you can require Touch ID and optionally Apple Watch unlock as a second factor. You can define the requirement and a potential fallback individually for FileVault unlock, the Lock Screen, and the login window using the following keys:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Set to `Password` or `UserSecureEnclaveKey`. |
| `Policies.Login` | `LoginPolicy` | No | The array can include `RequireTouchID` or `RequireTouchIDOrWatch` to require a second factor at the login window. Additionally, `AllowOpenIDForTouchIDFallback` can be set to allow web-based authentication as a fallback. |
| `Policies.FileVault` | `FileVaultPolicy` | No | The array can include `RequireTouchID` or `RequireTouchIDOrWatch` to require a second factor during the FileVault unlock process. Additionally, `AllowOpenIDForTouchIDFallback` can be set to allow web-based authentication as a fallback. |
| `Policies.Unlock` | `UnlockPolicy` | No | The array can include `RequireTouchID` or `RequireTouchIDOrWatch` to require a second factor at the Lock Screen. Additionally, set `AllowOpenIDForTouchIDFallback` to allow web-based authentication as a fallback. |
| `Policies.NonPlatformSSOAccounts` | `NonPlatformSSOAccounts` | No | Accounts listed in this key are excluded from these policies. |

When configuring `AuthenticationMethod` with `UserSecureEnclaveKey`, the following policies only support the values above as well as `Policies.OfflineGracePeriod` (configuration) and `OfflineGracePeriod` (profile) for web-based authentication fallback:

- `Policies.Login` and `LoginPolicy`.
- `Policies.FileVault` and `FileVaultPolicy`.
- `Policies.Unlock` and `UnlockPolicy`.

You can only use other options, such as `AttemptAuthentication`, with password authentication.

#### Synchronize Passwords

Password synchronization is automatically turned on when `AuthenticationMethod` is set to `Password`. You can optionally turn it on for `OpenID` authentication using the following keys:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Set to `OpenID`. |
| `WebAuthentication.AllowPasswordSync` | `AllowWebLoginPasswordSync` | No | If set to `true`, the password entered in the web sign-in form of the identity provider is captured and synced to the local user account. This requires the identity provider to call a specific Platform SSO JavaScript function on their login page. |

#### Define Login Policies

If you use `Password` as the `AuthenticationMethod`, you can optionally define login policies to change the default behavior.

Define login policies using the following keys:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Set to `Password`. |
| `Policies.Login` | `LoginPolicy` | No | The array needs to include either `AttemptAuthentication` or `RequireAuthentication`. If set to `RequireAuthentication`, the array can optionally include `AllowOfflineGracePeriod` and `AllowAuthenticationGracePeriod`. |
| `Policies.FileVault` | `FileVaultPolicy` | No | The array needs to include either `AttemptAuthentication` or `RequireAuthentication`. If set to `RequireAuthentication`, the array can optionally include `AllowOfflineGracePeriod` and `AllowAuthenticationGracePeriod`. |
| `Policies.Unlock` | `UnlockPolicy` | No | The array needs to include either `AttemptAuthentication` or `RequireAuthentication`. If set to `RequireAuthentication`, the array can optionally include `AllowOfflineGracePeriod`, `AllowAuthenticationGracePeriod`, and `AllowTouchIDOrWatchForUnlock`. |
| `Policies.OfflineGracePeriod` | `OfflineGracePeriod` | No | Set this if `LoginPolicy`, `FileVaultPolicy`, or `UnlockPolicy` contains `AllowOfflineGracePeriod` in its array. |
| `Policies.AuthenticationGracePeriod` | `AuthenticationGracePeriod` | No | Set this if `LoginPolicy`, `FileVaultPolicy`, or `UnlockPolicy` contains `AllowAuthenticationGracePeriod` in its array. |
| `Policies.NonPlatformSSOAccounts` | `NonPlatformSSOAccounts` | No | Accounts listed in this key are excluded from these policies. |

You can set `Policies.Login`, `Policies.FileVault`, and `Policies.Unlock` (configuration) and `LoginPolicy`, `FileVaultPolicy`, and `UnlockPolicy` (profile) individually. If you don’t specify one, the device defaults to requiring the local account password and attempting to authenticate live with the identity provider if the entered password differs from the local user account password.

#### Manage User Privileges

You can set permissions each time a user authenticates using the following key:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `Authorization.UserAuthorizationMode` | `UserAuthorizationMode` | Yes | Set to `Standard`, `Admin`, or `Groups`. |

If you don’t set this key, the device uses the existing permissions.

If set to `Groups`, Platform SSO requests group membership from the identity provider and assigns the corresponding permissions:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `Authorization.AdministratorGroups` | `AdministratorGroups` | No | The list of groups to use for administrator access. Platform SSO creates the local groups with the same name and adds them as subgroups to the administrator group. |
| `Authorization.AdditionalGroups` | `AdditionalGroups` | No | A list of groups available to the system and apps. An entry in this array creates a group inside the local directory if the group doesn’t exist. |
| `Authorization.AuthorizationGroups` | `AuthorizationGroups` | No | A list of access rights as the key and the identity provider group name to be associated with that access right. |

During authentication, the system requests the superset of the groups from the identity provider and the login response contains the group membership for the user. Platform SSO adds the user to the groups the identity provider returns and removes the user from the rest of the groups. You can trust these group memberships for security decisions because the identity provider signed them during the login and the system didn’t make a separate request for it. The system only updates group membership after user authentication.

The groups are normal local groups on a Mac computer and other processes can modify their membership. Administrators need to ensure there are sufficient controls and auditing processes in place to handle unauthorized changes.

> ❗ **Important**:  To help ensure good performance and proper use, the number of groups is limited to 100. Identity providers may have lower limits. Use the groups for macOS, not for every group and every application in the organization. When using modern authentication, each application should independently request the groups necessary for itself.

#### Turn on Network Authorization

To turn on network authorization based on group membership as defined by `Authorization.AdministratorGroups`, `Authorization.AdditionalGroups`, `Authorization.AuthorizationGroups` (configuration) and `AdministratorGroups`, `AdditionalGroups`, and `AuthorizationGroups` (profile), set the following keys:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `Authorization.EnableIdentityProviderAccounts` | `EnableAuthorization` | Yes | Set to `true`. |

#### Create User Accounts on Demand

Platform SSO can create a new user at the login window. The system checks that there isn’t an existing local account with the same login user name and unique identifier for the user before it creates a new account. Identity providers need to ensure `uniqueIdentifierClaimName` is correctly set to avoid duplicates.

To configure on-demand account creation, the following keys are specifically relevant:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `UserCreation.EnableAtLogin` | `EnableCreateUserAtLogin` | Yes | Set to `true`. |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Define this value. |
| `UserCreation.EnableRegistrationDuringSetup` | `EnableRegistrationDuringSetup` | No | Set to `true` for an unattended enrollment flow using Auto Advance. |
| `UserCreation.EnableFirstUserDuringSetup` | `EnableCreateFirstUserDuringSetup` | No | Set to `false` for an unattended enrollment flow using Auto Advance. |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | No | The array can include `OpenID`, `Password`, and `SmartCard`. If not specified, `Password` and `SmartCard` are available. |
| `UserCreation.NewUserAuthorizationMode` | `NewUserAuthorizationMode` | No | Set to `Standard`, `Admin`, or `Groups`. |
| `Authorization.UserAuthorizationMode` | `UserAuthorizationMode` | No | Use this to change the initially assigned account permissions. |
| `UserCreation.TokenToUserMapping` | `TokenToUserMapping` | No | Defines which values of the identity provider entry to use for the account name and full name. |

The system can create new users who authenticate with a smart card when the device has a valid attribute mapping. The mapping needs to use the `PlatformSSO` prefix followed by the user’s login username for the `AltSecurityIdentifier`. In the following mapping example, the `RFC 822 Name is mapped to it:

```xml
<key>AttributeMapping</key>
    <dict>
        <key>dsAttributeString</key>
        <string>dsAttrTypeStandard:AltSecurityIdentities</string>
        <key>fields</key>
        <array>
            <string>RFC 822 Name</string>
        </array>
        <key>formatString</key>
        <string>PlatformSSO:$1</string>
    </dict>
```

For more information, see [`Advanced smart card options on Mac`](https://developer.apple.comhttps://support.apple.com/guide/deployment/dep7b2ede1e3).

For more details on how to configure Automated Device Enrollment with Auto Advance to simplify device setup for use with on-demand created user accounts, see [`Implementing Platform SSO for unattended device enrollment`](implementing-platform-sso-for-unattended-device-enrollment.md).

#### Use Authenticated Guest Mode

Authenticated Guest Mode can use the same unattended setup process as on-demand creation and uses similar keys for configuration:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UseSharedDeviceKeys` | `UseSharedDeviceKeys` | Yes | Set to `true`. |
| `UserCreation.EnableAtLogin` | `EnableCreateUserAtLogin` | Yes | Set to `true`. |
| `AuthenticationMethod` | `AuthenticationMethod` | Yes | Define this value. |
| `UserCreation.EnableRegistrationDuringSetup` | `EnableRegistrationDuringSetup` | No | Set to `true` for an unattended enrollment flow using Auto Advance. |
| `UserCreation.EnableFirstUserDuringSetup` | `EnableCreateFirstUserDuringSetup` | No | Set to `false` for an unattended enrollment flow using Auto Advance. |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | No | The array can include `OpenID`, `Password`, and `SmartCard`. If not specified, `Password` and `SmartCard` are available. |
| `UserCreation.NewUserAuthorizationMode` | `NewUserAuthorizationMode` | Yes | Set to `Temporary`. |
| `Authorization.UserAuthorizationMode` | `UserAuthorizationMode` | No | Set to `Admin` or `Groups` to change the assigned default permissions of `Standard`. |
| `UserCreation.TokenToUserMapping` | `TokenToUserMapping` | No | Defines which values of the identity provider entry to use for the account name and full name. |
| `UserCreation.TemporarySessionQuickLogin` | `TemporarySessionQuickLogin` | No | Set this to `true` for shared environments that have a high frequency of short sessions. |

#### Support Tap to Login

Tap to Login extends Authenticated Guest Mode with a faster and more convenient way to log in. To configure Tap to log in, use the same keys as for Authenticated Guest Mode and the following ones in addition:

| Configuration key | Profile key | Required | Value |
| --- | --- | --- | --- |
| `UserCreation.NewUserAuthenticationMethods` | `NewUserAuthenticationMethods` | Yes | Set to `AccessKey`. |
| `AccessKey.ReaderGroupIdentifier` | `AccessKeyReaderGroupIdentifier` | Yes | The reader group identifier for use with the access key encoded as `Base64` data or `HEXData string. The value needs to match the configured access key. |
| `AccessKey.ReaderIssuerCertificateAssetReference` | `AccessKeyReaderIssuerCertificateUUID` | Yes | Set to the asset (when declarative device management is used) or `PayloadUUID` of a certificate payload containing the issuer certificate of the Terminal identity of the access key. |
| `AccessKey.TerminalIdentityAssetReference` | `AccessKeyTerminalIdentityUUID` | Yes | Set to the asset (when declarative device management is used) or `PayloadUUID` of an identity payload to use as the Terminal identity of the access key. |
| `AccessKey.AllowExpressMode` | `AllowAccessKeyExpressMode` | No | Set to `true` to allow use of the access key in Express Mode. |

## See Also

- [Enrollment with Platform Single Sign-on](enrolling-with-platform-single-sign-on.md)
  Authenticate users during Automated Device Enrollment using Platform Single Sign-on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/configuring-platform-single-sign-on)*