# ASAuthorizationProviderExtensionRegistrationResult

**Framework**: Authentication Services  
**Kind**: enum

The registration result.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum ASAuthorizationProviderExtensionRegistrationResult
```

## Mentions

- [Registering devices and users](registering-devices-and-users.md)

## Topics

### Identifying the results
- [ASAuthorizationProviderExtensionRegistrationResult.failed](asauthorizationproviderextensionregistrationresult/failed.md)
  The registration fails to complete and the system retries later.
- [ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry](asauthorizationproviderextensionregistrationresult/failednoretry.md)
  The registration fails to complete and the system doesn’t retry later.
- [ASAuthorizationProviderExtensionRegistrationResult.success](asauthorizationproviderextensionregistrationresult/success.md)
  The registration succeeds.
- [ASAuthorizationProviderExtensionRegistrationResult.userInterfaceRequired](asauthorizationproviderextensionregistrationresult/userinterfacerequired.md)
  The user interface is required to complete registration.
### Initializers
- [init?(rawValue: Int)](asauthorizationproviderextensionregistrationresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating extensions that support Platform SSO](creating-extensions-that-support-platform-sso.md)
  Configure capabilities and authentication options for extensions.
- [Registering devices and users](registering-devices-and-users.md)
  Implement device and user registration.
- [protocol ASAuthorizationProviderExtensionRegistrationHandler](asauthorizationproviderextensionregistrationhandler.md)
  An interface through which a single sign-on (SSO) authentication provider extension registers users and devices for platform SSO.
- [enum ASAuthorizationProviderExtensionAuthenticationMethod](asauthorizationproviderextensionauthenticationmethod.md)
  The platform single sign-on method for the user.
- [struct ASAuthorizationProviderExtensionRequestOptions](asauthorizationproviderextensionrequestoptions.md)
  The options for the extension to obtain the status of the registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationresult)*