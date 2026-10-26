# IOUSBHostObjectInitOptions

**Framework**: IOUSBHost  
**Kind**: struct  
**Role**: Structure

Options for initializing the host object.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostObjectInitOptions
```

```c
enum IOUSBHostObjectInitOptions : NSUInteger;
```

## Topics

### Options
- [static var deviceCapture: IOUSBHostObjectInitOptions](./iousbhostobjectinitoptions/devicecapture.md)
  The option to capture the device and terminate existing drivers.
- [IOUSBHostObjectInitOptionsNone](./iousbhostobjectinitoptions/iousbhostobjectinitoptionsnone.md)
  The default argument for initializing the host object.
### Initializing the Structure
- [init(rawValue: UInt)](./iousbhostobjectinitoptions/init%28rawvalue%29.md)
  Initializes the object.
### Type Properties
- [static var deviceSeize: IOUSBHostObjectInitOptions](./iousbhostobjectinitoptions/deviceseize.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing the Object Life Cycle
- [typealias IOUSBHostInterestHandler](./iousbhostinteresthandler.md)
  The callback that handles underlying service-state changes.
- [var ioService: io_service_t](./iousbhostobject/ioservice.md)
  A reference to the kernel object.
- [var queue: dispatch_queue_t](./iousbhostobject/queue.md)
  The queue for servicing input/output requests.
- [func destroy()](./iousbhostobject/destroy%28%29.md)
  Removes underlying allocations and connections from the USB host object.
- [- initWithIOService:options:queue:error:interestHandler:](./iousbhostobject/initwithioservice_options_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a communication channel to the kernel.
- [- initWithIOService:queue:error:interestHandler:](./iousbhostobject/initwithioservice_queue_error_interesthandler_.md)
  Creates a USB host object and sets up a default communication channel to the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectinitoptions)*