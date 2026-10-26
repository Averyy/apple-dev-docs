# IOUSBHostAbortOption

**Framework**: IOUSBHost  
**Kind**: enum  
**Role**: Enumeration

Options for aborting pending input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
enum IOUSBHostAbortOption
```

```c
enum IOUSBHostAbortOption : NSUInteger;
```

## Topics

### Options
- [IOUSBHostAbortOption.synchronous](./iousbhostabortoption/synchronous.md)
  The option to abort input/output requests synchronously.
- [IOUSBHostAbortOption.asynchronous](./iousbhostabortoption/asynchronous.md)
  The option to abort input/output requests asynchronously.
### Initializers
- [init?(rawValue: UInt)](./iousbhostabortoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Aborting Device Requests
- [- abortDeviceRequestsWithOption:error:](./iousbhostobject/abortdevicerequestswithoption_error_.md)
  Aborts device requests.
- [- abortDeviceRequestsWithError:](./iousbhostobject/abortdevicerequestswitherror_.md)
  Aborts device requests synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostabortoption)*