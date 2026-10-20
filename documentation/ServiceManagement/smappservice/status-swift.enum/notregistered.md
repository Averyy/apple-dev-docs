# SMAppService.Status.notRegistered

**Framework**: Service Management  
**Kind**: case  
**Role**: Case

The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case notRegistered
```

```c
SMAppServiceStatusNotRegistered
```

## See Also

### Constants
- [SMAppService.Status.enabled](./enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.requiresApproval](./requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](./notfound.md)
  An error occurred and the framework couldn’t find this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/notregistered)*