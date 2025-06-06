# beginUserRegistration(loginManager:userName:method:options:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Initiates the user registration process for the user and the single sign-on extension.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func beginUserRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, userName: String?, method authenticationMethod: ASAuthorizationProviderExtensionAuthenticationMethod, options: ASAuthorizationProviderExtensionRequestOptions = []) async -> ASAuthorizationProviderExtensionRegistrationResult
```

## Mentions

- [Registering devices and users](registering-devices-and-users.md)

#### Discussion

The completion handler returns the status as an [`ASAuthorizationProviderExtensionRegistrationResult`](asauthorizationproviderextensionregistrationresult.md).

## Parameters

- `loginManager`: The login manager for interfacing with platform SSO.
- `userName`: The user name for the user registration.
- `authenticationMethod`: The authentication method to use for the user.
- `options`: The request options that apply to the request.
- `completion`: The completion to call to continue user registration.

## See Also

- [func beginDeviceRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, options: ASAuthorizationProviderExtensionRequestOptions, completion: (ASAuthorizationProviderExtensionRegistrationResult) -> Void)](asauthorizationproviderextensionregistrationhandler/begindeviceregistration(loginmanager:options:completion:).md)
  Initiates the device registration process for the single sign-on extension.
- [func registrationDidComplete()](asauthorizationproviderextensionregistrationhandler/registrationdidcomplete.md)
  Calls the extension to allow it to complete registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/beginuserregistration(loginmanager:username:method:options:completion:))*