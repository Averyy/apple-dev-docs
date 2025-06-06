# registrationToken

**Framework**: Authentication Services  
**Kind**: property

The device registration token from the mobile device management profile.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var registrationToken: String? { get }
```

## See Also

- [var loginUserName: String?](asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:).md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:).md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/registrationtoken)*