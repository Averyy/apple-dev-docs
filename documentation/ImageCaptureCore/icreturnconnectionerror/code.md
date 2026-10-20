# ICReturnConnectionError.Code

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum ICReturnConnectionErrorCode : NSInteger;
```

## Topics

### Error Cases
- [ICReturnConnectionError.Code.closedSessionSuddenly](./code/closedsessionsuddenly.md)
  Device closed session without request.
- [ICReturnConnectionError.Code.driverExited](./code/driverexited.md)
  Device driver exited without request.
- [ICReturnConnectionError.Code.ejectedSuddenly](./code/ejectedsuddenly.md)
  Device ejected without request.
- [ICReturnConnectionError.Code.ejectFailed](./code/ejectfailed.md)
  Device reports eject has failed.
- [ICReturnConnectionError.Code.failedToOpen](./code/failedtoopen.md)
  Failed to open a connection to the device.
- [ICReturnConnectionError.Code.failedToOpenDevice](./code/failedtoopendevice.md)
  Failed to open the device.
- [ICReturnConnectionError.Code.sessionAlreadyOpen](./code/sessionalreadyopen.md)
  Device reports session is already open.
- [ICReturnConnectionError.Code.closedSessionSuddenly](./code/closedsessionsuddenly.md)
  Device closed session without request.
- [ICReturnConnectionError.Code.driverExited](./code/driverexited.md)
  Device driver exited without request.
- [ICReturnConnectionError.Code.ejectedSuddenly](./code/ejectedsuddenly.md)
  Device ejected without request.
- [ICReturnConnectionError.Code.ejectFailed](./code/ejectfailed.md)
  Device reports eject has failed.
- [ICReturnConnectionError.Code.failedToOpen](./code/failedtoopen.md)
  Failed to open a connection to the device.
- [ICReturnConnectionError.Code.failedToOpenDevice](./code/failedtoopendevice.md)
  Failed to open the device.
- [ICReturnConnectionError.Code.sessionAlreadyOpen](./code/sessionalreadyopen.md)
  Device reports session is already open.
### Enumeration Cases
- [ICReturnConnectionError.Code.notAuthorizedToOpenDevice](./code/notauthorizedtoopendevice.md)
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

### Error Codes
- [static var closedSessionSuddenly: ICReturnConnectionError.Code](./closedsessionsuddenly.md)
  Device closed session without request.
- [static var driverExited: ICReturnConnectionError.Code](./driverexited.md)
  Device driver exited without request.
- [static var ejectFailed: ICReturnConnectionError.Code](./ejectfailed.md)
  Device reports eject has failed.
- [static var ejectedSuddenly: ICReturnConnectionError.Code](./ejectedsuddenly.md)
  Device ejected without request.
- [static var failedToOpen: ICReturnConnectionError.Code](./failedtoopen.md)
  Failed to open a connection to the device.
- [static var failedToOpenDevice: ICReturnConnectionError.Code](./failedtoopendevice.md)
  Failed to open the device.
- [static var sessionAlreadyOpen: ICReturnConnectionError.Code](./sessionalreadyopen.md)
  Device reports session is already open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnconnectionerror/code)*