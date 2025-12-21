# Configuring authentication with the identity provider (IdP)

**Framework**: Authentication Services

Specify how Platform SSO authenticates with the identity provider.

#### Overview

Use a login configuration to instruct Platform SSO how to authenticate with the identity provider.

Use [`additionalAuthorizationScopes`](asauthorizationproviderextensionloginconfiguration/additionalauthorizationscopes.md) to differentiate authentication requests for network account authorization from other login requests. For example, these requests can return temporary admin group membership.

The [`accountDisplayName`](asauthorizationproviderextensionloginconfiguration/accountdisplayname.md) is the user-friendly name for the IdP, and replaces “identity provider” in notifications and the authentication dialog.

##### Configure for Federation

Federation enables authentication between security domains, such as from a local IdP to a cloud IdP.  You have two options to configure Platform SSO for federation:

To use WS-Trust, set [`federationType`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md) to [`ASAuthorizationProviderExtensionLoginConfiguration.FederationType.wsTrust`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum/wstrust.md). This federation type sends the WS-Trust request to the URLs in the metadata exchange data (MEX) response. The required configuration values are:

To use Dynamic WS-Trust, set [`federationType`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.property.md) to [`ASAuthorizationProviderExtensionLoginConfiguration.FederationType.dynamicWSTrust`](asauthorizationproviderextensionloginconfiguration/federationtype-swift.enum/dynamicwstrust.md). Dynamic WS-Trust sends a preauthentication to the IdP to determine whether to use federation and where to authenticate. The required configuration values are:

##### Use the Login Manager to Interface with Platform Sso

The SSO extension uses [`ASAuthorizationProviderExtensionLoginManager`](asauthorizationproviderextensionloginmanager.md) to interface with Platform SSO. The system provides and instance of the login manager for each authentication request. The login manager can:

- Update the login configuration.
- Update SSO tokens.
- Request that the user authenticate again in the case of expired credentials.
- Access the device keys to sign, encrypt, and decrypt additional requests.
- Restart registration if an unrecoverable error occurs.

If the extension detects that the keys or the device become compromised due to a security exploit, it can reset the keys and request device registration again. In this case, the extension needs to return `failedNoRetry` during registration until macOS is patched.

The loginConfiguration.additionalAuthorizationScopes can be used to differentiate authentication requests for Network Account Authorization from other login requests. For example, temporary admin group membership could be returned for these requests.

##### Migrate From Per User Device Keys to Shared Device Keys

Devices keys represent the device to the IdP. They keys can either be , which means each user on the device has separate keys, or , which means all users on the device use the same keys. Shared device keys enable a device to authenticate with the IdP before a user logs in. Shared keys are available in macOS 14 and later.

The following table summarizes feature availability for per-user device keys and shared device keys:

| Feature | Device Keys  (macOS 13 and later ) | Shared Device Keys |
| --- | --- | --- |
|  |  |  |
| Password | ✓ | ✓ |
| User Secure Enclave key | ✓ | ✓ |
| SmartCard | ✓ | ✓ |
|  |  |  |
| Password |  | ✓ |
| SmartCard |  | ✓ |
|  |  |  |
| Login window |  | ✓  (Platform SSO 2.0 only) |
| Screensaver unlock |  | ✓  (Platform SSO 2.0 only) |
|  |  |  |
| Group membership | ✓ | ✓ |
| Network account authorization |  | ✓ |

To migrate from user keys to shared keys you need to create new secure enclave backed keys and register these with the server. To facilitate this, the system initiates device registration on the SSO extension for migration with the [`registrationDeviceKeyMigration`](asauthorizationproviderextensionrequestoptions/registrationdevicekeymigration.md) option set. Both the user keys and the new shared keys are available only during this call. Use [`key(for:)`](asauthorizationproviderextensionloginmanager/key(for:).md) to access them. The SSO extension needs to register the new shared keys with the server and can use the existing user keys to provide a chain of trust.

When Device registration completes successfully, the system initiates user registration with the [`registrationDeviceKeyMigration`](asauthorizationproviderextensionrequestoptions/registrationdevicekeymigration.md) option set. You also need to migrate any user-specific login configuration to the [`ASAuthorizationProviderExtensionUserLoginConfiguration`](asauthorizationproviderextensionuserloginconfiguration.md) at this time. When user registration completes successfully, the system destroys the user keys and previous login configuration. For subsequent users, the same user registration flow repeats and the system destroys the user keys after a successful response.

## See Also

- [Configuring Device Management](configuring-device-management.md)
  Configure Device Management to support device and user registration for Platform SSO.
- [class ASAuthorizationProviderExtensionLoginConfiguration](asauthorizationproviderextensionloginconfiguration.md)
  An interface for configuring platform single sign-on.
- [class ASAuthorizationProviderExtensionLoginManager](asauthorizationproviderextensionloginmanager.md)
  An interface to maintain platform single sign-on (SSO) during authentication and registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/configuring-authentication-with-the-identity-provider-idp)*