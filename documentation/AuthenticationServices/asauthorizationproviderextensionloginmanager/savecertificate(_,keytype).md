# saveCertificate(_:keyType:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Saves the provided certificate for the key type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func saveCertificate(_ certificate: SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)
```

```objc
- (void) saveCertificate:(SecCertificateRef) certificate keyType:(ASAuthorizationProviderExtensionKeyType) keyType;
```

## Mentions

- [Supporting key requests and key exchange requests](../supporting-key-requests-and-key-exchange-requests.md)
- [Creating a refresh request](../creating-a-refresh-request.md)
- [Creating and validating a login request](../creating-and-validating-a-login-request.md)

## Parameters

- `certificate`: The certificate to save.
- `keyType`: The key type for the certificate.

## See Also

### Performing registration
- [var loginUserName: String?](./loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](./registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](./presentregistrationviewcontroller%28completion%29.md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](./saveloginconfiguration%28_%29.md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:))*