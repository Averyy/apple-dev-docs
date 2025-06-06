# SMAppService.Status.enabled

**Framework**: Service Management  
**Kind**: case

The service has been successfully registered and is eligible to run.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
case enabled
```

## See Also

- [SMAppService.Status.notRegistered](smappservice/status-swift.enum/notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.requiresApproval](smappservice/status-swift.enum/requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](smappservice/status-swift.enum/notfound.md)
  An error occurred and the framework couldn’t find this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum/enabled)*