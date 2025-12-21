# Platform single sign-on (SSO)

**Framework**: Authentication Services

Use credentials from macOS login to perform single sign-on with an identity provider.

#### Overview

Platform single sign-on (SSO) is a replacement for binding to directory services. It builds on enterprise SSO capabilities so SSO extensions can also perform single sign-on for apps and websites. It integrates with macOS and doesn’t use JavaScript or render webpages for authentication.

Platform SSO supports the following authentication methods with an identity provider (IdP):

Platform SSO can create new local user accounts on demand at the login window using IdP credentials, and also integrate IdP group membership with macOS. You can use network accounts for authorization, and groups can also authorize network accounts.

##### Platform Sso 20

Platform SSO 2.0 revises the system by adding a new Key service for SSO extensions and IdPs. When you use it, you need to implement an alternative registration flow and additional login configuration. Given this, the SSO extension must indicate that it supports the Key service before Platform SSO uses it.

The Key service registers encryption keys that can unlock the Mac at the login window and screensaver unlock. Two kinds of requests exist: create a key and perform Diffie-Hellman key exchange. Platform SSO sends the request to create the key after the user registration call to the SSO extension completes successfully. The system then binds the key to the user’s account and performs multiple key exchange requests during this time. You can use the key service only with shared device keys because it must function before a user unlocks their key bag. See more detail on the key service below.

##### Sso Tokens

Regardless of authentication method, the system stores SSO tokens in the keychain using the keychain data protection attribute `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly` and shares them with only the SSO extension. The SSO extension then uses the SSO tokens to authenticate the user to their on-premises apps and on websites as needed. If the SSO tokens are missing, expired, or more than 4 hours old, Platform SSO refreshes or retrieves new tokens from the IdP. The system can also retrieve Kerberos TGTs, import them to a credential cache, and (optionally) share them with the Kerberos SSO extension. For more information, see [`kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`](https://developer.apple.comhttps://developer.apple.com/documentation/security/ksecattraccessibleafterfirstunlockthisdeviceonly).

##### Device Management

Use [`Device Management`](https://developer.apple.com/documentation/DeviceManagement) to securely configure platform SSO, including device and user registration, configuring groups, and managing account permissions.

You can enable Platform SSO through the `com.apple.extensiblesso` device management payload, which applies only to redirect extensions. The PlatformSSO dictionary in the payload contains the Platform SSO options. `AuthenticationMethod` is the only required key, but you should strongly consider using shared device keys with `UseSharedDeviceKeys`. `AuthenticationMethod` specifies the authentication method for all users on the device. The possible values are `UserSecureEnclaveKey`, `Password`, or `SmartCard`. The SSO extension needs to also support the requested method to start registration. You can also switch methods—for example, you can create a new user account during login with a user name and password, then switch to Secure Enclave Backed key or SmartCard after the user reaches the desktop. The SSO extension can use the RegistrationToken for silent device registration.

You need to set the device management profile as a System profile when using shared device keys, because the configuration applies to all users. You can also configure user-specific extension data and registration tokens for individual users. If you have a User scoped `com.apple.extensiblesso` device management payload for the same extension without the PlatformSSO dictionary, the system uses the extension data and registration token for that user.

##### Group Membership

Platform SSO requests group membership from the IdP using the device management configuration. During device registration, if the device management profile specifies `AdministratorGroups`, Platform SSO creates the local groups with the same name and adds them as subgroups of the admin group. If the device management profile specifies `AdditionalGroups`, Platform SSO also creates a local group for them. You need to handle use of the additional groups for other services such as `sudo` separately. If the device management profile specifies `AuthorizationGroups`, Platform SSO creates a local group and updates the associated authorization right to use the group.

During authentication, Platform SSO requests the super set of the groups from the IdP, and the login response contains the group membership for the user. Platform SSO adds the user to the groups returned and removes the user from the rest of the groups. You can trust the group membership for security decisions because the IdP signed them during the login request rather than retrieving them separately. Platform SSO updates the group membership only after authentication for a user.

The groups are normal local groups on the Mac, and other processes could modify the membership. Administrators need to ensure sufficient controls and auditing are in place to prevent unauthorized changes.

[!NOTE] You have an overall limit of 100 groups for performance and proper use. IdPs may also have lower limits. Use the groups for macOS, not for every group and every application in the organization. When using modern authentication, each application should independently request the groups necessary for itself.

## Topics

### Essentials
- [Creating extensions that support Platform SSO](creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [Registering devices and users](registering-devices-and-users.md)
  Implement device and user registration.
- [protocol ASAuthorizationProviderExtensionRegistrationHandler](asauthorizationproviderextensionregistrationhandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.
- [enum ASAuthorizationProviderExtensionAuthenticationMethod](asauthorizationproviderextensionauthenticationmethod.md)
  The platform single sign-on method for the user.
- [struct ASAuthorizationProviderExtensionRequestOptions](asauthorizationproviderextensionrequestoptions.md)
  The options for the extension to obtain the status of the registration.
- [enum ASAuthorizationProviderExtensionRegistrationResult](asauthorizationproviderextensionregistrationresult.md)
  The registration result.
### Configuration
- [Configuring Device Management](configuring-device-management.md)
  Configure Device Management to support device and user registration for Platform SSO.
- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how Platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.
### Authentication
- [Authentication process](authentication-process.md)
  Use a system-supported method to authenticate with an identity provider.
- [class ASAuthorizationProviderExtensionKerberosMapping](asauthorizationproviderextensionkerberosmapping.md)
  A set of Kerberos mappings that the system login process uses.

## See Also

- [Enterprise single sign-on (SSO)](enterprise-single-sign-on-sso.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/platform-single-sign-on-sso)*