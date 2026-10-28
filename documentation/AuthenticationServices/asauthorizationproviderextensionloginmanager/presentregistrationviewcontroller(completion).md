# presentRegistrationViewController(completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Requests platform single sign-on to show the extension’s view controller to the user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func presentRegistrationViewController(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func presentRegistrationViewController() async throws
```

```objc
- (void) presentRegistrationViewControllerWithCompletion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Registering devices and users](../registering-devices-and-users.md)

## Discussion

This is only valid during registration. If the system can’t show the controller, the completion returns an error.

## Parameters

- `completion`: A completion handler that the method uses to indicate whether the view controller presents successfully, and the specific error if it doesn’t.

## See Also

### Performing registration
- [var loginUserName: String?](./loginusername.md)
  The user name to use when authenticating with the identity provider.
- [var registrationToken: String?](./registrationtoken.md)
  The device registration token from the mobile device management profile.
- [func saveCertificate(SecCertificate, keyType: ASAuthorizationProviderExtensionKeyType)](./savecertificate%28_,keytype%29.md)
  Saves the provided certificate for the key type.
- [func saveLoginConfiguration(ASAuthorizationProviderExtensionLoginConfiguration) throws](./saveloginconfiguration%28_%29.md)
  Saves or replaces the login configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/presentregistrationviewcontroller(completion:))*