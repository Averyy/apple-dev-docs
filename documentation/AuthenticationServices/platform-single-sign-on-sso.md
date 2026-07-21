# Platform Single Sign-on (SSO)

**Framework**: Authentication Services

Provide a Platform Single Sign-on (Platform SSO) extension to integrate your identity provider with macOS.

#### Overview

Platform SSO is a replacement for binding a Mac to directory services. It builds on enterprise SSO extensions to perform single sign-on for apps and websites.

Platform SSO supports the following authentication methods with an identity provider:

- Password: With this method, a user authenticates with the identity provider using a password. This method also supports WS-Trust, allowing the user to authenticate even when using a federated identity provider.
- Secure Enclave–backed key: With this method, a user who logs in to their Mac with a local account password can use a Secure Enclave–backed key to authenticate with the identity provider without a password. The identity provider sets up the Secure Enclave key during the user registration process.
- Web-based: With this method, a user authenticates on a web form that the identity provider presents. This web-based authentication method can also offer multistep authentication flows, and allows camera access for users to sign in by scanning a QR code.
- Smart card: With this method, a user authenticates with the identity provider using a smart card. Register the smart card with the identity provider and configure smart card attribute-mapping on the Mac.
- Access key: With this method, a user uses a pass stored in Apple Wallet to authenticate with the identity provider. As with a smart card, register the access key with the identity provider.

Platform SSO can create new local user accounts on demand at the login window using identity provider credentials. It can also integrate identity provider group membership into macOS. You can use network accounts for authorization, and groups can also authorize network accounts.

#### Implement Platform Sso 20

Platform SSO 2.0 revises the system by adding a new key service for SSO extensions and identity providers. Implement an alternative registration flow and additional login configuration to use it. Because Platform SSO 2.0 adds a new registration flow, the SSO extension must indicate that it supports the key service before Platform SSO can use the service.

The key service registers encryption keys that can unlock the Mac at the login window and screensaver unlock. The key service handles two request types: key creation and Diffie-Hellman key exchange. Platform SSO sends the request to create the key after the user registration call to the SSO extension completes successfully. The system then binds the key to the user’s account and performs multiple key exchange requests during this time. You can use the key service only with shared device keys because it must function before a user unlocks their key bag.

#### Migrate From User Keys to Shared Keys

To migrate from user keys to shared keys, create new Secure Enclave–backed keys and register them with the server. The system calls device registration on the SSO extension with the [`registrationDeviceKeyMigration`](asauthorizationproviderextensionrequestoptions/registrationdevicekeymigration.md) option set. During this call only, both the user keys and the new shared keys become available. You can access them using the `loginManager.key(for:)` method. The SSO extension registers the new shared keys with the server and can use the existing user keys to provide a chain of trust.

After device registration completes successfully, the system calls user registration with the [`registrationDeviceKeyMigration`](asauthorizationproviderextensionrequestoptions/registrationdevicekeymigration.md) option set. At this time, you should also migrate any user-specific login configuration to the [`ASAuthorizationProviderExtensionUserLoginConfiguration`](asauthorizationproviderextensionuserloginconfiguration.md). When user registration completes successfully, the system destroys the user keys and previous login configuration. For subsequent users, you repeat the same user registration flow, and the system destroys the user keys after a successful response.

For more information, see [`Registering devices and users`](registering-devices-and-users.md).

#### Use Sso Tokens

Regardless of authentication method, the system stores SSO tokens in the keychain using the keychain data protection attribute [`kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`](https://developer.apple.com/documentation/Security/kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly) and shares them only with the SSO extension.

The SSO extension then uses the SSO tokens to authenticate the user to their on-premises apps and on websites as needed. If the SSO tokens are missing, expired, or more than four hours old, Platform SSO refreshes or retrieves new tokens from the identity provider. The system can also retrieve Kerberos TGTs, import them to a credential cache, and (optionally) share them with the Kerberos SSO extension.

#### Configure Platform Sso Using Device Management

Use [`Device Management`](https://developer.apple.com/documentation/DeviceManagement) to securely configure Platform SSO, including registering devices and users, configuring groups, and managing account permissions.

For more information, see [`Configuring Platform Single Sign-on`](https://developer.apple.com/documentation/DeviceManagement/configuring-platform-single-sign-on).

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
- [Configuring authentication with the identity provider (IdP)](configuring-authentication-with-the-identity-provider-idp.md)
  Specify how Platform SSO authenticates with the identity provider.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.
- [Configuring Platform Single Sign-on](../DeviceManagement/configuring-platform-single-sign-on.md)
  Provide a seamless login and authentication experience when integrating with your identity provider.
### Authentication
- [Authentication process](authentication-process.md)
  Use a system-supported method to authenticate with an identity provider.
- [Implementing web-based authentication with Platform Single Sign-on](implementing-web-based-authentication.md)
  Support modern, phishing-resistant, and flexible authentication methods.
- [class ASAuthorizationProviderExtensionKerberosMapping](asauthorizationproviderextensionkerberosmapping.md)
  A set of Kerberos mappings that the system login process uses.

## See Also

- [Enterprise single sign-on (SSO)](enterprise-single-sign-on-sso.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/platform-single-sign-on-sso)*