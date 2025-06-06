# Configuring Device Management

**Framework**: Authenticationservices

Configure Device Management to support device and user registration for platform SSO.

#### Overview

Enable platform SSO through the `com.apple.extensiblesso` payload in [`Device Management`](https://developer.apple.com/documentation/DeviceManagement), for redirect extensions only, because these extensions are designed for modern authentication. The [`ExtensibleSingleSignOn.PlatformSSO`](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso) dictionary in the payload contains the options to configure platform SSO. These options include choosing which key or keys to use, assigning group membership, creating users during login, and including support for registering devices and users.

> **Note**:  The extension data and registration token is user-specific if there’s a user-scoped `com.apple.extensiblesso` MDM payload for the same extension without the `PlatformSSO` dictionary.

##### Choose Which Keys to Use

Although the only required key is `AuthenticationMethod`, it’s recommended that you use shared device keys through `UseSharedDeviceKeys`. Use `AuthenticationMethod` for all users on the device to authenticate, which has the possible values `Password`, `UserSecureEnclaveKey`, or `SmartCard`. The SSO extension needs to support the requested method to start registration, or to switch methods. For example, a new user account that the system created during login with a username and password can switch to secure enclave backed key or SmartCard after the user reaches the desktop. The SSO extension can use the `RegistrationToken` for silent device registration.

To use the recommended shared device keys, the Device Management profile needs to be a system profile because the configuration applies to all users. But, you can configure user-specific extenstion data and registration tokens for individual users.

For more information about creating and configuring the extension for platform SSO, see [`Creating extensions that support platform SSO`](creating-extensions-that-support-platform-sso.md) and [`ExtensibleSingleSignOn`](https://developer.apple.com/documentation/DeviceManagement/ExtensibleSingleSignOn).

##### Assign Group Membership

Platform SSO uses the Device Management configuration to request group membership from the identity provider (IdP). During device registration, if the Device Management profile specifies `AdministratorGroups`, it creates the local groups with the same name and adds them as sub groups of the admin group. If the profile specifies `AdditionalGroups`, then it creates a local group for them. Handle the use of additional groups separately for other services such as `sudo`. If the profile specifies `AuthorizationGroups`, then it creates a local group and updates the associated authorization right to use that group.

During authentication, the system requests the super set of the groups from the IdP and the login response contains the group membership for the user. Platform SSO adds the user to the groups the IdP returns and removes the user from the rest of the groups. You can trust these group memberships for security decisions because the IdP signed them during the login and the system didn’t make a separate request for it. The system only updates group membership after user authentication.

The groups are normal local groups on the Mac and the membership other processes can modify these groups. Administrators need to ensure there are sufficient controls and auditing processes in place to handle unauthorized changes.

> ❗ **Important**:  To help ensure good performance and proper use, macOS limits the number of groups to about 10. IdPs may also have limits. Each app needs to request the groups it requires. These groups are for use by macOS only.

##### Create User During Login

Platform SSO can create a new user at the login window with the password the user enters, if the MDM `EnableCreateUserAtLogin` and `UseSharedDeviceKeys` profile settings are both `true`. The system checks that there isn’t an existing local account with the same login user name and unique identifier for the user before it creates a new account. The system uses the `TokenToUserMapping` in the Device Management profile when it creates the local account name and short name.

IdPs need to ensure that [`uniqueIdentifierClaimName`](asauthorizationproviderextensionloginconfiguration/uniqueidentifierclaimname.md) is correctly set, to ensure the unique identifier is accurate and avoid duplicates.

The system can create new SmartCard users in macOS when the SmartCard contains a valid attribute mapping. The mapping needs to use the `PlatformSSO` prefix followed by the user’s login username for the `AltSecurityIdentifier`. In the following mapping example, the RFC 822 Name is mapped to it:

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

For more information, see [`Advanced smart card options on Mac`](https://developer.apple.comhttps://support.apple.com/guide/deployment/advanced-smart-card-options-dep7b2ede1e3/web).

##### Register Devices and Users

Identity providers (IdPs) who want to support platform SSO need to implement support for device and user registration. Registration enables the IdP to configure the device and decide if it’s eligible to receive SSO tokens to sign in to any app.

A Mac needs to receive an Device Management configuration profile with the [`ExtensibleSingleSignOn`](https://developer.apple.com/documentation/DeviceManagement/ExtensibleSingleSignOn) payload (`com.apple.extensiblesso`) that contains the authentication method. The authentication method defined in the SSO extension payload needs to be compatible with the authentication method supported and configured by the IdP. For example, if the configuration profile uses authentication with a secure enclave backed key, but the IdP supports only password authentication, then device registration won’t start.

In addition to the authentication method, the SSO extension payload may optionally include a registration token. If it’s present, device registration occurs in the background by default. However, if the IdP requires a user action for registration, the SSO extension prompts the user to confirm registration.

After registration with the IdP is complete, the SSO extension can work with Platform SSO when processing SSO requests. For example, the SSO extension can:

- Update the login configuration.
- Update SSO tokens.
- Request that the user authenticates again, such as if their credentials expire.
- Access the device keys to sign, encrypt, and decrypt their own additional requests.
- Restart registration if there’s an unrecoverable error.

For more information, see [`Registering devices and users`](registering-devices-and-users.md).

## See Also

- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AuthenticationServices/configuring-device-management)*