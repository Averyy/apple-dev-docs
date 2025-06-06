# SMAppService.Status.notRegistered

**Framework**: Service Management  
**Kind**: case

The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case notRegistered
```

## See Also

- [SMAppService.Status.enabled](smappservice/status-swift.enum/enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.requiresApproval](smappservice/status-swift.enum/requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](smappservice/status-swift.enum/notfound.md)
  An error occurred and the framework couldn’t find this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/notregistered)*