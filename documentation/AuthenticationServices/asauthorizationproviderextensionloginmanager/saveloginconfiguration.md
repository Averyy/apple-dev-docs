# saveLoginConfiguration(_:)

**Framework**: Authentication Services  
**Kind**: method

Saves or replaces the login configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func saveLoginConfiguration(_ loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration) throws
```

## Parameters

- `loginConfiguration`: The login configuration to save or replace.

## See Also

- [var loginUserName: String?](asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](asauthorizationproviderextensionloginmanager/registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:).md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md)
  Saves the provided certificate for the key type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:))*