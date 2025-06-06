# SMAppService.Status.requiresApproval

**Framework**: Service Management  
**Kind**: case

The service has been successfully registered, but the user needs to take action in System Preferences.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case requiresApproval
```

#### Discussion

The Service Management framework successfully registered this service, but the user needs to take action in System Settings before the service is eligible to run. The framework also returns this status if the user revokes consent for the service to run in System Settings.

## See Also

- [SMAppService.Status.notRegistered](smappservice/status-swift.enum/notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.enabled](smappservice/status-swift.enum/enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.notFound](smappservice/status-swift.enum/notfound.md)
  An error occurred and the framework couldn’t find this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/requiresapproval)*