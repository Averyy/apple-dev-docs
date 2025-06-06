# ASAuthorizationProviderExtensionAuthenticationMethod

**Framework**: Authentication Services  
**Kind**: enum

The platform single sign-on method for the user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum ASAuthorizationProviderExtensionAuthenticationMethod
```

## Topics

### Identifying the methods
- [ASAuthorizationProviderExtensionAuthenticationMethod.password](asauthorizationproviderextensionauthenticationmethod/password.md)
  Password authentication.
- [ASAuthorizationProviderExtensionAuthenticationMethod.userSecureEnclaveKey](asauthorizationproviderextensionauthenticationmethod/usersecureenclavekey.md)
  Secure Enclave key authentication.
### Enumeration Cases
- [ASAuthorizationProviderExtensionAuthenticationMethod.smartCard](asauthorizationproviderextensionauthenticationmethod/smartcard.md)
### Initializers
- [init?(rawValue: Int)](asauthorizationproviderextensionauthenticationmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating extensions that support platform SSO](creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [Registering devices and users](registering-devices-and-users.md)
  Implement device and user registration.
- [protocol ASAuthorizationProviderExtensionRegistrationHandler](asauthorizationproviderextensionregistrationhandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.
- [struct ASAuthorizationProviderExtensionRequestOptions](asauthorizationproviderextensionrequestoptions.md)
  The options for the extension to obtain the status of the registration.
- [enum ASAuthorizationProviderExtensionRegistrationResult](asauthorizationproviderextensionregistrationresult.md)
  The registration result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthenticationmethod)*