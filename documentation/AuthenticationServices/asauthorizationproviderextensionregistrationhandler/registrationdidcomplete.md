# registrationDidComplete()

**Framework**: Authentication Services  
**Kind**: method

Calls the extension to allow it to complete registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
optional func registrationDidComplete()
```

#### Discussion

The system calls this method once after all current registration calls complete. The extension may free any resources it allocates during registration.

## See Also

- [func beginDeviceRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, options: ASAuthorizationProviderExtensionRequestOptions, completion: (ASAuthorizationProviderExtensionRegistrationResult) -> Void)](asauthorizationproviderextensionregistrationhandler/begindeviceregistration(loginmanager:options:completion:).md)
  Initiates the device registration process for the single sign-on extension.
- [func beginUserRegistration(loginManager: ASAuthorizationProviderExtensionLoginManager, userName: String?, method: ASAuthorizationProviderExtensionAuthenticationMethod, options: ASAuthorizationProviderExtensionRequestOptions, completion: (ASAuthorizationProviderExtensionRegistrationResult) -> Void)](asauthorizationproviderextensionregistrationhandler/beginuserregistration(loginmanager:username:method:options:completion:).md)
  Initiates the user registration process for the user and the single sign-on extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/registrationdidcomplete())*