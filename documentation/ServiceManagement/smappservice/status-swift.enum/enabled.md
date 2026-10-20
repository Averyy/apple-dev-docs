# SMAppService.Status.enabled

**Framework**: Service Management  
**Kind**: case  
**Role**: Case

The service has been successfully registered and is eligible to run.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case enabled
```

```c
SMAppServiceStatusEnabled
```

## See Also

### Constants
- [SMAppService.Status.notRegistered](./notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.requiresApproval](./requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](./notfound.md)
  An error occurred and the framework couldn’t find this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/enabled)*