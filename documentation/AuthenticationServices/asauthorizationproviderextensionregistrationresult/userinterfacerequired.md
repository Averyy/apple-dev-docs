# ASAuthorizationProviderExtensionRegistrationResult.userInterfaceRequired

**Framework**: Authentication Services  
**Kind**: case  
**Role**: Case

The user interface is required to complete registration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case userInterfaceRequired
```

```c
ASAuthorizationProviderExtensionRegistrationResultUserInterfaceRequired
```

## See Also

### Identifying the results
- [ASAuthorizationProviderExtensionRegistrationResult.failed](./failed.md)
  The registration fails to complete and the system retries later.
- [ASAuthorizationProviderExtensionRegistrationResult.failedNoRetry](./failednoretry.md)
  The registration fails to complete and the system doesn’t retry later.
- [ASAuthorizationProviderExtensionRegistrationResult.success](./success.md)
  The registration succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationresult/userinterfacerequired)*