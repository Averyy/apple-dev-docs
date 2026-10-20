# NetService.ErrorCode.badArgumentError

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

An invalid argument was used when creating the `NSNetService` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case badArgumentError
```

```c
NSNetServicesBadArgumentError
```

## See Also

### Constants
- [NetService.ErrorCode.unknownError](./unknownerror.md)
  An unknown error occurred.
- [NetService.ErrorCode.collisionError](./collisionerror.md)
  The service could not be published because the name is already in use. The name could be in use locally or on another system.
- [NetService.ErrorCode.notFoundError](./notfounderror.md)
  The service could not be found on the network.
- [NetService.ErrorCode.activityInProgress](./activityinprogress.md)
  The net service cannot process the request at this time. No additional information about the network state is known.
- [NetService.ErrorCode.cancelledError](./cancellederror.md)
  The client canceled the action.
- [NetService.ErrorCode.invalidError](./invaliderror.md)
  The net service was improperly configured.
- [NetService.ErrorCode.timeoutError](./timeouterror.md)
  The net service has timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/errorcode-swift.enum/badargumenterror)*