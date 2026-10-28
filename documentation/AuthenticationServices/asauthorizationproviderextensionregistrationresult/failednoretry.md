# ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The registration fails to complete and the system doesn’t retry later.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case failedNoRetry
```

```c
ASAuthorizationProviderExtensionRegistrationResultFailedNoRetry
```

## Mentions

- [Registering devices and users](../registering-devices-and-users.md)

## Discussion

The system attemps to reregister when the mobile device management (MDM) profile changes, or the extension updates.

## See Also

### Identifying the results
- [ASAuthorizationProviderExtensionRegistrationResult.failed](./failed.md)
  The registration fails to complete and the system retries later.
- [ASAuthorizationProviderExtensionRegistrationResult.success](./success.md)
  The registration succeeds.
- [ASAuthorizationProviderExtensionRegistrationResult.userInterfaceRequired](./userinterfacerequired.md)
  The user interface is required to complete registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationresult/failednoretry)*