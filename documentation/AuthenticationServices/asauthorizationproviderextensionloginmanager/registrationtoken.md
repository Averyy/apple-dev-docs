# registrationToken

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The device registration token from the mobile device management profile.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var registrationToken: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * registrationToken;
```

## See Also

### Performing registration
- [var loginUserName: String?](./loginusername.md)
  The user name to use when authenticating with the identity provider.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](./presentregistrationviewcontroller%28completion%29.md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](./savecertificate%28_,keytype%29.md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](./saveloginconfiguration%28_%29.md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/registrationtoken)*