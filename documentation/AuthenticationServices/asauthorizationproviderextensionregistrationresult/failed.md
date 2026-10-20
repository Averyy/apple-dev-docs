# ASAuthorizationProviderExtensionRegistrationResult.failed

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The registration fails to complete and the system retries later.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case failed
```

```c
ASAuthorizationProviderExtensionRegistrationResultFailed
```

## Mentions

- [Registering devices and users](../registering-devices-and-users.md)

## See Also

### Identifying the results
- [ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry](./failednoretry.md)
  The registration fails to complete and the system doesn’t retry later.
- [ASAuthorizationProviderExtensionRegistrationResult.success](./success.md)
  The registration succeeds.
- [ASAuthorizationProviderExtensionRegistrationResult.userInterfaceRequired](./userinterfacerequired.md)
  The user interface is required to complete registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationresult/failed)*