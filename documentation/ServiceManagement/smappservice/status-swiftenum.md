# SMAppService.Status

**Framework**: Service Management  
**Kind**: enum

Constants that describe the registration or authorization status of a helper executable.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
enum Status
```

## Mentions

- [Updating helper executables from earlier versions of macOS](updating-helper-executables-from-earlier-versions-of-macos.md)

## Topics

### Constants
- [SMAppService.Status.notRegistered](smappservice/status-swift.enum/notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.enabled](smappservice/status-swift.enum/enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.requiresApproval](smappservice/status-swift.enum/requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](smappservice/status-swift.enum/notfound.md)
  An error occurred and the framework couldn’t find this service.
### Initializers
- [init?(rawValue: Int)](smappservice/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum)*