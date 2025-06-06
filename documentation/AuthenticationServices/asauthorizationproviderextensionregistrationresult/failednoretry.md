# ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry

**Framework**: Authentication Services  
**Kind**: case

The registration fails to complete and the system doesn’t retry later.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case failedNoRetry
```

## Mentions

- [Registering devices and users](registering-devices-and-users.md)

#### Discussion

The system attemps to reregister when the mobile device management (MDM) profile changes, or the extension updates.

## See Also

- [ASAuthorizationProviderExtensionRegistrationResult.failed](asauthorizationproviderextensionregistrationresult/failed.md)
  The registration fails to complete and the system retries later.
- [ASAuthorizationProviderExtensionRegistrationResult.success](asauthorizationproviderextensionregistrationresult/success.md)
  The registration succeeds.
- [ASAuthorizationProviderExtensionRegistrationResult.userInterfaceRequired](asauthorizationproviderextensionregistrationresult/userinterfacerequired.md)
  The user interface is required to complete registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationresult/failednoretry)*