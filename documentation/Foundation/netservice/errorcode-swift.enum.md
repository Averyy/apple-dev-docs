# NetService.ErrorCode

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants identify errors that can occur when accessing net services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum ErrorCode
```

```c
enum NSNetServicesError : NSInteger;
```

## Topics

### Constants
- [NetService.ErrorCode.unknownError](./errorcode-swift.enum/unknownerror.md)
  An unknown error occurred.
- [NetService.ErrorCode.collisionError](./errorcode-swift.enum/collisionerror.md)
  The service could not be published because the name is already in use. The name could be in use locally or on another system.
- [NetService.ErrorCode.notFoundError](./errorcode-swift.enum/notfounderror.md)
  The service could not be found on the network.
- [NetService.ErrorCode.activityInProgress](./errorcode-swift.enum/activityinprogress.md)
  The net service cannot process the request at this time. No additional information about the network state is known.
- [NetService.ErrorCode.badArgumentError](./errorcode-swift.enum/badargumenterror.md)
  An invalid argument was used when creating the `NSNetService` object.
- [NetService.ErrorCode.cancelledError](./errorcode-swift.enum/cancellederror.md)
  The client canceled the action.
- [NetService.ErrorCode.invalidError](./errorcode-swift.enum/invaliderror.md)
  The net service was improperly configured.
- [NetService.ErrorCode.timeoutError](./errorcode-swift.enum/timeouterror.md)
  The net service has timed out.
### Enumeration Cases
- [NetService.ErrorCode.missingRequiredConfigurationError](./errorcode-swift.enum/missingrequiredconfigurationerror.md)
  Missing required configuration for local network access.
### Initializers
- [init?(rawValue: Int)](./errorcode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSNetServices Errors](../nsnetservices-errors.md)
  If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [NetService.Options](./options.md)
  These constants specify options for a network service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/errorcode-swift.enum)*