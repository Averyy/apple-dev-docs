# NetService.ErrorCode

**Framework**: Foundation  
**Kind**: enum

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

## Topics

### Constants
- [NetService.ErrorCode.unknownError](netservice/errorcode-swift.enum/unknownerror.md)
  An unknown error occurred.
- [NetService.ErrorCode.collisionError](netservice/errorcode-swift.enum/collisionerror.md)
  The service could not be published because the name is already in use. The name could be in use locally or on another system.
- [NetService.ErrorCode.notFoundError](netservice/errorcode-swift.enum/notfounderror.md)
  The service could not be found on the network.
- [NetService.ErrorCode.activityInProgress](netservice/errorcode-swift.enum/activityinprogress.md)
  The net service cannot process the request at this time. No additional information about the network state is known.
- [NetService.ErrorCode.badArgumentError](netservice/errorcode-swift.enum/badargumenterror.md)
  An invalid argument was used when creating the `NSNetService` object.
- [NetService.ErrorCode.cancelledError](netservice/errorcode-swift.enum/cancellederror.md)
  The client canceled the action.
- [NetService.ErrorCode.invalidError](netservice/errorcode-swift.enum/invaliderror.md)
  The net service was improperly configured.
- [NetService.ErrorCode.timeoutError](netservice/errorcode-swift.enum/timeouterror.md)
  The net service has timed out.
### Enumeration Cases
- [NetService.ErrorCode.missingRequiredConfigurationError](netservice/errorcode-swift.enum/missingrequiredconfigurationerror.md)
### Initializers
- [init?(rawValue: Int)](netservice/errorcode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSNetServices Errors](nsnetservices-errors.md)
  If an error occurs, the delegate error-handling methods return a dictionary with the following keys.
- [NetService.Options](netservice/options.md)
  These constants specify options for a network service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/errorcode-swift.enum)*