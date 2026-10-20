# saveLoginConfiguration(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Saves or replaces the login configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func saveLoginConfiguration(_ loginConfiguration: ASAuthorizationProviderExtensionLoginConfiguration) throws
```

```objc
- (BOOL) saveLoginConfiguration:(ASAuthorizationProviderExtensionLoginConfiguration *) loginConfiguration error:(NSError **) error;
```

## Parameters

- `loginConfiguration`: The login configuration to save or replace.

## See Also

### Performing registration
- [var loginUserName: String?](./loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](./registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func presentRegistrationViewController(completion: ((any Error)?) -> Void)](./presentregistrationviewcontroller%28completion%29.md)
  Requests platform single sign-on to show the extension’s view controller to the user.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](./savecertificate%28_,keytype%29.md)
  Saves the provided certificate for the key type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/saveloginconfiguration(_:))*