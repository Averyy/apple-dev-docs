# presentRegistrationViewController(completion:)

**Framework**: Authentication Services  
**Kind**: method

Requests platform single sign-on to show the extension’s view controller to the user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func presentRegistrationViewController() async throws
```

## Mentions

- [Registering devices and users](registering-devices-and-users.md)

#### Discussion

This is only valid during registration. If the system can’t show the controller, the completion returns an error.

## Parameters

- `completion`: A completion handler that the method uses to indicate whether the view controller presents successfully, and the specific error if it doesn’t.

## See Also

- [var loginUserName: String?](asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](asauthorizationproviderextensionloginmanager/registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:).md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:))*