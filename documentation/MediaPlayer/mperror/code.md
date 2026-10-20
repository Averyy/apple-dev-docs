# MPError.Code

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents error codes for framework operations.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.14.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum Code
```

```c
enum MPErrorCode : NSInteger;
```

## Topics

### Error codes
- [MPError.Code.cancelled](./code/cancelled.md)
  An error that indicates the system canceled the requested operation before it completed.
- [MPError.Code.cloudServiceCapabilityMissing](./code/cloudservicecapabilitymissing.md)
  An error that indicates the operation can’t complete because iCloud services aren’t enabled.
- [MPError.Code.networkConnectionFailed](./code/networkconnectionfailed.md)
  An error that indicates the operation failed because the device can’t connect to the network.
- [MPError.Code.notFound](./code/notfound.md)
  An error that indicates the operation failed because the system can’t find the requested identifier in the current storefront.
- [MPError.Code.notSupported](./code/notsupported.md)
  An error that indicates the requested operation failed because the system doesn’t support it.
- [MPError.Code.permissionDenied](./code/permissiondenied.md)
  An error that indicates the operation can’t complete because the user doesn’t have permission to execute the operation.
- [MPError.Code.requestTimedOut](./code/requesttimedout.md)
  An error that indicates the requested operation timed out.
- [MPError.Code.unknown](./code/unknown.md)
  An error that indicates the requested operation can’t complete due to an unknown error.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an error
- [static var errorDomain: String](./errordomain.md)
- [let MPErrorDomain: String](../mperrordomain.md)
  The Media Player framework error domain.
- [Error constants](../error-constants.md)
  Error code constants for framework operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mperror/code)*