# saveCertificate(_:keyType:)

**Framework**: Authentication Services  
**Kind**: method

Saves the provided certificate for the key type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func saveCertificate(_ certificate: SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)
```

## Mentions

- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
- [Creating a refresh request](creating-a-refresh-request.md)

## Parameters

- `certificate`: The certificate to save.
- `keyType`: The key type for the certificate.

## See Also

- [var loginUserName: String?](asauthorizationproviderextensionloginmanager/loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](asauthorizationproviderextensionloginmanager/registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:).md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:).md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:))*