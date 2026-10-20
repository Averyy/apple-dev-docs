# SMAppService.Status

**Framework**: Service Management  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the registration or authorization status of a helper executable.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
enum Status
```

```c
enum SMAppServiceStatus : NSInteger;
```

## Mentions

- [Updating helper executables from earlier versions of macOS](../updating-helper-executables-from-earlier-versions-of-macos.md)

## Topics

### Constants
- [SMAppService.Status.notRegistered](./status-swift.enum/notregistered.md)
  The service hasn’t registered with the Service Management framework, or the service attempted to reregister after it was already registered.
- [SMAppService.Status.enabled](./status-swift.enum/enabled.md)
  The service has been successfully registered and is eligible to run.
- [SMAppService.Status.requiresApproval](./status-swift.enum/requiresapproval.md)
  The service has been successfully registered, but the user needs to take action in System Preferences.
- [SMAppService.Status.notFound](./status-swift.enum/notfound.md)
  An error occurred and the framework couldn’t find this service.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum)*