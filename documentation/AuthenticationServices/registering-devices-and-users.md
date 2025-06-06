# Registering devices and users

**Framework**: Authentication Services

Implement device and user registration.

#### Overview

Once you develop a single sign-on (SSO) extension, there’s a sequence of steps that it follows to register devices and users with an identity provider (IdP). Platform SSO calls the extension to perform these steps. First, the extension registers a device, and then it registers users on that device.

Your SSO extension needs to implement the [`ASAuthorizationProviderExtensionRegistrationHandler`](asauthorizationproviderextensionregistrationhandler.md) protocol to support registration. Platform SSO calls these methods when a device or user needs to register with the IdP, or when the system needs to repair an existing registration. The extension repeats the registration calls for each user on a device.

For more information, see [`Creating extensions that support platform SSO`](creating-extensions-that-support-platform-sso.md).

##### Register a Device

An SSO extension registers a device using [`beginDeviceRegistration(loginManager:options:completion:)`](asauthorizationproviderextensionregistrationhandler/begindeviceregistration(loginmanager:options:completion:).md). The extension needs to:

- Register the device with its associated IdP.
- Provide the login configuration to Platform SSO.
- Execute the completion handler.

If there’s a registration token in the Device Management configuration profile, then platform SSO attempts a silent device registration. The extension can use the registration token to authenticate the device with the IdP to avoid prompting the user. If necessary, the system presents a user interface that prompts the user to register and then again calls [`beginDeviceRegistration(loginManager:options:completion:)`](asauthorizationproviderextensionregistrationhandler/begindeviceregistration(loginmanager:options:completion:).md).

If the SSO extension needs to present a user interface during registration, it can call [`presentRegistrationViewController(completion:)`](asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:).md) on the login manager.

You can use the [`ASAuthorizationProviderExtensionKeyType.currentDeviceSigning`](asauthorizationproviderextensionkeytype/currentdevicesigning.md) and [`ASAuthorizationProviderExtensionKeyType.currentDeviceEncryption`](asauthorizationproviderextensionkeytype/currentdeviceencryption.md) key types to access the signing and encryption keys, regardless of the use of shared keys.

When complete, the SSO extension needs to call the completion handler with an [`ASAuthorizationProviderExtensionRegistrationResult`](asauthorizationproviderextensionregistrationresult.md). If the result is [`ASAuthorizationProviderExtensionRegistrationResult.failed`](asauthorizationproviderextensionregistrationresult/failed.md), then platform SSO automatically prompts the user for registration again in about 10 minutes. The user can also use the register button under Settings → Users & Groups → Network Account Server to restart registration. If the result is [`ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry`](asauthorizationproviderextensionregistrationresult/failednoretry.md), then platform SSO doesn’t attempt registration again until the configuration or extension changes.

> 💡 **Tip**:  During device registration, SSO extensions can run as a user or a role account. Device registration is also user-agnostic. So, don’t set user-specific settings such as [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) during registration.

 During device registration, SSO extensions can run as a user or a role account. Device registration is also user-agnostic. So, don’t set user-specific settings such as [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) during registration.

For more information on registering devices and users, see [`ASAuthorizationProviderExtensionRegistrationHandler`](asauthorizationproviderextensionregistrationhandler.md).

##### Register a User

After the device registration completes successfully with a [`ASAuthorizationProviderExtensionRegistrationResult.success`](asauthorizationproviderextensionregistrationresult/success.md) result, the SSO extension initiates user registration through [`beginUserRegistration(loginManager:userName:method:options:completion:)`](asauthorizationproviderextensionregistrationhandler/beginuserregistration(loginmanager:username:method:options:completion:).md). All users on a device use the login configuration, including when the system creates new users during login. You can set user-specific login configuration values that the system supports during user registration by creating an instance of [`ASAuthorizationProviderExtensionUserLoginConfiguration`](asauthorizationproviderextensionuserloginconfiguration.md) and save these values using [`saveUserLoginConfiguration(_:)`](asauthorizationproviderextensionloginmanager/saveuserloginconfiguration(_:).md).

When using shared device keys, the system only starts user registration for each subsequent user on the device. If the system creates new users during login, it prompts the user to start registration when they reach the desktop if necessary. The login manager’s [`saveUserLoginConfiguration(_:)`](asauthorizationproviderextensionloginmanager/saveuserloginconfiguration(_:).md) method specifies per-user login configuration changes. If the user already entered a user name, it’s sent through the `userName` parameter.

The SSO extension needs to call the completion handler when registration completes. The system then prompts the user to authenticate using the new configuration which can use platform SSO immediately.

If the extension supports the new platform SSO 2.0 protocol methods and the system uses password authentication, it calls the key service to provision a new key and bind it to the user account.

## See Also

- [Creating extensions that support platform SSO](creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [protocol ASAuthorizationProviderExtensionRegistrationHandler](asauthorizationproviderextensionregistrationhandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.
- [enum ASAuthorizationProviderExtensionAuthenticationMethod](asauthorizationproviderextensionauthenticationmethod.md)
  The platform single sign-on method for the user.
- [struct ASAuthorizationProviderExtensionRequestOptions](asauthorizationproviderextensionrequestoptions.md)
  The options for the extension to obtain the status of the registration.
- [enum ASAuthorizationProviderExtensionRegistrationResult](asauthorizationproviderextensionregistrationresult.md)
  The registration result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/registering-devices-and-users)*