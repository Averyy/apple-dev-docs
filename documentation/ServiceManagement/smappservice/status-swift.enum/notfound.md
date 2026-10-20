# SMAppService.Status.notFound

**Framework**: Service Management  
**Kind**: case  
**Role**: Case

An error occurred and the framework couldn’t find this service.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case notFound
```

```c
SMAppServiceStatusNotFound
```

## See Also

### Constants
- [SMAppService.Status.notRegistered](./notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.enabled](./enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.requiresApproval](./requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/notfound)*